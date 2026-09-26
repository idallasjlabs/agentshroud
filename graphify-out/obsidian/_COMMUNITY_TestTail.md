---
type: community
cohesion: 0.33
members: 7
---

# TestTail

**Cohesion:** 0.33 - loosely connected
**Members:** 7 nodes

## Members
- [[.get_integrity_status()]] - code - gateway/security/memory_integrity.py
- [[.get_recent_alerts()]] - code - gateway/security/memory_integrity.py
- [[.to_dict()_11]] - code - gateway/security/memory_integrity.py
- [[Any_48]] - code - gateway/security/memory_integrity.py
- [[Convert to dictionary for JSON serialization.]] - rationale - gateway/security/memory_integrity.py
- [[Get alerts from the last N hours.]] - rationale - gateway/security/memory_integrity.py
- [[Get current integrity monitoring status.]] - rationale - gateway/security/memory_integrity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestTail
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_ContainerEngine]]
- 1 edge to [[_COMMUNITY_falco_monitor.py]]

## Top bridge nodes
- [[.to_dict()_11]] - degree 4, connects to 2 communities
- [[Any_48]] - degree 5, connects to 1 community
- [[.get_integrity_status()]] - degree 4, connects to 1 community
- [[.get_recent_alerts()]] - degree 4, connects to 1 community