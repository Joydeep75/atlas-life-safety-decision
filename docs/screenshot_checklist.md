# ATLAS Screenshot Capture Checklist

Use this checklist to capture and save all required visual screenshots of the ATLAS Life-Safety Decision Agent. Save the captures into the `assets/screenshots/` directory.

---

## Required Screenshots

- [ ] **1. README Top Section**
  - *Details:* Capture the title, cover banner, track details, and problem statement section in a clean browser or markdown reader.

- [ ] **2. High-Level and Low-Level Architecture Diagrams**
  - *Details:* Capture the rendered Mermaid diagrams (both high-level pipeline flow and low-level file structure) inside the README or slide package.

- [ ] **3. ADK Playground Running**
  - *Details:* Capture the ADK Web Playground (`http://localhost:18081`) showing the compiled multi-agent DAG graph.

- [ ] **4. Streamlit Home Screen (Empty State)**
  - *Details:* Capture the Streamlit dashboard (`http://localhost:8501`) on load showing the greeting box and form prompts before execution.

- [ ] **5. Destination Readiness Result**
  - *Details:* Capture the full Streamlit UI after running the Coastal City demo, displaying the caution score, rating label, and recommendation bullet points.

- [ ] **6. Food & Place Result**
  - *Details:* Capture the Streamlit UI after running the Mediterranean food demo, displaying the Excellent Idea score and recommended eatery cards.

- [ ] **7. Security Block Result**
  - *Details:* Capture the Streamlit UI after submitting the flood bypass injection, displaying the red Blocked verdict badge and security warning banner.

- [ ] **8. Decision Score Explanation**
  - *Details:* Capture the overall `decision_reason` paragraph displayed under the score cards.

- [ ] **9. Score Breakdown Explanation**
  - *Details:* Capture the expanded **Category Score Breakdown** panel showing individual metrics (Weather, AQI, Civic) and their respective sub-reasons.

- [ ] **10. Security Trace**
  - *Details:* Capture the expanded **View Agent Execution Traces** panel focusing on the **Security Audit Log Highlights** where scrubbed/blocked event notes are logged.

- [ ] **11. History/Favorites Sidebar**
  - *Details:* Capture the Deep Navy sidebar showing populated History navigation buttons and the saved Favorites panel.
