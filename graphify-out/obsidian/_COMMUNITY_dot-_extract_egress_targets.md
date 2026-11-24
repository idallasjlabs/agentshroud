---
type: community
members: 31
---

# ._extract_egress_targets

**Members:** 31 nodes

## Members
- [[dot-_emit_privacy_event()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_extract_egress_targets()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_sanitize_admin_private_data()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-check_approval_required()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-get_stats()_19]] - code - gateway/proxy/mcp_proxy.py
- [[dot-process_tool_call()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-process_tool_result()_1]] - code - gateway/proxy/mcp_proxy.py
- [[dot-send_request()_1]] - code - gateway/proxy/mcp_proxy.py
- [[dot-send_request()_2]] - code - gateway/proxy/mcp_proxy.py
- [[dot-start()_2]] - code - gateway/proxy/mcp_proxy.py
- [[dot-test_bare_host_in_destination_field()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_bare_host_in_non_destination_field_ignored()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_direct_urls_dedup_and_lists()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_invalid_url_without_netloc_ignored()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_list_inherits_parent_key()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_non_matching_text_in_destination_field()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[Any_91]] - code
- [[Best-effort privacy event emission.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Check if a tool call requires approval and wait for it if needed.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Extract outbound URL-like targets from nested MCP tool parameters.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Get proxy statistics._1]] - rationale - gateway/proxy/mcp_proxy.py
- [[Process a tool result coming back (for cases where execution happens…]] - rationale - gateway/proxy/mcp_proxy.py
- [[Process an MCP tool call through the security pipeline. Args tool_call The…]] - rationale - gateway/proxy/mcp_proxy.py
- [[Redact admin-private data from tool results for non-owner agents.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Send a JSON-RPC request and read the response.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Send an HTTP request to the MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Start the MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestExtractEgressTargets]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[_add()]] - code - gateway/proxy/mcp_proxy.py
- [[_scrub()]] - code - gateway/proxy/mcp_proxy.py
- [[_walk()_1]] - code - gateway/proxy/mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_extract_egress_targets
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_test_mcp_proxy.py]]
- 4 edges to [[_COMMUNITY_MCPToolCall]]
- 2 edges to [[_COMMUNITY_ProxyResult]]
- 1 edge to [[_COMMUNITY_make_event]]

## Top bridge nodes
- [[dot-process_tool_call()]] - degree 9, connects to 3 communities
- [[dot-process_tool_result()_1]] - degree 6, connects to 3 communities
- [[dot-_emit_privacy_event()]] - degree 5, connects to 2 communities
- [[dot-_extract_egress_targets()]] - degree 12, connects to 1 community
- [[TestExtractEgressTargets]] - degree 8, connects to 1 community
