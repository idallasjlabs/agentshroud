---
type: community
members: 2
---

# .test_private_ip_filtering

**Members:** 2 nodes

## Members
- [[dot-test_private_ip_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[Test that private IP addresses are filtered.]] - rationale - gateway/tests/test_outbound_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_private_ip_filtering
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_TestOutboundInfoFilter]]

## Top bridge nodes
- [[dot-test_private_ip_filtering()]] - degree 2, connects to 1 community
