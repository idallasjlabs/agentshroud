---
type: community
members: 38
---

# ProxyResult

**Members:** 38 nodes

## Members
- [[dot-_emit_privacy_event()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_sanitize_admin_private_data()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-check_approval_required()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-process_tool_call()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-process_tool_result()_1]] - code - gateway/proxy/mcp_proxy.py
- [[dot-test_body_agent_id_used_when_header_missing()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_clean_tool_call_allowed()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_empty_parameters_allowed()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_header_user_id_overrides_body_agent_id()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_injection_in_parameters_blocked()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_invalid_header_identity_rejected()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_missing_required_fields_returns_422()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_owner_body_identity_rejected_without_header()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_requires_auth()_1]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_response_includes_processing_time()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[A clean tool call with no threats should be allowed (200).]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Best-effort privacy event emission.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Body agent_id is used only when trusted header is absent.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Body-only owner identity must be rejected to prevent impersonation.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Check if a tool call requires approval and wait for it if needed.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Integration tests for POST mcpproxy endpoint (P4 MCP proxy wiring).]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Missing server_name or tool_name should return 422.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[POST mcpproxy without auth should return 401.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Process a tool result coming back (for cases where execution happens…]] - rationale - gateway/proxy/mcp_proxy.py
- [[Process an MCP tool call through the security pipeline. Args tool_call The…]] - rationale - gateway/proxy/mcp_proxy.py
- [[ProxyResult]] - code - gateway/proxy/mcp_proxy.py
- [[Redact admin-private data from tool results for non-owner agents.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Response should include processing_time_ms.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Result of proxying an MCP tool call.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestMCPProxyEndpoint_1]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[Tool call with injection pattern in parameters should return 403.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Tool call with no parameters should be accepted.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[_capture()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[_capture()_1]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[_scrub()]] - code - gateway/proxy/mcp_proxy.py
- [[asyncio_30]] - code
- [[test_mcp_proxy_endpoint.py]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[x-agentshroud-user-id header must override spoofable body agent_id.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ProxyResult
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_test_mcp_proxy.py]]
- 3 edges to [[_COMMUNITY_MCPToolCall]]
- 3 edges to [[_COMMUNITY_TestMCPResultEndpoint]]
- 3 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_dot-_extract_egress_targets]]
- 1 edge to [[_COMMUNITY_MCPServerConfig]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[test_mcp_proxy_endpoint.py]] - degree 8, connects to 4 communities
- [[ProxyResult]] - degree 13, connects to 3 communities
- [[dot-process_tool_call()]] - degree 9, connects to 3 communities
- [[dot-process_tool_result()_1]] - degree 6, connects to 2 communities
- [[dot-_sanitize_admin_private_data()]] - degree 6, connects to 2 communities
