---
type: community
cohesion: 0.10
members: 23
---

# Module Group 205

**Cohesion:** 0.10 - loosely connected
**Members:** 23 nodes

## Members
- [[._emit_privacy_event()]] - code - gateway/proxy/mcp_proxy.py
- [[._execute_tool_call()]] - code - gateway/proxy/mcp_proxy.py
- [[._extract_egress_targets()]] - code - gateway/proxy/mcp_proxy.py
- [[._sanitize_admin_private_data()]] - code - gateway/proxy/mcp_proxy.py
- [[.check_approval_required()]] - code - gateway/proxy/mcp_proxy.py
- [[.get_stats()_5]] - code - gateway/proxy/mcp_proxy.py
- [[.process_tool_call()]] - code - gateway/proxy/mcp_proxy.py
- [[.process_tool_result()_1]] - code - gateway/proxy/mcp_proxy.py
- [[.send_request()_1]] - code - gateway/proxy/mcp_proxy.py
- [[.send_request()]] - code - gateway/proxy/mcp_proxy.py
- [[.start()_1]] - code - gateway/proxy/mcp_proxy.py
- [[Actually execute the tool call against the MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Any_15]] - code - gateway/proxy/mcp_proxy.py
- [[Best-effort privacy event emission.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Check if a tool call requires approval and wait for it if needed.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Extract outbound URL-like targets from nested MCP tool parameters.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Get proxy statistics.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Process a tool result coming back (for cases where execution happens externally)]] - rationale - gateway/proxy/mcp_proxy.py
- [[Process an MCP tool call through the security pipeline.          Args]] - rationale - gateway/proxy/mcp_proxy.py
- [[Redact admin-private data from tool results for non-owner agents.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Send a JSON-RPC request and read the response.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Send an HTTP request to the MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Start the MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_205
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Module Group 78]]
- 8 edges to [[_COMMUNITY_MCP Config & Proxy]]
- 2 edges to [[_COMMUNITY_Module Group 266]]
- 2 edges to [[_COMMUNITY_MCP Inspector & Audit]]
- 1 edge to [[_COMMUNITY_Dashboard Routes & WebSocket]]
- 1 edge to [[_COMMUNITY_Module Group 139]]
- 1 edge to [[_COMMUNITY_MCP Permissions Manager]]

## Top bridge nodes
- [[Any_15]] - degree 12, connects to 3 communities
- [[._execute_tool_call()]] - degree 8, connects to 3 communities
- [[.process_tool_result()_1]] - degree 6, connects to 3 communities
- [[.process_tool_call()]] - degree 9, connects to 2 communities
- [[._emit_privacy_event()]] - degree 5, connects to 2 communities