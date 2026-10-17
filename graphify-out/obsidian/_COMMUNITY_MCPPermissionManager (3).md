---
type: community
members: 22
---

# MCPPermissionManager (3)

**Members:** 22 nodes

## Members
- [[dot-__post_init__()_4]] - code - gateway/proxy/mcp_proxy.py
- [[dot-test_admin_private_data_not_redacted_for_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_admin_private_data_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_blocked_entries()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_clean_result_passes()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_error_result_logged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_failed_entries()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_filter_by_agent()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_filter_by_server()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_filter_by_tool()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_gateway_contributor_paths_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_generate_report()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_memory_markers_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_pii_redacted_in_result()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_private_redaction_emits_privacy_event()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_result_audit_logged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_result_processing_time()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_tool_result_timestamp_default()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[MCPToolResult]] - code - gateway/proxy/mcp_proxy.py
- [[Represents an MCP tool result.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestAuditQueries]] - code - gateway/tests/test_mcp_proxy.py
- [[TestProxyResultProcessing]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPPermissionManager_3
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_MCPPermissionManager]]
- 24 edges to [[_COMMUNITY_StdioConnection]]
- 8 edges to [[_COMMUNITY_MCPInspector]]
- 8 edges to [[_COMMUNITY_StdioConnection (2)]]
- 6 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 5 edges to [[_COMMUNITY_MCPPermissionManager (2)]]
- 4 edges to [[_COMMUNITY_MCPAuditTrail]]
- 2 edges to [[_COMMUNITY_PermissionLevel]]
- 1 edge to [[_COMMUNITY_MCPToolResult]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager (6)]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager (7)]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager (5)]]
- 1 edge to [[_COMMUNITY_TestAuditTrail]]

## Top bridge nodes
- [[MCPToolResult]] - degree 77, connects to 12 communities
- [[TestProxyResultProcessing]] - degree 23, connects to 6 communities
- [[TestAuditQueries]] - degree 20, connects to 6 communities
- [[dot-test_tool_result_timestamp_default()]] - degree 2, connects to 1 community
- [[dot-test_result_processing_time()]] - degree 2, connects to 1 community
