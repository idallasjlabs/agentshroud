---
type: community
cohesion: 0.40
members: 5
---

# TestIsFresh

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_empty_dir_returns_false()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_fresh_file_returns_true()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_old_file_returns_false()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_stat_error_returns_false()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestIsFresh_1]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestIsFresh
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY__w()]]
- 1 edge to [[_COMMUNITY_test_scanner_integration_coverage.py]]
- 1 edge to [[_COMMUNITY__age()]]

## Top bridge nodes
- [[.test_old_file_returns_false()]] - degree 3, connects to 2 communities
- [[TestIsFresh_1]] - degree 5, connects to 1 community
- [[.test_fresh_file_returns_true()]] - degree 2, connects to 1 community