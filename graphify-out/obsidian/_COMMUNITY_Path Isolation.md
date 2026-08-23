---
type: community
cohesion: 0.67
members: 3
---

# Path Isolation

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[.test_get_stats()_1]] - code - gateway/tests/test_path_isolation.py
- [[.test_global_stats()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[Test getting statistics.]] - rationale - gateway/tests/test_path_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Path_Isolation
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Multi Turn Tracker]]
- 1 edge to [[_COMMUNITY_Path Isolation]]

## Top bridge nodes
- [[.test_global_stats()]] - degree 2, connects to 1 community
- [[.test_get_stats()_1]] - degree 2, connects to 1 community