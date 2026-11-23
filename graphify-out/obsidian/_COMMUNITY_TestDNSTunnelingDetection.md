---
type: community
members: 7
---

# TestDNSTunnelingDetection

**Members:** 7 nodes

## Members
- [[dot-test_base64_in_subdomain_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_enforce_mode_blocks_tunneling()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_hex_encoded_subdomain_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_high_entropy_subdomain_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_multiple_long_labels_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_very_long_subdomain_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[TestDNSTunnelingDetection]] - code - gateway/tests/test_dns_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestDNSTunnelingDetection
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_DNSFilterConfig]]

## Top bridge nodes
- [[TestDNSTunnelingDetection]] - degree 7, connects to 1 community
