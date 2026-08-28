---
type: community
cohesion: 0.29
members: 7
---

# Community 1058

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[.test_base64_in_subdomain_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[.test_enforce_mode_blocks_tunneling()]] - code - gateway/tests/test_dns_filter.py
- [[.test_hex_encoded_subdomain_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[.test_high_entropy_subdomain_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[.test_multiple_long_labels_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[.test_very_long_subdomain_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[TestDNSTunnelingDetection]] - code - gateway/tests/test_dns_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1058
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 1 edge to [[_COMMUNITY_Security Audit & Drift Detection]]

## Top bridge nodes
- [[TestDNSTunnelingDetection]] - degree 10, connects to 2 communities