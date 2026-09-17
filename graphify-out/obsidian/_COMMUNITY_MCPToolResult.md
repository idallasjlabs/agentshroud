---
type: community
cohesion: 0.18
members: 18
---

# MCPToolResult

**Cohesion:** 0.18 - loosely connected
**Members:** 18 nodes

## Members
- [[.__post_init__()_5]] - code - gateway/proxy/mcp_proxy.py
- [[.test_admin_private_data_not_redacted_for_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_admin_private_data_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_clean_result_passes()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_error_result_logged()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_gateway_contributor_paths_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_memory_markers_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_pii_redacted_in_result()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_private_redaction_emits_privacy_event()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_result_audit_logged()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_result_processing_time()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_tool_call_generates_id_and_timestamp()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_tool_result_timestamp_default()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[MCPToolCall]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[MCPToolResult]] - code - gateway/proxy/mcp_proxy.py
- [[Represents an MCP tool result.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestDataclasses]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestProxyResultProcessing]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPToolResult
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_MCPToolCall]]
- 25 edges to [[_COMMUNITY_StdioConnection]]
- 15 edges to [[_COMMUNITY_MCPServerConfig]]
- 7 edges to [[_COMMUNITY_PermissionLevel]]
- 6 edges to [[_COMMUNITY_load_config()]]
- 5 edges to [[_COMMUNITY_MCPInspector]]
- 5 edges to [[_COMMUNITY_MCPAuditTrail]]
- 4 edges to [[_COMMUNITY_MCPPermissionManager]]
- 3 edges to [[_COMMUNITY_FakeProcess]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_TestInspectorEdgeCases]]
- 2 edges to [[_COMMUNITY_.process_tool_call()]]
- 1 edge to [[_COMMUNITY_TestAuditTrail]]
- 1 edge to [[_COMMUNITY_TestInjectionDetection]]

## Top bridge nodes
- [[MCPToolResult]] - degree 79, connects to 14 communities
- [[TestDataclasses]] - degree 17, connects to 7 communities
- [[MCPToolCall]] - degree 16, connects to 7 communities
- [[TestProxyResultProcessing]] - degree 23, connects to 6 communities
- [[.test_result_processing_time()]] - degree 2, connects to 1 community