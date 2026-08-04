---
type: community
cohesion: 0.11
members: 18
---

# Module Group 255

**Cohesion:** 0.11 - loosely connected
**Members:** 18 nodes

## Members
- [[.test_body_agent_id_used_without_header()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_clean_result_accepted()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_header_user_id_overrides_body_agent_id()_1]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_invalid_header_identity_rejected()_1]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_owner_body_identity_rejected_without_header()_1]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_result_missing_server_name_rejected()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_result_requires_auth()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_result_returns_processing_time()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_result_with_null_content()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_result_with_pii_is_audited_not_blocked()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[A result containing PII is audited and redacted — never blocked (results are nev]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[A result with no threats should be accepted and audited (200).]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[Body-only owner identity must be rejected to prevent impersonation._1]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[Null content is handled gracefully.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[Request missing required server_name is rejected with 422.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[Response includes processing_time_ms.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[TestMCPResultEndpoint]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[Unauthenticated request is rejected.]] - rationale - gateway/tests/test_mcp_result_endpoint.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_255
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_SSH Proxy & Gateway Config]]
- 1 edge to [[_COMMUNITY_Tool Result Sanitizer]]
- 1 edge to [[_COMMUNITY_Ledger Config & Test Infra]]
- 1 edge to [[_COMMUNITY_Enhanced Approval Queue]]
- 1 edge to [[_COMMUNITY_MCP Inspector & Audit]]

## Top bridge nodes
- [[TestMCPResultEndpoint]] - degree 17, connects to 5 communities
