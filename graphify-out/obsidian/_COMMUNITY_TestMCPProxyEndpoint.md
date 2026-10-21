---
type: community
members: 23
---

# TestMCPProxyEndpoint

**Members:** 23 nodes

## Members
- [[dot-test_body_agent_id_used_when_header_missing()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_clean_tool_call_allowed()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_empty_parameters_allowed()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_header_user_id_overrides_body_agent_id()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_injection_in_parameters_blocked()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_invalid_header_identity_rejected()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_missing_required_fields_returns_422()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_owner_body_identity_rejected_without_header()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_requires_auth()_2]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_response_includes_processing_time()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[A clean tool call with no threats should be allowed (200).]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Body agent_id is used only when trusted header is absent.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Body-only owner identity must be rejected to prevent impersonation.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Missing server_name or tool_name should return 422.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[POST mcpproxy without auth should return 401.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[ProxyResult]] - code - gateway/proxy/mcp_proxy.py
- [[Response should include processing_time_ms.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Result of proxying an MCP tool call.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestMCPProxyEndpoint_1]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[Tool call with injection pattern in parameters should return 403.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Tool call with no parameters should be accepted.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[test_mcp_proxy_endpoint.py]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[x-agentshroud-user-id header must override spoofable body agent_id.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestMCPProxyEndpoint
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_MCPPermissionManager (3)]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 3 edges to [[_COMMUNITY_MCPInspector]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager]]
- 1 edge to [[_COMMUNITY_PermissionLevel]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager (2)]]
- 1 edge to [[_COMMUNITY_StdioConnection (2)]]
- 1 edge to [[_COMMUNITY_MCPAuditTrail]]
- 1 edge to [[_COMMUNITY_TestMCPResultEndpoint]]
- 1 edge to [[_COMMUNITY_ForwardRequest (2)]]

## Top bridge nodes
- [[ProxyResult]] - degree 18, connects to 7 communities
- [[test_mcp_proxy_endpoint.py]] - degree 5, connects to 3 communities
