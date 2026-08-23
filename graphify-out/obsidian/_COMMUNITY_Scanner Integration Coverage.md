---
type: community
cohesion: 0.50
members: 4
---

# Scanner Integration Coverage

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_full_compose()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_no_compose_zero()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_unreadable_first_path_falls_through()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestResourceAvailability]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Scanner_Integration_Coverage
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Scanner Integration Coverage]]
- 1 edge to [[_COMMUNITY_Scanner Integration Coverage]]

## Top bridge nodes
- [[TestResourceAvailability]] - degree 4, connects to 1 community
- [[.test_full_compose()]] - degree 2, connects to 1 community
- [[.test_unreadable_first_path_falls_through()]] - degree 2, connects to 1 community