---
type: community
members: 36
---

# Community 965

**Members:** 36 nodes

## Members
- [[.__post_init__()_1]] - code - gateway/proxy/mcp_proxy.py
- [[._emit_privacy_event()]] - code - gateway/proxy/mcp_proxy.py
- [[._execute_tool_call()]] - code - gateway/proxy/mcp_proxy.py
- [[._extract_egress_targets()]] - code - gateway/proxy/mcp_proxy.py
- [[._sanitize_admin_private_data()]] - code - gateway/proxy/mcp_proxy.py
- [[.check_approval_required()]] - code - gateway/proxy/mcp_proxy.py
- [[.process_tool_call()]] - code - gateway/proxy/mcp_proxy.py
- [[.process_tool_result()_1]] - code - gateway/proxy/mcp_proxy.py
- [[.send_request()_1]] - code - gateway/proxy/mcp_proxy.py
- [[.test_admin_private_data_not_redacted_for_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_admin_private_data_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_bare_host_in_destination_field()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_bare_host_in_non_destination_field_ignored()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_clean_result_passes()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_direct_urls_dedup_and_lists()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_error_result_logged()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_gateway_contributor_paths_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_invalid_url_without_netloc_ignored()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_list_inherits_parent_key()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_memory_markers_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_non_matching_text_in_destination_field()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_pii_redacted_in_result()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_private_redaction_emits_privacy_event()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_result_audit_logged()]] - code - gateway/tests/test_mcp_proxy.py
- [[Actually execute the tool call against the MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Best-effort privacy event emission.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Check if a tool call requires approval and wait for it if needed.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Extract outbound URL-like targets from nested MCP tool parameters.]] - rationale - gateway/proxy/mcp_proxy.py
- [[MCPToolResult]] - code - gateway/proxy/mcp_proxy.py
- [[Process a tool result coming back (for cases where execution happens externally)]] - rationale - gateway/proxy/mcp_proxy.py
- [[Process an MCP tool call through the security pipeline.          Args]] - rationale - gateway/proxy/mcp_proxy.py
- [[Redact admin-private data from tool results for non-owner agents.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Represents an MCP tool result.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Send an HTTP request to the MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestExtractEgressTargets]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestProxyResultProcessing]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_965
SORT file.name ASC
```

## Connections to other communities
- 39 edges to [[_COMMUNITY_Community 64]]
- 31 edges to [[_COMMUNITY_Community 132]]
- 22 edges to [[_COMMUNITY_Community 54]]
- 6 edges to [[_COMMUNITY_Community 35]]
- 4 edges to [[_COMMUNITY_Community 184]]
- 2 edges to [[_COMMUNITY_Community 978]]
- 2 edges to [[_COMMUNITY_Community 2038]]
- 1 edge to [[_COMMUNITY_Community 2048]]
- 1 edge to [[_COMMUNITY_Community 68]]
- 1 edge to [[_COMMUNITY_Community 85]]
- 1 edge to [[_COMMUNITY_Community 941]]
- 1 edge to [[_COMMUNITY_Community 1970]]

## Top bridge nodes
- [[MCPToolResult]] - degree 79, connects to 8 communities
- [[TestProxyResultProcessing]] - degree 23, connects to 5 communities
- [[TestExtractEgressTargets]] - degree 21, connects to 5 communities
- [[._execute_tool_call()]] - degree 8, connects to 3 communities
- [[._sanitize_admin_private_data()]] - degree 6, connects to 3 communities