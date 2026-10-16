---
type: community
cohesion: 0.50
members: 4
---

# soc_dashboard

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[Fallback minimal dashboard when template file is missing.]] - rationale - gateway/soc/router.py
- [[Serve the unified SOC web dashboard.]] - rationale - gateway/soc/router.py
- [[_minimal_dashboard_html()]] - code - gateway/soc/router.py
- [[soc_dashboard()]] - code - gateway/soc/router.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/soc_dashboard
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY__FakeRBAC]]

## Top bridge nodes
- [[soc_dashboard()]] - degree 4, connects to 2 communities
- [[_minimal_dashboard_html()]] - degree 3, connects to 1 community
