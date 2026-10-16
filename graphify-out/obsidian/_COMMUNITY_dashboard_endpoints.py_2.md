---
type: community
cohesion: 0.29
members: 7
---

# dashboard_endpoints.py

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[dot-recent()]] - code - gateway/web/dashboard_endpoints.py
- [[dot-tail()]] - code - gateway/web/dashboard_endpoints.py
- [[Any_10]] - code - gateway/web/dashboard_endpoints.py
- [[SSH host connectivity status.]] - rationale - gateway/web/dashboard_endpoints.py
- [[TCP connect to port 22 to check if host is reachable.]] - rationale - gateway/web/dashboard_endpoints.py
- [[_check_host()]] - code - gateway/web/dashboard_endpoints.py
- [[ssh_hosts()_1]] - code - gateway/web/dashboard_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/dashboard_endpointspy
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_dashboard_endpoints.py]]
- 1 edge to [[_COMMUNITY_dashboard_endpoints.py_1]]
- 1 edge to [[_COMMUNITY_test_dashboard_endpoints.py]]

## Top bridge nodes
- [[dot-tail()]] - degree 3, connects to 2 communities
- [[_check_host()]] - degree 4, connects to 1 community
- [[ssh_hosts()_1]] - degree 4, connects to 1 community
- [[dot-recent()]] - degree 2, connects to 1 community
