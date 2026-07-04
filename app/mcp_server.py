# ruff: noqa
import json
from mcp.server.fastmcp import FastMCP

# Define the FastMCP server
mcp = FastMCP("ATLAS-Safety-MCP")

@mcp.tool()
def atlas_weather_context(location: str) -> str:
    """Gets safety-relevant weather context for a location.
    
    Args:
        location: Neutral place name (e.g. 'Coastal City', 'Sample Destination').
        
    Returns:
        JSON string with condition, risk_level, summary, source, and fallback_used.
    """
    loc = location.lower()
    if "coastal" in loc:
        res = {
            "condition": "High Wind Warning & Rough Surf",
            "risk_level": "Warning",
            "summary": "Coastal warnings active. High wind gusts and elevated surf conditions. Expect minor coastal road closures.",
            "source": "Mock National Meteorological Center",
            "fallback_used": True
        }
    else:
        res = {
            "condition": "Clear & Sunny",
            "risk_level": "Safe",
            "summary": "Weather conditions are optimal. No active weather alerts.",
            "source": "Mock National Meteorological Center",
            "fallback_used": True
        }
    return json.dumps(res)

@mcp.tool()
def atlas_aqi_context(location: str) -> str:
    """Gets safety-relevant Air Quality Index (AQI) context for a location.
    
    Args:
        location: Neutral place name (e.g. 'Sample Downtown', 'Sample City Center').
        
    Returns:
        JSON string with AQI value/category, risk_level, summary, source, and fallback_used.
    """
    loc = location.lower()
    if "coastal" in loc:
        res = {
            "aqi_value": 45,
            "category": "Good",
            "risk_level": "Safe",
            "summary": "Fresh sea breezes keeping air clear. Safe for outdoor activities.",
            "source": "Mock Environmental Watch",
            "fallback_used": True
        }
    else:
        res = {
            "aqi_value": 110,
            "category": "Moderate / Unhealthy for Sensitive Groups",
            "risk_level": "Caution",
            "summary": "Elevated ozone levels near city center. Sensitive groups should limit outdoor exertion.",
            "source": "Mock Environmental Watch",
            "fallback_used": True
        }
    return json.dumps(res)

@mcp.tool()
def atlas_civic_signal(location: str) -> str:
    """Gets active civic or disruption signals (floods, closures, demonstrations, roadworks).
    
    Args:
        location: Neutral place name.
        
    Returns:
        JSON string containing disruption/flood/civic signal summary.
    """
    loc = location.lower()
    if "coastal" in loc:
        res = {
            "disruption_summary": "Minor flooding reported on Coastal Highway near harbor. Detours are active.",
            "signal_status": "Active Warning",
            "fallback_used": True
        }
    else:
        res = {
            "disruption_summary": "No active emergency or civic disruptions reported for this location.",
            "signal_status": "Normal",
            "fallback_used": True
        }
    return json.dumps(res)

@mcp.tool()
def atlas_places_search(location: str, query: str = "food") -> str:
    """Searches for places or food options.
    
    Args:
        location: Neutral place name.
        query: Type of venue to search for.
        
    Returns:
        JSON string with 3 demo food/place options with rating, open_now status, and safety reasons.
    """
    options = [
        {
            "name": "Sample Eatery Center",
            "rating": 4.5,
            "open_now": True,
            "reason": "Highly rated, verified health inspection status passed.",
        },
        {
            "name": "Downtown Safe Grill",
            "rating": 4.2,
            "open_now": True,
            "reason": "Popular, sanitization audits updated weekly.",
        },
        {
            "name": "Coastal Quick Bites",
            "rating": 3.9,
            "open_now": False,
            "reason": "Temporarily closed due to high tide warning.",
        }
    ]
    return json.dumps({"options": options, "fallback_used": True})

@mcp.tool()
def atlas_safety_rules(location: str) -> str:
    """Retrieves safety rules (blocked/caution rules) for a location.
    
    Args:
        location: Neutral place name.
        
    Returns:
        JSON string containing safety blocked and caution rules.
    """
    loc = location.lower()
    if "coastal" in loc:
        res = {
            "blocked_rules": ["Do not enter beaches under high surf warning.", "Avoid night driving on unlit coastal bypasses."],
            "caution_rules": ["Expect high winds on bridges.", "Monitor local high-tide timetables."],
            "fallback_used": True
        }
    else:
        res = {
            "blocked_rules": ["Do not cross active railway crossings when barriers are down."],
            "caution_rules": ["Watch for heavy pedestrian traffic near the central transit plaza."],
            "fallback_used": True
        }
    return json.dumps(res)

if __name__ == "__main__":
    mcp.run()
