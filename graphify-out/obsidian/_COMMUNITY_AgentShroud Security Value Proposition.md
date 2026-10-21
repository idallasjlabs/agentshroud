---
type: community
members: 20
---

# AgentShroud Security Value Proposition

**Members:** 20 nodes

## Members
- [[dot-test_body_agent_id_used_when_header_missing()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_clean_tool_call_allowed()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_empty_parameters_allowed()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_header_user_id_overrides_body_agent_id()_1]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_injection_in_parameters_blocked()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_invalid_header_identity_rejected()_1]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_missing_required_fields_returns_422()_1]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_owner_body_identity_rejected_without_header()_1]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_requires_auth()_3]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[dot-test_response_includes_processing_time()]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[A clean tool call with no threats should be allowed (200).]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Body agent_id is used only when trusted header is absent.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Body-only owner identity must be rejected to prevent impersonation._1]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Missing server_name or tool_name should return 422.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[POST mcpproxy without auth should return 401.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Response should include processing_time_ms.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[TestMCPProxyEndpoint_1]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[Tool call with injection pattern in parameters should return 403.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[Tool call with no parameters should be accepted.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py
- [[x-agentshroud-user-id header must override spoofable body agent_id.]] - rationale - gateway/tests/test_mcp_proxy_endpoint.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Security_Value_Proposition
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_CrossBotTrustLedger]]

## Top bridge nodes
- [[TestMCPProxyEndpoint_1]] - degree 12, connects to 1 community
