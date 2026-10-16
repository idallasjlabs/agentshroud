---
type: community
cohesion: 0.67
members: 3
---

# management.py

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[Serve the main management dashboard.]] - rationale - gateway/web/management.py
- [[dashboard()]] - code - gateway/web/management.py
- [[dashboard.html (Control Center Template)]] - code - gateway/web/templates/dashboard.html

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/managementpy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_KeyRotationManager]]

## Top bridge nodes
- [[dashboard()]] - degree 4, connects to 2 communities
