---
type: community
cohesion: 0.33
members: 6
---

# Community 1123

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[.test_default_allows_all_domains()]] - code - gateway/tests/test_dns_filter.py
- [[.test_default_mode_is_enforce()]] - code - gateway/tests/test_dns_filter.py
- [[.test_generous_defaults()]] - code - gateway/tests/test_dns_filter.py
- [[.test_strict_has_allowlist()]] - code - gateway/tests/test_dns_filter.py
- [[Default mode is enforce after v0.8.0 enforcement hardening.]] - rationale - gateway/tests/test_dns_filter.py
- [[TestDNSFilterConfig]] - code - gateway/tests/test_dns_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1123
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 1 edge to [[_COMMUNITY_Security Audit & Drift Detection]]

## Top bridge nodes
- [[TestDNSFilterConfig]] - degree 8, connects to 2 communities