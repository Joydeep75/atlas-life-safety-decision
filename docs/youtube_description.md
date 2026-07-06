# ATLAS YouTube Video Description

Copy and paste this structured text into the description field of your YouTube video upload.

---

## Video Description

ATLAS is a proactive Life-Safety Decision Agent developed for the Kaggle Google AI Hackathon ("Agents for Good" track). 

By leveraging a secure, multi-agent architecture built on the Google Antigravity and ADK 2.0 Workflows framework, ATLAS translates natural language plan descriptions (e.g. travel schedules or dining activities) into instant, context-aware safety scans. The agent routes queries to a local Model Context Protocol (MCP) server exposing local weather, AQI, civic events, and dining hygiene registry databases, producing a unified and fully explainable ATLAS Decision Score.

Learn more and reproduce the project locally:
GitHub Repository: https://github.com/Joydeep75/atlas-life-safety-decision

### Key Features
- **Gateway Security Checkpoint:** Redacts PII, blocks prompt injections, filters unsafe directives, and logs critical audit data.
- **Dynamic Intent Routing:** Automatically matches plan details to specialized Destination and Dining sub-agents.
- **Stdio MCP Server integration:** Isolates local safety telemetry context using FastMCP tools.
- **Glanceable B2C Dashboard:** Light neumorphic user interface with semantic traffic light scores.
- **100% Offline Reproducibility:** Uses local mock/fallback databases by default to ensure judging verification runs out-of-the-box.

### Technologies Used
- Google Antigravity SDK & ADK 2.0 Workflows
- Python 3.11 / FastAPI / Streamlit
- Model Context Protocol (MCP)
- Pytest (15 passed unit, integration, and E2E tests)

#GoogleAIHackathon #Kaggle #AgentsForGood #AI #MultiAgent #ModelContextProtocol
