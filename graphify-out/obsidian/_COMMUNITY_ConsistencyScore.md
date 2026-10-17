---
type: community
members: 4
---

# ConsistencyScore

**Members:** 4 nodes

## Members
- [[dot-score_response_consistency()]] - code - gateway/security/multi_turn_tracker.py
- [[Compute a heuristic consistency score between query and response.          Retur]] - rationale - gateway/security/multi_turn_tracker.py
- [[ConsistencyScore]] - code - gateway/security/multi_turn_tracker.py
- [[Heuristic consistency score between a query and its response.]] - rationale - gateway/security/multi_turn_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ConsistencyScore
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_TestToolChainAnalyzer]]

## Top bridge nodes
- [[ConsistencyScore]] - degree 3, connects to 1 community
- [[dot-score_response_consistency()]] - degree 3, connects to 1 community
