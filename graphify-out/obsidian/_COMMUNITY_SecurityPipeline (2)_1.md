---
type: community
cohesion: 0.40
members: 5
---

# SecurityPipeline (2)

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[dot-test_get_stats()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_global_stats()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_global_stats()_1]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[Test getting global statistics.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test getting statistics.]] - rationale - gateway/tests/test_path_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SecurityPipeline_2
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_PathIsolationManager]]
- 1 edge to [[_COMMUNITY_test_soc_router_coverage.py]]

## Top bridge nodes
- [[dot-test_global_stats()_1]] - degree 3, connects to 1 community
- [[dot-test_global_stats()]] - degree 2, connects to 1 community
- [[dot-test_get_stats()]] - degree 2, connects to 1 community
