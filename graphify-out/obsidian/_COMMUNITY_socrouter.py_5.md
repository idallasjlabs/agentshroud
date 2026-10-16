---
type: community
cohesion: 1.00
members: 2
---

# soc/router.py

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[dot-is_group_admin()_1]] - code - gateway/soc/auth.py
- [[Check group admin status via TeamsConfig if available.]] - rationale - gateway/soc/auth.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/soc/routerpy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_socrouter.py]]

## Top bridge nodes
- [[dot-is_group_admin()_1]] - degree 2, connects to 1 community
