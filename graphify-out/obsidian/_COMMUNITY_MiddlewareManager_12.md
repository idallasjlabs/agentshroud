---
type: community
cohesion: 1.00
members: 2
---

# MiddlewareManager

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[dot-test_memory_write_validation()]] - code - gateway/tests/test_memory_lifecycle.py
- [[Test validation before writing to memory files.]] - rationale - gateway/tests/test_memory_lifecycle.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MiddlewareManager
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_MiddlewareManager_4]]

## Top bridge nodes
- [[dot-test_memory_write_validation()]] - degree 2, connects to 1 community
