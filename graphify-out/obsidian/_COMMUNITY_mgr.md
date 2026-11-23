---
type: community
members: 3
---

# mgr

**Members:** 3 nodes

## Members
- [[In-memory delegation manager (no disk IO).]] - rationale - gateway/tests/test_delegation.py
- [[fixture_57]] - code
- [[mgr()_1]] - code - gateway/tests/test_delegation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/mgr
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_test_delegation.py]]

## Top bridge nodes
- [[mgr()_1]] - degree 4, connects to 2 communities
