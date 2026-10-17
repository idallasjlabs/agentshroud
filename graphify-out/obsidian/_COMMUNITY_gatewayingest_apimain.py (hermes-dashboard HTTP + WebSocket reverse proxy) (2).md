---
type: community
members: 14
---

# gateway/ingest_api/main.py (/hermes-dashboard/ HTTP + WebSocket reverse proxy) (2)

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
TABLE source_file, type FROM #community/gateway/ingest_api/mainpy_/hermes-dashboard/_HTTP__WebSocket_reverse_proxy_2
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]

## Top bridge nodes
- [[mcp_proxy_endpoint()]] - degree 8, connects to 2 communities
- [[mcp_result_endpoint()]] - degree 7, connects to 2 communities
- [[MCPProxyRequest]] - degree 4, connects to 2 communities
- [[MCPResultRequest]] - degree 4, connects to 2 communities
- [[_resolve_effective_agent_id()]] - degree 5, connects to 1 community
