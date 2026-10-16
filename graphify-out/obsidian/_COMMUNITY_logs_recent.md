---
type: community
cohesion: 0.40
members: 5
---

# logs_recent

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[dot-recent()]] - code - gateway/web/dashboard_endpoints.py
- [[dot-tail()]] - code - gateway/web/dashboard_endpoints.py
- [[Any_18]] - code - gateway/web/dashboard_endpoints.py
- [[Recent securityaudit log entries.      Optional ``bot=`` query parameter restr]] - rationale - gateway/web/dashboard_endpoints.py
- [[logs_recent()]] - code - gateway/web/dashboard_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/logs_recent
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_dashboard_endpoints.py]]
- 1 edge to [[_COMMUNITY_AlertStore]]
- 1 edge to [[_COMMUNITY_LogBuffer]]

## Top bridge nodes
- [[logs_recent()]] - degree 4, connects to 1 community
- [[Any_18]] - degree 3, connects to 1 community
- [[dot-tail()]] - degree 3, connects to 1 community
- [[dot-recent()]] - degree 2, connects to 1 community
