# ATLAS: Decision Scoring Engine Specifications

This document outlines the scoring algorithms and explainability patterns of the ATLAS Life-Safety Decision Agent.

---

## 1. Overall Score
The overall safety rating (0–100) represents a weighted calculation of environmental, civic, and operational safety metrics. Scoring is performed dynamically by the Decision Scoring Agent, integrating sub-agent reports.

---

## 2. Category Scoring Weights
The scoring breakdown categories and their maximum weights are structured as follows:

### Mission: Destination Readiness
- **Weather Safety (25):** Evaluates storm, wind, temperature, and sea alerts.
- **Air Quality - AQI (20):** Evaluates active dust, ozone, PM2.5, or pollution alerts.
- **Civic Signals (20):** Evaluates municipal active closures, flooding events, or structural blocks.
- **Destination Readiness (15):** Evaluates site hours, booking alerts, or local warnings.
- **User Specific Context (10):** Assesses suitability against user constraints (elderly, kids, allergies).
- **Safety Policy Validation (10):** Assesses alignment with safety guidelines.

### Mission: Food & Place Recommendation
- **Eatery Quality / Hygiene (30):** Assesses department ratings and warnings.
- **Open/Distance Convenience (15):** Evaluates transit distance and active hours.
- **Weather Comfort (15):** Evaluates outdoor seating conditions and warnings.
- **Air Quality Comfort (15):** Evaluates indoor/outdoor air levels.
- **Civic/Transit Stability (10):** Evaluates surrounding road closures and transit alerts.
- **User Specific Context (5):** Assesses dining needs (dietary, accessibility).
- **Safety Policy Validation (10):** Assesses compliance.

---

## 3. Score Labels
The overall score maps to a clear safety category:
- **90–100:** Excellent Idea
- **75–89:** Good Idea
- **60–74:** Okay with Caution
- **40–59:** Risky / Consider Alternatives
- **0–39:** Not Recommended
- **Blocked:** Blocked for unsafe request (Score = 0)

---

## 4. One-Line Reasons & Explainability
To guarantee explainability, every final response must include:
- A single-sentence **`decision_reason`** summarizing the overall scan status.
- A specific one-line **`reason`** for every individual category component in the breakdown.

---

## 5. Confidence Scores
ATLAS outputs a confidence assessment (`High`, `Medium`, or `Medium-Low`). Because local evaluations rely on fallback/mock databases to guarantee reproducibility, the default confidence is set to `Medium` or `Medium-Low` to transparently indicate that real-time live APIs were not called.
