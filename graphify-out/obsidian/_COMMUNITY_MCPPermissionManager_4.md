---
type: community
cohesion: 0.12
members: 24
---

# MCPPermissionManager

**Cohesion:** 0.12 - loosely connected
**Members:** 24 nodes

## Members
- [[dot-__post_init__()_7]] - code - gateway/proxy/mcp_proxy.py
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
- [[dot-test_tool_call_generates_id_and_timestamp()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_tool_result_timestamp_default()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[MCPToolCall]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[MCPToolResult]] - code - gateway/proxy/mcp_proxy.py
- [[Represents an MCP tool result.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestAuditQueries]] - code - gateway/tests/test_mcp_proxy.py
- [[TestDataclasses]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestProxyResultProcessing]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPPermissionManager
SORT file.name ASC
```

## Connections to other communities
- 33 edges to [[_COMMUNITY_MCPPermissionManager]]
- 15 edges to [[_COMMUNITY_StdioConnection_1]]
- 13 edges to [[_COMMUNITY_StdioConnection]]
- 12 edges to [[_COMMUNITY_MCPPermissionManager_1]]
- 11 edges to [[_COMMUNITY_MCPInspector]]
- 8 edges to [[_COMMUNITY_PermissionLevel]]
- 6 edges to [[_COMMUNITY_MCPAuditTrail]]
- 6 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 5 edges to [[_COMMUNITY_MCPPermissionManager_2]]
- 1 edge to [[_COMMUNITY_MCPToolResult]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager_5]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager_6]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager_7]]
- 1 edge to [[_COMMUNITY_Athena — Knowledge Distiller_4]]
- 1 edge to [[_COMMUNITY_TestAuditTrail]]

## Top bridge nodes
- [[MCPToolResult]] - degree 77, connects to 14 communities
- [[TestDataclasses]] - degree 17, connects to 8 communities
- [[MCPToolCall]] - degree 16, connects to 8 communities
- [[TestProxyResultProcessing]] - degree 23, connects to 6 communities
- [[TestAuditQueries]] - degree 20, connects to 6 communities
