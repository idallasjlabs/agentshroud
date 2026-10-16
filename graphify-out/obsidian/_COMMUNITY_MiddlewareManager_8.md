---
type: community
cohesion: 0.33
members: 7
---

# MiddlewareManager

**Cohesion:** 0.33 - loosely connected
**Members:** 7 nodes

## Members
- [[dot-get_integrity_status()]] - code - gateway/security/memory_integrity.py
- [[dot-get_recent_alerts()]] - code - gateway/security/memory_integrity.py
- [[dot-to_dict()_4]] - code - gateway/security/memory_integrity.py
- [[Any_8]] - code - gateway/security/memory_integrity.py
- [[Convert to dictionary for JSON serialization.]] - rationale - gateway/security/memory_integrity.py
- [[Get alerts from the last N hours.]] - rationale - gateway/security/memory_integrity.py
- [[Get current integrity monitoring status.]] - rationale - gateway/security/memory_integrity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MiddlewareManager
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_MiddlewareManager_4]]
- 1 edge to [[_COMMUNITY_MiddlewareManager_6]]

## Top bridge nodes
- [[dot-to_dict()_4]] - degree 4, connects to 2 communities
- [[Any_8]] - degree 5, connects to 1 community
- [[dot-get_integrity_status()]] - degree 4, connects to 1 community
- [[dot-get_recent_alerts()]] - degree 4, connects to 1 community
