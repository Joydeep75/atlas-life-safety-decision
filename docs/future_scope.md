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

---

## 4. Expanded Decision Frameworks
Extend the agent's domain scope to cover broader life-safety categories (e.g., active structural fire risks, extreme thermal alerts, and municipal chemical hazards) by adding specialized sub-agents integrated with live municipal API registries. This will support day-to-day consumer tasks such as:
- **Personalized Commute Planning:** Automatically analyzing daily travel routes (e.g., home-to-office, local grocery stores, school drop-offs) for localized road hazards, toxic spill alerts, or transit delays. Safety scores will adapt dynamically to the user's travel patterns based on their saved searches and explicitly granted consent.
- **Event & Activity Validation:** Scanning local safety mandates and environmental hazards for outdoor runs, sports events, or community festivals.

---

## 5. Cross-Platform Client Ecosystem
Expand the B2C delivery model by engineering dedicated mobile (iOS/Android), iPad, and smart wearable applications to bring real-time, context-aware safety assessments directly to users on the move.
