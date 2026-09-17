---
type: community
cohesion: 0.50
members: 4
---

# ConsistencyScore

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.score_response_consistency()]] - code - gateway/security/multi_turn_tracker.py
- [[Compute a heuristic consistency score between query and response.          Retur]] - rationale - gateway/security/multi_turn_tracker.py
- [[ConsistencyScore]] - code - gateway/security/multi_turn_tracker.py
- [[Heuristic consistency score between a query and its response.]] - rationale - gateway/security/multi_turn_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ConsistencyScore
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_Enum]]

## Top bridge nodes
- [[ConsistencyScore]] - degree 3, connects to 1 community
- [[.score_response_consistency()]] - degree 3, connects to 1 community