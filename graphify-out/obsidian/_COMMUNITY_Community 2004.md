---
type: community
members: 8
---

# Community 2004

**Members:** 8 nodes

## Members
- [[.test_domains_in_default_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[.test_domains_not_denylisted()]] - code - gateway/tests/test_egress_filter.py
- [[.test_egress_filter_allows_in_enforce_mode()]] - code - gateway/tests/test_egress_filter.py
- [[All four domains must be in EgressFilterConfig's default allowlist.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter in enforce mode allows all four domains for openclaw.]] - rationale - gateway/tests/test_egress_filter.py
- [[None of the four domains should match the default denylist.]] - rationale - gateway/tests/test_egress_filter.py
- [[TestOpenClawResearchDomainsAllowlisted]] - code - gateway/tests/test_egress_filter.py
- [[Verify that OpenClaw's web_searchresearch destinations are pre-approved.      T]] - rationale - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_2004
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Community 17]]
- 3 edges to [[_COMMUNITY_Community 21]]
- 2 edges to [[_COMMUNITY_Community 1119]]
- 1 edge to [[_COMMUNITY_Community 93]]

## Top bridge nodes
- [[TestOpenClawResearchDomainsAllowlisted]] - degree 11, connects to 4 communities
- [[.test_egress_filter_allows_in_enforce_mode()]] - degree 4, connects to 2 communities
- [[.test_domains_in_default_allowlist()]] - degree 3, connects to 1 community
- [[.test_domains_not_denylisted()]] - degree 3, connects to 1 community