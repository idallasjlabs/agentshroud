---
type: community
cohesion: 0.29
members: 7
---

# Operating Rules (Non-Negotiable)

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[.test_bare_host_in_destination_field()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_bare_host_in_non_destination_field_ignored()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_direct_urls_dedup_and_lists()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_invalid_url_without_netloc_ignored()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_list_inherits_parent_key()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_non_matching_text_in_destination_field()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestExtractEgressTargets]] - code - gateway/tests/test_mcp_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Operating_Rules_Non-Negotiable
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 3 edges to [[_COMMUNITY_GitGuard]]
- 3 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py]]
- 1 edge to [[_COMMUNITY_brand-guidelines]]
- 1 edge to [[_COMMUNITY_TestParanoidConfig]]
- 1 edge to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY_AgentShroud v0.9.0 — Human Interface Testing Gui]]

## Top bridge nodes
- [[TestExtractEgressTargets]] - degree 21, connects to 7 communities