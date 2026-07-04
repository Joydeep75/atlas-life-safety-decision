# ATLAS: Future Scope & Roadmap

This document outlines the architectural roadmap and expansion plans for the ATLAS Life-Safety Decision Agent.

---

## 1. Live Municipal API Integration
The current MVP utilizes a Model Context Protocol (MCP) server loaded with mock databases. In production, we plan to connect the server tools to live public safety registries:
- **Weather:** NOAA Weather Alert API.
- **Air Quality:** EPA AirNow API.
- **Civic Signals:** Local city transit registries, municipal flood indicators, and state police road blocks.
- **Dining Hygiene:** County Health Department health inspection databases.

---

## 2. Privacy-First Local Execution
To enhance privacy (especially when processing sensitive daily plans, location histories, and health constraints), future versions will support routing queries to local offline models (e.g. Gemma 2B or Llama 3 8B) running entirely on the user's local device.

---

## 3. Secure Persistent Storage
The MVP uses session-only storage (`st.session_state`) for favorites and history to protect data privacy. Future expansions will include:
- **Encrypted Local Database:** Encrypting saved items using user-controlled master keys.
- **Zero-Knowledge Cloud Sync:** Enabling cross-device favorites utilizing secure, end-to-end encrypted storage protocols.
