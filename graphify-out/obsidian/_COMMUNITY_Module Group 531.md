---
type: community
cohesion: 0.40
members: 5
---

# Module Group 531

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_empty_dir_returns_false()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_fresh_file_returns_true()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_old_file_returns_false()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_stat_error_returns_false()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestIsFresh]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_531
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Module Group 131]]
- 1 edge to [[_COMMUNITY_Module Group 170]]
- 1 edge to [[_COMMUNITY_Module Group 243]]

## Top bridge nodes
- [[.test_old_file_returns_false()]] - degree 3, connects to 2 communities
- [[TestIsFresh]] - degree 5, connects to 1 community
- [[.test_fresh_file_returns_true()]] - degree 2, connects to 1 community
