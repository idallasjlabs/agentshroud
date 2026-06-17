---
type: community
cohesion: 0.19
members: 17
---

# Module Group 266

**Cohesion:** 0.19 - loosely connected
**Members:** 17 nodes

## Members
- [[.__post_init__()_1]] - code - gateway/proxy/mcp_proxy.py
- [[.test_admin_private_data_not_redacted_for_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_admin_private_data_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_clean_result_passes()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_error_result_logged()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_gateway_contributor_paths_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_memory_markers_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_pii_redacted_in_result()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_private_redaction_emits_privacy_event()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_processing_time_recorded()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_result_audit_logged()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_result_processing_time()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_tool_result_timestamp_default()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[MCPToolResult]] - code - gateway/proxy/mcp_proxy.py
- [[Represents an MCP tool result.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestProcessingTime]] - code - gateway/tests/test_mcp_proxy.py
- [[TestProxyResultProcessing]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_266
SORT file.name ASC
```

## Connections to other communities
- 31 edges to [[_COMMUNITY_MCP Config & Proxy]]
- 18 edges to [[_COMMUNITY_Module Group 78]]
- 10 edges to [[_COMMUNITY_MCP Inspector & Audit]]
- 7 edges to [[_COMMUNITY_Module Group 124]]
- 4 edges to [[_COMMUNITY_Module Group 139]]
- 4 edges to [[_COMMUNITY_Module Group 154]]
- 3 edges to [[_COMMUNITY_MCP Permissions Manager]]
- 2 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 2 edges to [[_COMMUNITY_Module Group 205]]
- 1 edge to [[_COMMUNITY_Module Group 387]]
- 1 edge to [[_COMMUNITY_Module Group 442]]
- 1 edge to [[_COMMUNITY_Module Group 468]]

## Top bridge nodes
- [[MCPToolResult]] - degree 71, connects to 12 communities
- [[TestProxyResultProcessing]] - degree 23, connects to 6 communities
- [[TestProcessingTime]] - degree 16, connects to 6 communities
- [[.test_tool_result_timestamp_default()]] - degree 2, connects to 1 community
- [[.test_processing_time_recorded()]] - degree 2, connects to 1 community