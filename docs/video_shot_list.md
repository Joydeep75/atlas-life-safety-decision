# ATLAS Video Shot List

This document lists the exact sequence of screen actions and code files to record during the video presentation.

---

## Shot 1: The Presentation Title (0:00–0:20)
* **Action:** Open `assets/cover_page_banner_tech.png` in image viewer or full screen.

## Shot 2: Problem Statement (0:20–0:45)
* **Action:** Open `README.md` in VS Code or web browser, highlight Section 1: Problem Statement, and scroll slowly.

## Shot 3: Streamlit UI Interface (0:45–1:10)
* **Action:** Switch to web browser showing `http://localhost:8501`. Scroll down to display input form and session sidebar.

## Shot 4: Architecture Diagrams (1:10–1:30)
* **Action:** Open `README.md` and scroll to Section 6: Architecture & Visuals. Show the rendered high-level and low-level Mermaid flowcharts.

## Shot 5: Workflow Code (1:30–1:45)
* **Action:** Open `app/agent.py` in VS Code. Hover cursor over the `safety_policy_agent` function and scroll down to the `edges` list at the bottom.

## Shot 6: Demo 1 (Destination Readiness) (1:45–2:30)
* **Action:** In Streamlit, click the **Destination readiness Demo** button. Show the populated form fields. Click **Shield Scan Plan**. Hover cursor over the Score (75/100) and click the **Category Score Breakdown** expander.

## Shot 7: Demo 2 (Food & Place) (2:30–3:15)
* **Action:** In Streamlit, click the **Food & Place Recommendation Demo** button. Click **Shield Scan Plan**. Show the rendered dining recommendations and comfort scores.

## Shot 8: Demo 3 (Security Checkpoint) (3:15–3:40)
* **Action:** In Streamlit, click the **Security Block Demo** button. Click **Shield Scan Plan**. Show the red error alert card: *"Blocked for unsafe request"*.

## Shot 9: Audit Logs (3:40–3:50)
* **Action:** Switch to a terminal window showing the uvicorn stdout feed. Highlight the JSON audit log containing the `BLOCKED` status and severity `CRITICAL`.

## Shot 10: MCP Server Tools (3:50–4:10)
* **Action:** Open `app/mcp_server.py` in VS Code. Show the FastMCP tool registrations like `@mcp.tool()`.

## Shot 11: Unit Tests Run (4:10–4:25)
* **Action:** Open a terminal window, run `make test`, and scroll through the passing pytest logs (15 passed).

## Shot 12: GitHub Configuration (4:25–4:45)
* **Action:** Open `README.md` Section 12: Local Setup showing the Github repository instructions and the `.gitignore` secrets warnings.

## Shot 13: Closing (4:45–5:00)
* **Action:** Display `assets/cover_page_banner_tech.png` in full screen.
