---
type: community
members: 20
---

# dashboard_endpoints.py

**Members:** 20 nodes

## Members
- [[dot-__init__()_218]] - code - gateway/web/dashboard_endpoints.py
- [[dot-push()_4]] - code - gateway/web/dashboard_endpoints.py
- [[Alert]] - code - gateway/web/dashboard_endpoints.py
- [[Alert counts by severity.]] - rationale - gateway/web/dashboard_endpoints.py
- [[AlertStore]] - code - gateway/web/dashboard_endpoints.py
- [[Dashboard API endpoints for proxy status, alerts, SSH hosts, and logs. These…]] - rationale - gateway/web/dashboard_endpoints.py
- [[Proxy statistics (requests allowedblockedflagged).]] - rationale - gateway/web/dashboard_endpoints.py
- [[Recent securityaudit log entries. Optional ``bot=`` query parameter restricts…]] - rationale - gateway/web/dashboard_endpoints.py
- [[SSH host connectivity status.]] - rationale - gateway/web/dashboard_endpoints.py
- [[Simple in-memory alert store. Thread-safe enough for single-process use.]] - rationale - gateway/web/dashboard_endpoints.py
- [[TCP connect to port 22 to check if host is reachable.]] - rationale - gateway/web/dashboard_endpoints.py
- [[_check_host()]] - code - gateway/web/dashboard_endpoints.py
- [[_tcp_check()]] - code - gateway/web/dashboard_endpoints.py
- [[alerts_summary()]] - code - gateway/web/dashboard_endpoints.py
- [[dashboard_endpoints.py]] - code - gateway/web/dashboard_endpoints.py
- [[get_9]] - code
- [[logs_recent()]] - code - gateway/web/dashboard_endpoints.py
- [[proxy_status()_1]] - code - gateway/web/dashboard_endpoints.py
- [[ssh_hosts()_1]] - code - gateway/web/dashboard_endpoints.py
- [[test_alert_store_push_and_summary()]] - code - gateway/tests/test_dashboard_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/dashboard_endpointspy
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_LogBuffer]]
- 3 edges to [[_COMMUNITY_test_dashboard_endpoints.py]]
- 1 edge to [[_COMMUNITY_BufferHandler]]
- 1 edge to [[_COMMUNITY_dot-_handle]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_test_web_api_coverage.py]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_fastapi]]

## Top bridge nodes
- [[dashboard_endpoints.py]] - degree 18, connects to 9 communities
- [[AlertStore]] - degree 8, connects to 3 communities
- [[_check_host()]] - degree 5, connects to 1 community
- [[test_alert_store_push_and_summary()]] - degree 2, connects to 1 community
