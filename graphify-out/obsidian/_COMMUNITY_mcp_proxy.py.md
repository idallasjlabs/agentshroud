---
type: community
members: 49
---

# mcp_proxy.py

**Members:** 49 nodes

## Members
- [[dot-test_body_agent_id_used_when_header_missing()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_body_agent_id_used_without_header()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[dot-test_clean_result_accepted()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[dot-test_clean_tool_call_allowed()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_empty_parameters_allowed()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_header_user_id_overrides_body_agent_id()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_header_user_id_overrides_body_agent_id()_1]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[dot-test_injection_in_parameters_blocked()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_invalid_header_identity_rejected()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_invalid_header_identity_rejected()_1]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[dot-test_missing_required_fields_returns_422()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_owner_body_identity_rejected_without_header()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_owner_body_identity_rejected_without_header()_1]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[dot-test_requires_auth()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_response_includes_processing_time()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_result_missing_server_name_rejected()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[dot-test_result_requires_auth()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[dot-test_result_returns_processing_time()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[dot-test_result_with_null_content()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[dot-test_result_with_pii_is_audited_not_blocked()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[A clean tool call with no threats should be allowed (200).]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[A result containing PII is audited and redacted — never blocked (results are…]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[A result with no threats should be accepted and audited (200).]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[Body agent_id is used only when trusted header is absent.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Body-only owner identity must be rejected to prevent impersonation.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Body-only owner identity must be rejected to prevent impersonation._1]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[Integration tests for POST mcpproxy endpoint (P4 MCP proxy wiring).]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Missing server_name or tool_name should return 422.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Null content is handled gracefully.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[POST mcpproxy without auth should return 401.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[ProxyResult]] - code - gateway/proxy/mcp_proxy.py
- [[Request missing required server_name is rejected with 422.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[Response includes processing_time_ms.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[Response should include processing_time_ms.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Result of proxying an MCP tool call.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestMCPProxyEndpoint]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[TestMCPResultEndpoint]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[Tool call with injection pattern in parameters should return 403.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Tool call with no parameters should be accepted.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Unauthenticated request is rejected.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[_capture()_3]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[_capture()_4]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[_capture()_5]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[_capture()_6]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[asyncio_28]] - code
- [[asyncio_29]] - code
- [[mcp_proxy.py_2]] - code - gateway/proxy/mcp_proxy.py
- [[test_mcp_proxy_endpoint.py]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[x-agentshroud-user-id header must override spoofable body agent_id.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/mcp_proxypy
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_mcp_proxy.py]]
- 5 edges to [[_COMMUNITY_ingest_apimain.py]]
- 4 edges to [[_COMMUNITY_MCPServerConfig]]
- 4 edges to [[_COMMUNITY_MCPProxy]]
- 4 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 3 edges to [[_COMMUNITY_EnhancedApprovalQueue]]
- 2 edges to [[_COMMUNITY_MCPToolCall]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager]]
- 2 edges to [[_COMMUNITY_MCPAuditTrail]]
- 2 edges to [[_COMMUNITY_PermissionLevel]]
- 1 edge to [[_COMMUNITY_app]]
- 1 edge to [[_COMMUNITY_test_mcp_proxy_coverage.py]]
- 1 edge to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[mcp_proxy.py_2]] - degree 30, connects to 12 communities
- [[ProxyResult]] - degree 13, connects to 3 communities
- [[test_mcp_proxy_endpoint.py]] - degree 8, connects to 3 communities
- [[TestMCPResultEndpoint]] - degree 12, connects to 1 community
