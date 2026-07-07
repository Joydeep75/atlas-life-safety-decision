# ATLAS Demo Recording Checklist

Use this checklist during recording to ensure all required assets, files, and actions are shown and correct.

---

## 1. Pre-Recording Checks
- [ ] Set browser zoom to 125% for readability.
- [ ] Open VS Code and close unnecessary tabs.
- [ ] Run `make ui` in a terminal window (ensure port 8501 is open).
- [ ] Run `make playground` in another terminal window (ensure port 18081 is open).
- [ ] Open uvicorn stdout logs in a terminal window.

---

## 2. Shot List Checklist
- [ ] **Banner:** Show `cover_page_banner.png` for intro.
- [ ] **Problem:** Scroll through Section 1: Problem Statement in `README.md`.
- [ ] **Architecture:** Scroll through rendered High-Level and Low-Level diagrams in `README.md`.
- [ ] **Agent Logic:** Open `app/agent.py` and show `safety_policy_agent` function.
- [ ] **MCP Server:** Open `app/mcp_server.py` and show FastMCP tool definitions.
- [ ] **Demo 1 (Destination):** Execute Coastal City demo in Streamlit ➔ show score (75/100) and breakdown reasons.
- [ ] **Demo 2 (Food):** Execute Mediterranean food demo in Streamlit ➔ show eatery suggestion cards.
- [ ] **Demo 3 (Security):** Execute Security Block demo in Streamlit ➔ show blocked message.
- [ ] **Audit logs:** Show JSON logging output in terminal.
- [ ] **Tests:** Run `make test` in terminal ➔ show passing pytest results (15 passed).
- [ ] **Github Setup:** Scroll through Section 12: Local Setup in `README.md`.

---

## 3. Post-Recording Quality Checks
- [ ] Video is under 5 minutes.
- [ ] Text in code and web interface is readable.
- [ ] Spoken voiceover is synchronized with screen actions.
- [ ] No real-world demo cities were mentioned.
