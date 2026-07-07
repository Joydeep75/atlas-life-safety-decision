# ATLAS: Final Video Recording Plan

This plan guides you through the process of recording the 5-minute presentation video for your Kaggle ATLAS submission.

---

## 1. Setup & Environment
- **Browser:** Open two tabs:
  - Tab 1: Streamlit Mission Control Dashboard (`http://localhost:8501`)
  - Tab 2: ADK Web Playground (`http://localhost:18081`) showing the graph DAG.
- **IDE (VS Code):** Open the project workspace. Keep the following files open in separate editor tabs:
  - `app/agent.py` (focusing on the graph nodes and the `safety_policy_agent` logic)
  - `app/mcp_server.py` (showing the registered stdio tool functions)
- **Terminal:** Open a terminal window positioned at the bottom of the screen.

---

## 2. Timing & Shot Roadmap (Under 5 Minutes)

### 0:00–0:20 | Scene 1: Introduction & Title
- **Visual:** Display `assets/cover_page_banner.png` in full-screen mode.
- **Action:** Introduce ATLAS, its mission focus on health/safety for the *Agents for Good* track, and outline the goal of proactive safety scans.

### 0:20–0:45 | Scene 2: Problem Statement & Why Agents
- **Visual:** Open `README.md` and scroll through Section 1: Problem Statement.
- **Action:** Explain the danger of reactive safety checks and why a multi-agent system is necessary for domain routing, scoring, and security checkpoints.

### 0:45–1:10 | Scene 3: Platform Architecture
- **Visual:** Open the ADK Web Playground tab showing the 5-agent DAG. Briefly cycle to `app/agent.py` to highlight `safety_policy_agent` and how sub-agents are structured.
- **Action:** Walk through the workflow path: Security Gateway -> Commander -> Sub-Agents (Destination/Food) -> Decision Scoring -> Final Formatting.

### 1:10–1:45 | Scene 4: MCP Tools & Scoring Configuration
- **Visual:** Switch to `app/mcp_server.py` and scroll through the `@mcp.tool()` definitions.
- **Action:** Discuss how sub-agents access local environmental telemetry (Weather, AQI, Civic events) via MCP stdio tools, and how the scoring engine weights these alerts.

### 1:45–2:30 | Demo 1: Destination Readiness
- **Visual:** Switch to Streamlit dashboard. Click **Destination Demo** -> Click **Shield Scan Plan**. Expand the **Score Breakdown** tab to show the metrics (Weather, AQI, Civic) and the natural language component reasons.
- **Action:** Demonstrate a travel safety check for Coastal City, explaining the caution score breakdown (75/100) due to moderate wind alert logs.

### 2:30–3:15 | Demo 2: Food & Place
- **Visual:** Click **Food & Place Demo** -> Click **Shield Scan Plan**. Show the rendered dining recommendations and the active comfort score breakdown.
- **Action:** Walk through the dining validation flow for Sample City Center with adult family members, returning safe restaurant certifications.

### 3:15–3:50 | Demo 3: Security Checkpoint Block
- **Visual:** Click **Block Check Demo** -> Click **Shield Scan Plan**. Point to the red **Blocked for unsafe request** alert card. Switch to the terminal window showing the uvicorn stdout feed to point out the printed JSON audit log.
- **Action:** Explain how the Safety Policy Agent gateway filters prompt injections and dangerous action paths at the entrance, returning a score of 0.

### 3:50–4:25 | Course Concepts & Verification
- **Visual:** Run `make test` inside the terminal window to show the 15 passing tests.
- **Action:** Highlight key course concepts applied: ADK workflows, stdio MCP, gateway safety check, and local mock data reproducibility.

### 4:25–4:45 | Local Setup & Reproducibility
- **Visual:** Scroll through the setup sections in the README showing git instructions, `.gitignore`, and the optional deployment guide.
- **Action:** State that the app runs completely locally from GitHub with zero cloud dependencies, making it 100% reproducible for judges.

### 4:45–5:00 | Future Roadmap & Closing
- **Visual:** Display `assets/cover_page_banner.png` in full-screen mode.
- **Action:** Highlight future scope items (personalized consent-based commute routes, mobile/iPad clients, and live APIs) and close the presentation.
