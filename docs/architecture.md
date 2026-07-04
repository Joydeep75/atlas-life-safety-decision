# ATLAS: System Architecture Specifications

This document outlines the architectural components and multi-agent coordination within the ATLAS Life-Safety Decision Agent.

---

## Multi-Agent Hierarchy
ATLAS coordinates domain validation using five specialized agent nodes structured in a Directed Acyclic Graph (DAG) using the ADK 2.0 Workflows API:

1. **Safety Policy Agent (Gateway Node):** Serves as a secure firewall, inspecting, redacting, and logging all inputs *before* downstream agents execute.
2. **Commander Agent (Coordinator Node):** Processes validated inputs, infers intent, and routes calls using ADK `AgentTool` delegation.
3. **Destination Readiness Agent (Domain Node):** Processes travel destination plans and queries localized weather, AQI, and civic safety server tools.
4. **Food & Place Agent (Domain Node):** Evaluates dining plans, querying restaurant hygiene database registries via MCP search tools.
5. **Decision Scoring Agent (Synthesis Node):** Integrates sub-agent reports, weights scoring categories, and determines final labels.

---

## State Sharing (`ctx.state`)
The agents communicate telemetry and security events asynchronously via the shared ADK `Context` object (`ctx.state` dictionary). Downstream nodes read this state to compute scores and trace safety flags.

---

## Formatter Node
The final node (`final_formatting`) enforces output structure, validating that all responses strictly conform to the `ATLASDecisionOutput` Pydantic schema before returning JSON payload.
