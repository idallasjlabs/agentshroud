---
type: community
members: 35
---

# Community 232

**Members:** 35 nodes

## Members
- [[._emit_privacy_event()]] - code - gateway/proxy/mcp_proxy.py
- [[._extract_egress_targets()]] - code - gateway/proxy/mcp_proxy.py
- [[._sanitize_admin_private_data()]] - code - gateway/proxy/mcp_proxy.py
- [[.check_approval_required()]] - code - gateway/proxy/mcp_proxy.py
- [[.process_tool_call()]] - code - gateway/proxy/mcp_proxy.py
- [[.process_tool_result()_1]] - code - gateway/proxy/mcp_proxy.py
- [[.test_body_agent_id_used_when_header_missing()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[.test_clean_tool_call_allowed()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[.test_empty_parameters_allowed()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[.test_header_user_id_overrides_body_agent_id()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[.test_injection_in_parameters_blocked()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[.test_invalid_header_identity_rejected()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[.test_missing_required_fields_returns_422()_1]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[.test_owner_body_identity_rejected_without_header()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[.test_requires_auth()_3]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[.test_response_includes_processing_time()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[A clean tool call with no threats should be allowed (200).]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Best-effort privacy event emission.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Body agent_id is used only when trusted header is absent.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Body-only owner identity must be rejected to prevent impersonation.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Check if a tool call requires approval and wait for it if needed.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Extract outbound URL-like targets from nested MCP tool parameters.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Missing server_name or tool_name should return 422.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[POST mcpproxy without auth should return 401.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Process a tool result coming back (for cases where execution happens externally)]] - rationale - gateway/proxy/mcp_proxy.py
- [[Process an MCP tool call through the security pipeline.          Args]] - rationale - gateway/proxy/mcp_proxy.py
- [[ProxyResult]] - code - gateway/proxy/mcp_proxy.py
- [[Redact admin-private data from tool results for non-owner agents.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Response should include processing_time_ms.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Result of proxying an MCP tool call.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestMCPProxyEndpoint_1]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[Tool call with injection pattern in parameters should return 403.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Tool call with no parameters should be accepted.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[test_mcp_proxy_endpoint.py]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[x-agentshroud-user-id header must override spoofable body agent_id.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_232
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Community 64]]
- 6 edges to [[_COMMUNITY_Community 59]]
- 5 edges to [[_COMMUNITY_Community 230]]
- 3 edges to [[_COMMUNITY_Community 7]]
- 2 edges to [[_COMMUNITY_Community 329]]
- 1 edge to [[_COMMUNITY_Community 85]]
- 1 edge to [[_COMMUNITY_Community 184]]
- 1 edge to [[_COMMUNITY_Community 541]]
- 1 edge to [[_COMMUNITY_Community 132]]
- 1 edge to [[_COMMUNITY_Community 309]]

## Top bridge nodes
- [[ProxyResult]] - degree 18, connects to 5 communities
- [[test_mcp_proxy_endpoint.py]] - degree 5, connects to 3 communities
- [[.process_tool_call()]] - degree 9, connects to 2 communities
- [[.process_tool_result()_1]] - degree 6, connects to 2 communities
- [[._emit_privacy_event()]] - degree 5, connects to 2 communities