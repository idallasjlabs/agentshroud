---
type: community
cohesion: 0.29
members: 7
---

# Community 1057

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[.test_common_services_allowed()]] - code - gateway/tests/test_dns_filter.py
- [[.test_long_but_legitimate_domain()]] - code - gateway/tests/test_dns_filter.py
- [[.test_monitor_mode_never_blocks()]] - code - gateway/tests/test_dns_filter.py
- [[.test_normal_domain_allowed()]] - code - gateway/tests/test_dns_filter.py
- [[.test_subdomain_allowed()]] - code - gateway/tests/test_dns_filter.py
- [[Even suspicious queries pass in monitor mode.]] - rationale - gateway/tests/test_dns_filter.py
- [[TestNormalDNSResolution]] - code - gateway/tests/test_dns_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1057
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 1 edge to [[_COMMUNITY_Security Audit & Drift Detection]]

## Top bridge nodes
- [[TestNormalDNSResolution]] - degree 9, connects to 2 communities