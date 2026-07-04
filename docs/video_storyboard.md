# ATLAS Video Storyboard

This document storyboard outlines the visual transitions and slide sequences for the ATLAS presentation video (Target: 5 minutes).

---

## Scene 1: Introduction (0:00–0:45)
* **Visual:** Premium technical cover page banner (`cover_page_banner_tech.png`).
* **Transition:** Cut to IDE showing `README.md` (specifically Section 1: Problem Statement).
* **Key Voiceover Focus:** The hook. Explain the difference between reactive search and proactive life-safety scanning.

---

## Scene 2: The Core Rationale (0:45–1:10)
* **Visual:** Streamlit UI landing page showing the input forms.
* **Transition:** Smooth scroll through the UI elements (demos and forms).
* **Key Voiceover Focus:** How natural language plans are processed into scores without needing explicit safety prompts.

---

## Scene 3: Under the Hood (1:10–1:45)
* **Visual:** Visual rendering of High-Level and Low-Level architecture diagrams in `README.md`.
* **Transition:** Split screen or scroll showing `app/agent.py` code structure and routing dictionary definition.
* **Key Voiceover Focus:** Multi-agent design (Commander, domain agents, scoring agent) and ADK 2.0 Workflows.

---

## Scene 4: Live Scanner Demos (1:45–3:50)
* **Visual:** Active Streamlit UI scan executions.
* **Flow:**
  1. *Demo 1 (Destination Readiness):* Click coastal city demo button ➔ show score metric and category breakdown expander.
  2. *Demo 2 (Food & Place):* Click Mediterranean food demo button ➔ show dining cards and open statuses.
  3. *Demo 3 (Security Block):* Click injection demo button ➔ show blocked error message, then switch to terminal window showing JSON audit log output.
* **Key Voiceover Focus:** Step-by-step telemetry, scoring weights, and security checks.

---

## Scene 5: Technical Details & Concepts (3:50–4:45)
* **Visual:** IDE showing `mcp_server.py` stdio tools and running `make test` inside the terminal.
* **Transition:** Scroll showing clean passing test outputs (15/15).
* **Key Voiceover Focus:** Model Context Protocol (MCP) server, local mock data for reproducibility, and test validation.

---

## Scene 6: Future Scope & Wrap-up (4:45–5:00)
* **Visual:** Premium cover page banner (`cover_page_banner_tech.png`).
* **Transition:** Slow fade to black.
* **Key Voiceover Focus:** Value statement, privacy principles, and project closing.
