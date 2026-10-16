---
type: community
cohesion: 0.25
members: 8
---

# AlertStore

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[dot-__init__()_25]] - code - gateway/web/dashboard_endpoints.py
- [[dot-summary()_1]] - code - gateway/web/dashboard_endpoints.py
- [[Alert counts by severity.]] - rationale - gateway/web/dashboard_endpoints.py
- [[AlertStore]] - code - gateway/web/dashboard_endpoints.py
- [[Simple in-memory alert store. Thread-safe enough for single-process use.]] - rationale - gateway/web/dashboard_endpoints.py
- [[Test Dashboard Endpoints Suite]] - code - gateway/tests/test_dashboard_endpoints.py
- [[alerts_summary()]] - code - gateway/web/dashboard_endpoints.py
- [[test_alert_store_push_and_summary()]] - code - gateway/tests/test_dashboard_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AlertStore
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_dashboard_endpoints.py]]
- 2 edges to [[_COMMUNITY_test_dashboard_endpoints.py]]
- 1 edge to [[_COMMUNITY_logs_recent]]

## Top bridge nodes
- [[AlertStore]] - degree 9, connects to 3 communities
- [[alerts_summary()]] - degree 3, connects to 1 community
- [[test_alert_store_push_and_summary()]] - degree 2, connects to 1 community
