---
type: community
cohesion: 0.15
members: 16
---

# dashboard_endpoints.py

**Cohesion:** 0.15 - loosely connected
**Members:** 16 nodes

## Members
- [[dot-append()_1]] - code - gateway/web/dashboard_endpoints.py
- [[dot-emit()_1]] - code - gateway/web/dashboard_endpoints.py
- [[dot-push()_4]] - code - gateway/web/dashboard_endpoints.py
- [[Alert]] - code - gateway/web/dashboard_endpoints.py
- [[BufferHandler]] - code - gateway/web/dashboard_endpoints.py
- [[Live Dashboard Module Badge Icon]] - image - branding/icons/modules/live-dashboard-256x256.png
- [[LogRecord_1]] - code - gateway/web/dashboard_endpoints.py
- [[Logging handler that pushes records into the LogBuffer.]] - rationale - gateway/web/dashboard_endpoints.py
- [[Proxy statistics (requests allowedblockedflagged).]] - rationale - gateway/web/dashboard_endpoints.py
- [[SSH host connectivity status.]] - rationale - gateway/web/dashboard_endpoints.py
- [[TCP connect to port 22 to check if host is reachable.]] - rationale - gateway/web/dashboard_endpoints.py
- [[_check_host()]] - code - gateway/web/dashboard_endpoints.py
- [[_tcp_check()]] - code - gateway/web/dashboard_endpoints.py
- [[dashboard_endpoints.py]] - code - gateway/web/dashboard_endpoints.py
- [[proxy_status()_1]] - code - gateway/web/dashboard_endpoints.py
- [[ssh_hosts()_1]] - code - gateway/web/dashboard_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/dashboard_endpointspy
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_AlertStore]]
- 3 edges to [[_COMMUNITY_logs_recent]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_LogBuffer]]
- 1 edge to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]]

## Top bridge nodes
- [[dashboard_endpoints.py]] - degree 15, connects to 6 communities
- [[dot-append()_1]] - degree 5, connects to 2 communities
- [[BufferHandler]] - degree 4, connects to 1 community
- [[_check_host()]] - degree 4, connects to 1 community
- [[dot-push()_4]] - degree 3, connects to 1 community
