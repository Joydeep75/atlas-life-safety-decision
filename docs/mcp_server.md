# ATLAS: Model Context Protocol (MCP) Server Specifications

This document outlines the design and operation of the Model Context Protocol (MCP) server integrated into the ATLAS Life-Safety Decision Agent.

---

## 1. Purpose of the MCP Server
Large Language Models (LLMs) lack real-time local safety telemetry and municipal alerts. The ATLAS MCP Server acts as a standardized bridge, allowing the agents to query localized environmental databases and regulations dynamically.

---

## 2. Exposed Tools
The MCP server (implemented using `FastMCP` in `app/mcp_server.py`) exposes five stdio-based tools:

1. **`atlas_weather_context`:** Returns current conditions, high-wind/storm warnings, risk levels, and fallback status.
2. **`atlas_aqi_context`:** Returns Air Quality Index values, safety categories, health alerts, and recommendations.
3. **`atlas_civic_signal`:** Returns infrastructure events (e.g., active flooding, road blocks, transit closures).
4. **`atlas_places_search`:** Returns local eateries matched against municipal hygiene registers.
5. **`atlas_safety_rules`:** Returns active municipal safety regulations and advisory guidelines.

---

## 3. Fallback and Mock Data
To ensure 100% reproducibility and prevent brittle dependencies on live public APIs, the MCP server serves deterministic mock data for neutral demo locations (`Coastal City`, `Sample City Center`, `Sample Downtown`, `Sample Destination`). If a query falls outside these locations, it returns default safe parameters, flagged with `fallback_used = True`.

---

## 4. How Agents Use Tools
Sub-agents (Destination Readiness Agent and Food & Place Agent) are wired to the MCP server. During graph execution, the sub-agents construct tool calls based on the location extracted from the user's plan. They parse the tool's JSON outputs and store the parameters in `ctx.state`, allowing the Decision Scoring Agent to parse the telemetry and calculate weighted scores.
