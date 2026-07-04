# ATLAS: Evaluation & Validation Rig

This document outlines the testing and evaluation workflows designed to validate the ATLAS Life-Safety Decision Agent's safety, intent classification, and routing performance.

---

## 1. Unit Tests
The core test suite is located in [tests/unit/test_atlas.py](file:///Users/joydeepg/Education/Kaggle-Google/15-19-June-2026/Capstone_Project/adk-workspace/atlas-life-safety-decision/tests/unit/test_atlas.py). These tests run locally, offline, and deterministically using `pytest`. They cover:
1. **Intent routing:** Verifying that travel plans route to `destination_readiness` and dining plans route to `food_place`.
2. **PII Scrubbing:** Verifying that email, phone, and SSN formats are redacted.
3. **Prompt Injection & Unsafe Actions Block:** Verifying that system override prompts or flood bypass requests are caught and set to score `0` (Blocked).
4. **Scoring Label Boundaries:** Checking that scores map correctly to safety labels.

---

## 2. Integration and E2E Tests
Located in `tests/integration/`, these tests launch the local FastAPI server in a subprocess to verify the API adapters:
- **`test_agent.py`:** Validates local runner execution and message streaming.
- **`test_server_e2e.py`:** Validates feedback collection (`/feedback`), agent cards, A2A endpoints, and `/api/stream_reasoning_engine` (skipped in dummy environments).

---

## 3. ADK Evaluation Dataset
The evaluation datasets are located under `tests/eval/datasets/`. They allow developers to measure classification precision and scoring accuracy across hundreds of test prompts using the command:
```bash
agents-cli eval run
```
The configurations are defined in [tests/eval/eval_config.yaml](file:///Users/joydeepg/Education/Kaggle-Google/15-19-June-2026/Capstone_Project/adk-workspace/atlas-life-safety-decision/tests/eval/eval_config.yaml) and [tests/eval/metrics.py](file:///Users/joydeepg/Education/Kaggle-Google/15-19-June-2026/Capstone_Project/adk-workspace/atlas-life-safety-decision/tests/eval/metrics.py).
