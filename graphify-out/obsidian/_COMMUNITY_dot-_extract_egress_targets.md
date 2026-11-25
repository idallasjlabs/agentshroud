---
type: community
members: 11
---

# ._extract_egress_targets

**Members:** 11 nodes

## Members
- [[dot-_extract_egress_targets()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-test_bare_host_in_destination_field()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_bare_host_in_non_destination_field_ignored()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_direct_urls_dedup_and_lists()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_invalid_url_without_netloc_ignored()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_list_inherits_parent_key()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_non_matching_text_in_destination_field()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[Extract outbound URL-like targets from nested MCP tool parameters.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestExtractEgressTargets]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[_add()]] - code - gateway/proxy/mcp_proxy.py
- [[_walk()_1]] - code - gateway/proxy/mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_extract_egress_targets
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_mcp_proxy.py]]
- 1 edge to [[_COMMUNITY_ProxyResult]]
- 1 edge to [[_COMMUNITY_MCPServerConfig]]

## Top bridge nodes
- [[dot-_extract_egress_targets()]] - degree 12, connects to 3 communities
- [[TestExtractEgressTargets]] - degree 8, connects to 1 community
