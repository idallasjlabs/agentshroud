---
type: community
members: 7
---

# TestNormalDNSResolution

**Members:** 7 nodes

## Members
- [[dot-test_common_services_allowed()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_long_but_legitimate_domain()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_monitor_mode_never_blocks()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_normal_domain_allowed()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_subdomain_allowed()]] - code - gateway/tests/test_dns_filter.py
- [[Even suspicious queries pass in monitor mode.]] - rationale - gateway/tests/test_dns_filter.py
- [[TestNormalDNSResolution]] - code - gateway/tests/test_dns_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestNormalDNSResolution
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_DNSFilterConfig]]

## Top bridge nodes
- [[TestNormalDNSResolution]] - degree 6, connects to 1 community
