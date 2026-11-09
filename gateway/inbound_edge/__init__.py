# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Inbound MCP Edge — the one governed boundary hosted personal AI agents may cross.

Hosted agents (Claude Duet, Poke, Gemini Spark, OpenAI Dots) run in vendor clouds,
so AgentShroud cannot sit in their model or egress path. This package fronts them
with a single MCP endpoint instead. The internet-facing container
(``edge_app``) only terminates the protocol; every policy decision and all state
live in the gateway (``routes`` → ``call_pipeline``), which reuses the existing
P0–P6 modules on ``app_state``. See docs/inbound-mcp-edge/.
"""
