# ruff: noqa
import datetime
import json
import re
from pydantic import BaseModel, Field
from google.adk.agents import Agent, LlmAgent
from google.adk.tools import AgentTool
from google.adk.workflow import Workflow, START, node
from google.adk.events.event import Event
from google.adk.events.request_input import RequestInput
from google.adk.agents.context import Context
from google.adk.apps import App, ResumabilityConfig
from google.adk.models import Gemini
from google.genai import types

from app.config import config
from app.mcp_server import (
    atlas_weather_context,
    atlas_aqi_context,
    atlas_civic_signal,
    atlas_places_search,
    atlas_safety_rules,
)


# ═══════════════════════════════════════════════════════════════════════════════
# SCHEMAS & MODELS
# ═══════════════════════════════════════════════════════════════════════════════

class UserPlanInput(BaseModel):
    plan: str = Field(description="The natural language decision/plan to evaluate.")

class ScoreBreakdown(BaseModel):
    category: str = Field(description="Safety domain or category.")
    score: int = Field(description="Safety score for this category.")
    max_score: int = Field(description="Maximum possible score for this category.")
    reason: str = Field(description="One-line explanation of the category safety status.")

class ATLASDecisionOutput(BaseModel):
    decision_score: int = Field(description="Overall safety/readiness score (0-100).")
    decision_label: str = Field(description="Overall safety label based on overall score (e.g. Excellent Idea, Good Idea, Okay with Caution, Risky / Consider Alternatives, Not Recommended, Blocked for unsafe request).")
    decision_reason: str = Field(description="One-line summary explaining the overall score.")
    confidence: str = Field(description="Confidence level of the evaluation (e.g. High, Medium, Low, Medium-Low). Since mock/fallback data is used, use Medium-Low or Medium.")
    score_breakdown: list[ScoreBreakdown] = Field(description="Detailed breakdown of component scores.")
    recommendations: list[str] = Field(description="Actionable recommendations for safety/readiness.")
    agent_trace: list[str] = Field(description="List of agents activated during execution.")
    tool_trace: list[str] = Field(description="List of tools activated during execution.")
    security_trace: list[str] = Field(description="List of security events or actions.")
    safety_validation: str = Field(description="Validation status (e.g., PASSED, FAILED, HUMAN_REVIEW).")
    fallback_used: bool = Field(description="Whether mock or fallback data was used.")


# Intermediate sub-agent schemas
class DestinationReadinessOutput(BaseModel):
    weather_score: int
    readiness_reason: str
    recommendations: list[str]

class FoodPlaceOutput(BaseModel):
    hygiene_score: int
    food_safety_reason: str
    recommendations: list[str]

# ═══════════════════════════════════════════════════════════════════════════════
# AGENTS SETUP
# ═══════════════════════════════════════════════════════════════════════════════

gemini_model = Gemini(
    model=config.model,
    retry_options=types.HttpRetryOptions(attempts=3),
)

# 1. Destination Readiness Agent
destination_agent = LlmAgent(
    name="destination_agent",
    model=gemini_model,
    instruction=(
        "You are the ATLAS Destination Readiness Agent.\n"
        "Analyze travel, lodging, transit, or weather readiness of a plan.\n"
        "Ensure no real locations are used; enforce neutral locations: 'Coastal City', 'Sample Destination'.\n"
        "Use your weather, AQI, civic signal, and safety rules tools to gather local safety context.\n"
        "Provide a weather_score (0-100), readiness_reason (one line), and recommendations."
    ),
    output_schema=DestinationReadinessOutput,
    tools=[atlas_weather_context, atlas_aqi_context, atlas_civic_signal, atlas_safety_rules],
)

# 2. Food & Place Agent
food_place_agent = LlmAgent(
    name="food_place_agent",
    model=gemini_model,
    instruction=(
        "You are the ATLAS Food & Place Agent.\n"
        "Analyze dining safety, restaurant selection, food allergens, or place hygiene of a plan.\n"
        "Ensure no real locations are used; enforce neutral locations: 'Sample City Center', 'Sample Downtown'.\n"
        "Use your places search, safety rules, and AQI tools to find safe dining/places information.\n"
        "Provide a hygiene_score (0-100), food_safety_reason (one line), and recommendations."
    ),
    output_schema=FoodPlaceOutput,
    tools=[atlas_places_search, atlas_safety_rules, atlas_aqi_context],
)

# 3. Commander Agent (using AgentTools for delegation)
commander_agent = LlmAgent(
    name="commander_agent",
    model=gemini_model,
    instruction=(
        "You are the ATLAS Commander Agent.\n"
        "Your task is to coordinate the safety evaluation of the user's plan.\n"
        "Delegate tasks to your sub-agents (destination_agent or food_place_agent) as appropriate using their tools.\n"
        "Always use neutral placeholders: 'Coastal City', 'Sample City Center', 'Sample Downtown', 'Sample Destination'.\n"
        "Summarize the findings and report which agents/tools were activated."
    ),
    tools=[AgentTool(destination_agent), AgentTool(food_place_agent)],
)

# 4. Decision Scoring Agent
decision_scoring_agent = LlmAgent(
    name="decision_scoring_agent",
    model=gemini_model,
    instruction=(
        "You are the ATLAS Decision Scoring Agent.\n"
        "Generate the final ATLASDecisionOutput based on findings in the context.\n"
        "Calculate the overall score (0-100) using the following weights:\n\n"
        "For Destination Readiness mission:\n"
        "- Weather: max 25\n"
        "- AQI: max 20\n"
        "- Civic signals: max 20\n"
        "- Destination readiness: max 15\n"
        "- User context: max 10\n"
        "- Safety validation: max 10\n\n"
        "For Food & Place mission:\n"
        "- Place quality: max 30\n"
        "- Open/distance convenience: max 15\n"
        "- Weather comfort: max 15\n"
        "- AQI comfort: max 15\n"
        "- Civic stability: max 10\n"
        "- User context: max 5\n"
        "- Safety validation: max 10\n\n"
        "Map the overall score to one of these labels:\n"
        "- 90–100: Excellent Idea\n"
        "- 75–89: Good Idea\n"
        "- 60–74: Okay with Caution\n"
        "- 40–59: Risky / Consider Alternatives\n"
        "- 0–39: Not Recommended\n"
        "- Blocked for unsafe request\n\n"
        "Set confidence to 'Medium-Low' because fallback/mock data is used.\n"
        "Every breakdown item must have score, max_score, and a one-line reason."
    ),
    output_schema=ATLASDecisionOutput,
)


# ═══════════════════════════════════════════════════════════════════════════════
# WORKFLOW NODES
# ═══════════════════════════════════════════════════════════════════════════════

@node
def safety_policy_agent(ctx: Context, node_input: types.Content) -> Event:
    # 0. Extract Plan Text (robustly supporting Content and Pydantic objects)
    if hasattr(node_input, "parts") and node_input.parts:
        plan_text = node_input.parts[0].text or ""
    elif isinstance(node_input, dict) and "plan" in node_input:
        plan_text = node_input["plan"]
    elif hasattr(node_input, "plan"):
        plan_text = getattr(node_input, "plan")
    else:
        plan_text = str(node_input)
    detected_flags = []

    blocked_reason = ""
    safety_status = "PASSED"
    severity = "INFO"
    
    # 1. Infer Mission Type
    plan_lower = plan_text.lower()
    mission_type = "destination_readiness"
    if any(kw in plan_lower for kw in ["food", "eat", "restaurant", "cafe", "diner", "mediterranean", "cuisine"]):
        mission_type = "food_place"
    
    # Check for safety_block triggers
    if any(kw in plan_lower for kw in ["block", "security check", "dangerous", "hazard", "unsafe"]):
        mission_type = "safety_block"

    # 2. PII Scrubbing
    scrubbed = plan_text
    if config.pii_redaction_enabled:
        email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
        phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
        ssn_pattern = r'\b\d{3}-\d{2}-\d{4}\b'
        card_pattern = r'\b(?:\d[ -]*?){13,16}\b'
        
        if re.search(email_pattern, scrubbed):
            detected_flags.append("PII_EMAIL_FOUND")
            scrubbed = re.sub(email_pattern, '[REDACTED_EMAIL]', scrubbed)
        if re.search(phone_pattern, scrubbed):
            detected_flags.append("PII_PHONE_FOUND")
            scrubbed = re.sub(phone_pattern, '[REDACTED_PHONE]', scrubbed)
        if re.search(ssn_pattern, scrubbed):
            detected_flags.append("PII_SSN_FOUND")
            scrubbed = re.sub(ssn_pattern, '[REDACTED_SSN]', scrubbed)
        if re.search(card_pattern, scrubbed):
            detected_flags.append("PII_CREDIT_CARD_FOUND")
            scrubbed = re.sub(card_pattern, '[REDACTED_CARD]', scrubbed)

    # 3. Prompt Injection Detection
    injection_phrases = [
        "ignore previous instructions",
        "reveal system prompt",
        "reveal developer message",
        "bypass safety",
        "disable policy",
        "show secrets",
        "leak api key",
        "override tool allowlist",
        "execute shell command"
    ]
    injection_detected = False
    for phrase in injection_phrases:
        if phrase in plan_lower:
            injection_detected = True
            detected_flags.append(f"PROMPT_INJECTION_DETECTED: {phrase}")
            blocked_reason = f"Plan contains unauthorized prompt injection command: {phrase}"
            break

    # 4. Unsafe Guidance Blocking
    unsafe_phrases = [
        "drive through flooded roads",
        "bypass barricades",
        "ignore official alerts",
        "reveal secrets or prompts"
    ]
    unsafe_detected = False
    for phrase in unsafe_phrases:
        if phrase in plan_lower:
            unsafe_detected = True
            detected_flags.append(f"UNSAFE_GUIDANCE_DETECTED: {phrase}")
            blocked_reason = f"Plan violates safety guidance rule: {phrase}"
            break

    # Determine status & severity
    is_blocked = injection_detected or unsafe_detected
    if is_blocked:
        safety_status = "FAILED"
        severity = "CRITICAL"
    elif len(detected_flags) > 0:
        severity = "WARNING"

    # Define tool authorization list
    if mission_type == "destination_readiness":
        authorized_tools = ["atlas_weather_context", "atlas_aqi_context", "atlas_civic_signal", "atlas_safety_rules"]
    elif mission_type == "food_place":
        authorized_tools = ["atlas_weather_context", "atlas_aqi_context", "atlas_civic_signal", "atlas_places_search", "atlas_safety_rules"]
    else: # safety_block
        authorized_tools = ["atlas_safety_rules"]

    # Structured JSON audit logging
    audit_entry = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "severity": severity,
        "event_type": "security_checkpoint_evaluation",
        "mission_type": mission_type,
        "detected_flags": detected_flags,
        "safety_status": safety_status,
        "blocked_reason": blocked_reason
    }
    print(f"AUDIT LOG: {json.dumps(audit_entry)}")

    # Save state variables for Decision Scoring Agent
    ctx.state["mission_type"] = mission_type
    ctx.state["security_trace"] = detected_flags
    ctx.state["safety_validation"] = safety_status
    ctx.state["authorized_tools"] = authorized_tools
    ctx.state["fallback_used"] = True

    if is_blocked:
        return Event(
            output={"error": blocked_reason},
            route="SECURITY_EVENT"
        )

    return Event(
        output=UserPlanInput(plan=scrubbed),
        route="CLEAN"
    )


@node
def final_formatting(ctx: Context, node_input: dict) -> ATLASDecisionOutput:
    security_trace = ctx.state.get("security_trace", [])
    
    if isinstance(node_input, dict) and "error" in node_input:
        return ATLASDecisionOutput(
            decision_score=0,
            decision_label="Blocked for unsafe request",
            decision_reason=node_input["error"],
            confidence="High",
            score_breakdown=[
                ScoreBreakdown(
                    category="Security Check",
                    score=0,
                    max_score=10,
                    reason="Input plan failed safety policies (violates security guidelines)."
                )
            ],
            recommendations=["Revise the plan input to exclude dangerous/malicious keywords."],
            agent_trace=["safety_policy_agent"],
            tool_trace=[],
            security_trace=security_trace + ["PLAN_BLOCKED_BY_SECURITY"],
            safety_validation="FAILED",
            fallback_used=True
        )
        
    if isinstance(node_input, ATLASDecisionOutput):
        return node_input
        
    if isinstance(node_input, dict):
        return ATLASDecisionOutput(**node_input)
        
    return ATLASDecisionOutput(
        decision_score=50,
        decision_label="Risky / Consider Alternatives",
        decision_reason="Safety score could not be determined.",
        confidence="Low",
        score_breakdown=[],
        recommendations=[],
        agent_trace=["safety_policy_agent"],
        tool_trace=[],
        security_trace=security_trace,
        safety_validation="FAILED",
        fallback_used=True
    )


# ═══════════════════════════════════════════════════════════════════════════════
# GRAPH & APP INITIALIZATION
# ═══════════════════════════════════════════════════════════════════════════════

edges = [
    (START, safety_policy_agent),
    (safety_policy_agent, {"SECURITY_EVENT": final_formatting, "CLEAN": commander_agent}),
    (commander_agent, decision_scoring_agent),
    (decision_scoring_agent, final_formatting),
]


root_agent = Workflow(
    name="atlas_workflow",
    edges=edges,
    output_schema=ATLASDecisionOutput,
)

app = App(
    root_agent=root_agent,
    name="app",
    resumability_config=ResumabilityConfig(enabled=True)
)
