# ATLAS: Security Gate Specifications

This document outlines the multi-layered security controls implemented at the entry gateway of the ATLAS Life-Safety Decision Agent.

---

## 1. PII Redaction
Regular expressions scan all user input plans for sensitive patterns. Flagged items are replaced with standard placeholders before the plan is forwarded to downstream LLMs:
- **Email Addresses:** Redacted to `[REDACTED_EMAIL]`.
- **Phone Numbers:** Redacted to `[REDACTED_PHONE]`.
- **Social Security Numbers (SSN):** Redacted to `[REDACTED_SSN]`.
- **Credit Cards:** Redacted to `[REDACTED_CREDIT_CARD]`.

---

## 2. Prompt Injection Detection
The input scanner evaluates strings against injection signatures (e.g., *"ignore previous instructions"*, *"reveal developer message"*, *"reveal system prompt"*, *"leak api key"*). If detected, execution halts immediately at the gateway, and the request is routed directly to the final formatter with a blocked label.

---

## 3. Unsafe Guidance Blocking
ATLAS blocks requests seeking instructions on hazardous or illegal tasks (e.g., *"drive through flooded roads"*, *"bypass barricades"*, *"ignore official alerts"*). These checks protect human lives by preventing the agent from generating step-by-step instructions for dangerous actions.

---

## 4. Tool Authorization
To enforce the principle of least privilege, tools are restricted by mission type:
- **Destination Readiness missions** are authorized to access: `atlas_weather_context`, `atlas_aqi_context`, `atlas_civic_signal`, and `atlas_safety_rules`.
- **Food & Place Recommendation missions** are authorized to access: `atlas_weather_context`, `atlas_aqi_context`, `atlas_civic_signal`, `atlas_places_search`, and `atlas_safety_rules`.
- **Safety Block missions** are restricted to calling `atlas_safety_rules` only.

---

## 5. Final Response Audit & Logs
If a request violates safety thresholds:
1. The Safety Policy Agent halts downstream graph execution.
2. The overall decision score is set to `0`, and the label is mapped to `"Blocked for unsafe request"`.
3. A structured JSON audit event containing severity (`CRITICAL`), flags, status (`BLOCKED`), and reasons is output to stdout.

---

## 6. Security Trace
Any security flags raised or PII redaction actions triggered are appended to the `security_trace` list, which is exposed to the user in the final output and the Streamlit Mission Control traces panel.
