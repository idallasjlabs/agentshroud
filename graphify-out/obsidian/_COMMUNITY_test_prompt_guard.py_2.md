---
type: community
cohesion: 0.14
members: 14
---

# test_prompt_guard.py

**Cohesion:** 0.14 - loosely connected
**Members:** 14 nodes

## Members
- [[MCP tool call interception endpoint. Receives an MCP tool call, runs it through…]] - rationale - gateway/ingest_api/main.py
- [[MCP tool result outbound audit endpoint. Receives a tool result from the bot's…]] - rationale - gateway/ingest_api/main.py
- [[MCPProxyRequest]] - code - gateway/ingest_api/main.py
- [[MCPResultRequest]] - code - gateway/ingest_api/main.py
- [[Request body for POST mcpproxy — intercept a single MCP tool call.]] - rationale - gateway/ingest_api/main.py
- [[Request body for POST mcpresult — submit a tool result for outbound audit.]] - rationale - gateway/ingest_api/main.py
- [[Resolve trusted effective identity and prevent owner spoofing via body.]] - rationale - gateway/ingest_api/main.py
- [[Return True if the recipient is in the allowlist.]] - rationale - gateway/ingest_api/main.py
- [[Validate and normalize agentuser identity used for policy checks.]] - rationale - gateway/ingest_api/main.py
- [[_is_imessage_recipient_allowed()]] - code - gateway/ingest_api/main.py
- [[_normalize_agent_identity()]] - code - gateway/ingest_api/main.py
- [[_resolve_effective_agent_id()]] - code - gateway/ingest_api/main.py
- [[mcp_proxy_endpoint()]] - code - gateway/ingest_api/main.py
- [[mcp_result_endpoint()]] - code - gateway/ingest_api/main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_prompt_guardpy
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 2 edges to [[_COMMUNITY__FakeRBAC]]
- 2 edges to [[_COMMUNITY_AuditChain_1]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL_4]]

## Top bridge nodes
- [[mcp_proxy_endpoint()]] - degree 8, connects to 3 communities
- [[mcp_result_endpoint()]] - degree 7, connects to 3 communities
- [[MCPProxyRequest]] - degree 4, connects to 2 communities
- [[MCPResultRequest]] - degree 4, connects to 2 communities
- [[_resolve_effective_agent_id()]] - degree 5, connects to 1 community
