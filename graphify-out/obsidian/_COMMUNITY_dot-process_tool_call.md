---
type: community
cohesion: 0.13
members: 16
---

# .process_tool_call

**Cohesion:** 0.13 - loosely connected
**Members:** 16 nodes

## Members
- [[dot-_emit_privacy_event()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_execute_tool_call()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_extract_egress_targets()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_sanitize_admin_private_data()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-check_approval_required()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-process_tool_call()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-process_tool_result()_1]] - code - gateway/proxy/mcp_proxy.py
- [[dot-send_request()_1]] - code - gateway/proxy/mcp_proxy.py
- [[Actually execute the tool call against the MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Best-effort privacy event emission.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Check if a tool call requires approval and wait for it if needed.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Extract outbound URL-like targets from nested MCP tool parameters.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Process a tool result coming back (for cases where execution happens externally)]] - rationale - gateway/proxy/mcp_proxy.py
- [[Process an MCP tool call through the security pipeline.          Args]] - rationale - gateway/proxy/mcp_proxy.py
- [[Redact admin-private data from tool results for non-owner agents.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Send an HTTP request to the MCP server.]] - rationale - gateway/proxy/mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/process_tool_call
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_MCPToolCall]]
- 6 edges to [[_COMMUNITY_MCPPermissionManager]]
- 2 edges to [[_COMMUNITY_StdioConnection]]
- 2 edges to [[_COMMUNITY_MCPToolResult]]
- 1 edge to [[_COMMUNITY_make_event]]

## Top bridge nodes
- [[dot-_execute_tool_call()]] - degree 8, connects to 4 communities
- [[dot-process_tool_result()_1]] - degree 6, connects to 3 communities
- [[dot-process_tool_call()]] - degree 9, connects to 2 communities
- [[dot-_emit_privacy_event()]] - degree 5, connects to 2 communities
- [[dot-_sanitize_admin_private_data()]] - degree 5, connects to 2 communities
