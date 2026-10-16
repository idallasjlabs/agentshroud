---
type: community
cohesion: 0.11
members: 26
---

# MCPPermissionManager

**Cohesion:** 0.11 - loosely connected
**Members:** 26 nodes

## Members
- [[dot-__post_init__()_3]] - code - gateway/proxy/mcp_proxy.py
- [[dot-test_admin_private_data_not_redacted_for_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_admin_private_data_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_clean_result_passes()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_clean_result_passes_through()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_credit_card_detected()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_credit_card_redacted()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_email_detected_but_low_threat()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_error_result_logged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_gateway_contributor_paths_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_memory_markers_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_pii_in_tool_result_redacted()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_pii_redacted_in_result()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_private_redaction_emits_privacy_event()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_result_audit_logged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_result_processing_time()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_ssn_detected_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_ssn_redacted_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_tool_call_generates_id_and_timestamp()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_tool_result_timestamp_default()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[MCPToolCall]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[MCPToolResult]] - code - gateway/proxy/mcp_proxy.py
- [[Represents an MCP tool result.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestDataclasses]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestPIIDetection_2]] - code - gateway/tests/test_mcp_proxy.py
- [[TestProxyResultProcessing]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPPermissionManager
SORT file.name ASC
```

## Connections to other communities
- 32 edges to [[_COMMUNITY_MCPPermissionManager]]
- 25 edges to [[_COMMUNITY_StdioConnection]]
- 18 edges to [[_COMMUNITY_MCPPermissionManager_1]]
- 9 edges to [[_COMMUNITY_PermissionLevel]]
- 6 edges to [[_COMMUNITY_MCPAuditTrail]]
- 6 edges to [[_COMMUNITY_MCPInspector]]
- 6 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 5 edges to [[_COMMUNITY_MCPPermissionManager_2]]
- 3 edges to [[_COMMUNITY_MCPPermissionManager_4]]
- 2 edges to [[_COMMUNITY_dot-process_tool_call]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager_5]]
- 1 edge to [[_COMMUNITY_TestAuditTrail]]
- 1 edge to [[_COMMUNITY_MCPToolResult]]

## Top bridge nodes
- [[MCPToolResult]] - degree 77, connects to 13 communities
- [[TestDataclasses]] - degree 17, connects to 7 communities
- [[MCPToolCall]] - degree 16, connects to 7 communities
- [[TestProxyResultProcessing]] - degree 23, connects to 6 communities
- [[TestPIIDetection_2]] - degree 21, connects to 6 communities
