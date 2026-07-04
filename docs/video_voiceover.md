# ATLAS Video Voiceover Narration Script

This document contains the raw spoken voiceover text divided by timestamps.

---

### [0:00–0:20] Hook
> "Welcome, judges. This is ATLAS: the Life-Safety Decision Agent. Built for the 'Agents for Good' track, ATLAS helps people make safer everyday choices by converting natural language travel and dining plans into proactive safety scans. It automatically highlights risks without requiring you to look them up yourself."

---

### [0:20–0:45] Problem
> "Every day, environmental and safety hazards are published across fragmented local government dashboards. Travelers often visit wind-warned coasts or eat at hygiene-flagged diners simply because they didn't think to check. ATLAS removes this cognitive burden by shifting safety from reactive searching to proactive, automatic agentic reasoning."

---

### [0:45–1:10] ATLAS Solution
> "Users input plans naturally—like traveling to a coastal city or looking for dinner. ATLAS infers the implicit safety intent, triggers specialized sub-agents, queries local context safety databases via the Model Context Protocol, and returns an explainable safety score."

---

### [1:10–1:45] Architecture
> "Under the hood, ATLAS implements an ADK 2.0 Workflow graph. First, a Safety Policy Agent validates inputs. If clear, the Commander Agent routes the plan to the correct sub-agent, which calls Model Context Protocol server tools. Finally, a Decision Scoring Agent weights the alerts to generate a unified score."

---

### [1:45–2:30] Demo 1: Destination Readiness
> "Let's run a destination plan. We click 'Destination readiness Demo' for a coastal city with family context. ATLAS calls the weather, AQI, and safety rules tools. We get a score of 75, labeled 'Good Idea' with caution recommendations. In the breakdown, we see a slight reduction due to forecast wind levels."

---

### [2:30–3:15] Demo 2: Food & Place
> "Now, let's look at dining safety. We click 'Food & Place Recommendation Demo.' ATLAS queries the places search MCP tool, checking local departments for hygiene registry files. It suggests certified options like 'Sample Eatery Center' and scores the plan's safety comfort at 92 out of 100."

---

### [3:15–3:50] Demo 3: Security Block
> "Security is a core requirement. If a user inputs a prompt injection or asks how to drive on flooded roads, the Safety Policy Agent blocks it instantly. Downstream routing is cut off, returning a score of 0. A structured security audit event is logged to stdout with critical severity."

---

### [3:50–4:25] Course Concepts
> "ATLAS is a practical application of course concepts: using ADK workflows for multi-agent routing, FastMCP for stdio tools isolation, PII redacting gateway checkpoints, and a full unit test suite ensuring robust, deterministic local execution."

---

### [4:25–4:45] Deployability & Reproducibility
> "ATLAS is highly reproducible. With local mock data fallbacks, judges can run the entire test suite, playground, or Streamlit UI offline in seconds using the provided Makefile. A Dockerfile is also included for easy Cloud Run deployment."

---

### [4:45–5:00] Future Scope & Close
> "For future scope, we will connect ATLAS to live NOAA APIs and deploy local offline models to maximize data privacy. ATLAS is a clear showcase of how intelligent, secured agents can work for social good. Thank you."
