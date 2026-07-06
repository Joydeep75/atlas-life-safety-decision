# ATLAS: Life-Safety Decision Agent — Project State & Polish Checkpoint

## 1. Completed So Far
* **Phase 1 (Scaffold, Auth & Environment):** Scaffolded project using `agents-cli`, set up local `.env` (Gemini API key), configured `.gitignore`.
* **Phase 2 (Multi-Agent Architecture):** Implemented a 5-agent design (Commander, Destination Readiness, Food & Place, Decision Scoring, Safety Policy) via the ADK 2.0 Workflows graph API (no duplicate edges, dictionary-based routing).
* **Phase 3 (MCP Server):** Built FastMCP server exposing 5 tools (`atlas_weather_context`, `atlas_aqi_context`, `atlas_civic_signal`, `atlas_places_search`, `atlas_safety_rules`) with mock safety rules data.
* **Phase 4 (Security):** Implemented gateway regex-based PII scrubber, prompt injection blocker, unsafe plan filter, and JSON audit logging.
* **Phase 5 (Local Dev & Testing):** Written and passed 9 unit tests checking validation, redaction, and intent routing. Checked compatibility.
* **Streamlit Mission Control UI:** Built [streamlit_app.py](file:///Users/joydeepg/Education/Kaggle-Google/15-19-June-2026/Capstone_Project/adk-workspace/atlas-life-safety-decision/streamlit_app.py) with quick interactive demos, history, favorites, and detailed trace logging.
* **Phase 6 (README & Write-Up):** Created [README.md](file:///Users/joydeepg/Education/Kaggle-Google/15-19-June-2026/Capstone_Project/adk-workspace/atlas-life-safety-decision/README.md) and [SUBMISSION_WRITEUP.md](file:///Users/joydeepg/Education/Kaggle-Google/15-19-June-2026/Capstone_Project/adk-workspace/atlas-life-safety-decision/SUBMISSION_WRITEUP.md) containing project architecture, scoring tables, and privacy statements.
* **Phase 7 (Submission Assets):** Generated professional, dark-themed AI agent workflow diagram (`architecture_high_level.png`), low-level codebase architecture diagram (`architecture_low_level.png`), and project cover page banner (`cover_page_banner_professional.png`) inside the `assets/` directory. Preserved original `.mmd` files and legacy `architecture_diagram.png` per instruction. Linked these assets in `README.md`.
* **Phase 8 (Narration Script & Video Package):** Created spoken narration script (`DEMO_SCRIPT.txt`), video storyboard (`docs/video_storyboard.md`), shot list (`docs/video_shot_list.md`), voiceover script (`docs/video_voiceover.md`), and presenter recording checklist (`docs/demo_checklist.md`).
* **Step 23 (Screenshot Plan):** Created [docs/screenshot_checklist.md](file:///Users/joydeepg/Education/Kaggle-Google/15-19-June-2026/Capstone_Project/adk-workspace/atlas-life-safety-decision/docs/screenshot_checklist.md) and appended `## Screenshots` placeholder image blocks inside `README.md`. Created the empty `assets/screenshots/` folder.
* **Step 24 (Demo Scenarios):** Created [tests/eval_scenarios.json](file:///Users/joydeepg/Education/Kaggle-Google/15-19-June-2026/Capstone_Project/adk-workspace/atlas-life-safety-decision/tests/eval_scenarios.json) and [docs/demo_prompts.md](file:///Users/joydeepg/Education/Kaggle-Google/15-19-June-2026/Capstone_Project/adk-workspace/atlas-life-safety-decision/docs/demo_prompts.md) containing final evaluation/demo scenarios covering Destination Readiness, Food & Place, Security Blocks, PII Redaction, and Tool Authorizations.

## 2. Current Working Commands
* **Run Streamlit UI:** `make ui` (starts Streamlit on http://localhost:8501)
* **Run ADK Playground:** `make playground` (starts playground on http://localhost:18081)
* **Run Unit Tests:** `make test` (runs unit tests via pytest)
* **Verify Dependencies:** `make install` (runs uv sync)

## 3. Current Known Issues
* **None:** Unit tests pass (15/15, including E2E and integration tests), and Streamlit UI runs successfully without any model type or session lookup errors.

## 4. Remaining Polish Tasks
* **None:** All agent development, configuration, testing, design assets, submission write-ups, and documentation have been fully completed.

## 5. Files Protected (Do not change unless required)
* `app/agent.py` — Core graph logic and routing.
* `app/mcp_server.py` — Stdio MCP tools definition.
* `tests/unit/test_atlas.py` — Deterministic test suite.
* `streamlit_app.py` — Mission Control UI layout.

## 6. Non-Negotiable ATLAS Requirements
* **Track:** Agents for Good (Health, Safety, and Civic Readiness).
* **ADK multi-agent workflow** must remain.
* **MCP server code** must remain.
* **Security checkpoint** must remain.
* **Neutral demo locations only:** `Coastal City`, `Sample City Center`, `Sample Downtown`, `Sample Destination`.
* **No hardcoded real cities** in code, tests, or documentation.
* **ATLAS Decision Score** must include a one-line `decision_reason`.
* **Score Breakdown components** must include one-line `reason` entries.
* **History/Favorites** must be session-only (Streamlit `st.session_state` only).
* **No database, login, cookies, browser storage, cloud storage, or persistent profiles.**
* **No API keys or secrets** committed to git.
* **Live deployment is optional; GitHub reproducibility is mandatory.**
