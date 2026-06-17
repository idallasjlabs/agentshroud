---
type: community
cohesion: 0.08
members: 29
---

# Module Group 166

**Cohesion:** 0.08 - loosely connected
**Members:** 29 nodes

## Members
- [[.__init__()_147]] - code - gateway/web/dashboard_endpoints.py
- [[.__init__()_148]] - code - gateway/web/dashboard_endpoints.py
- [[.summary()_1]] - code - gateway/web/dashboard_endpoints.py
- [[Alert counts by severity.]] - rationale - gateway/web/dashboard_endpoints.py
- [[AlertStore]] - code - gateway/web/dashboard_endpoints.py
- [[LogBuffer]] - code - gateway/web/dashboard_endpoints.py
- [[Ring buffer for recent logaudit entries.]] - rationale - gateway/web/dashboard_endpoints.py
- [[Simple in-memory alert store. Thread-safe enough for single-process use.]] - rationale - gateway/web/dashboard_endpoints.py
- [[When pipeline exists, stats should reflect its data.]] - rationale - gateway/tests/test_dashboard_endpoints.py
- [[alerts_summary()]] - code - gateway/web/dashboard_endpoints.py
- [[auth_headers()_1]] - code - gateway/tests/test_dashboard_endpoints.py
- [[tail parameter is clamped to 1-100.]] - rationale - gateway/tests/test_dashboard_endpoints.py
- [[test_alert_store_push_and_summary()]] - code - gateway/tests/test_dashboard_endpoints.py
- [[test_alerts_summary_empty()]] - code - gateway/tests/test_dashboard_endpoints.py
- [[test_alerts_summary_requires_auth()]] - code - gateway/tests/test_dashboard_endpoints.py
- [[test_alerts_summary_with_alerts()]] - code - gateway/tests/test_dashboard_endpoints.py
- [[test_dashboard_endpoints.py]] - code - gateway/tests/test_dashboard_endpoints.py
- [[test_log_buffer_ring()]] - code - gateway/tests/test_dashboard_endpoints.py
- [[test_log_buffer_tail()]] - code - gateway/tests/test_dashboard_endpoints.py
- [[test_logs_recent_requires_auth()]] - code - gateway/tests/test_dashboard_endpoints.py
- [[test_logs_recent_returns_entries()]] - code - gateway/tests/test_dashboard_endpoints.py
- [[test_logs_recent_tail_clamped()]] - code - gateway/tests/test_dashboard_endpoints.py
- [[test_logs_recent_tail_param()]] - code - gateway/tests/test_dashboard_endpoints.py
- [[test_proxy_status_includes_pipeline_stats()]] - code - gateway/tests/test_dashboard_endpoints.py
- [[test_proxy_status_requires_auth()]] - code - gateway/tests/test_dashboard_endpoints.py
- [[test_proxy_status_returns_stats()]] - code - gateway/tests/test_dashboard_endpoints.py
- [[test_ssh_hosts_online()]] - code - gateway/tests/test_dashboard_endpoints.py
- [[test_ssh_hosts_requires_auth()]] - code - gateway/tests/test_dashboard_endpoints.py
- [[test_ssh_hosts_returns_hosts()]] - code - gateway/tests/test_dashboard_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_166
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Module Group 304]]
- 3 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_Module Group 311]]

## Top bridge nodes
- [[AlertStore]] - degree 8, connects to 2 communities
- [[LogBuffer]] - degree 8, connects to 2 communities
- [[test_dashboard_endpoints.py]] - degree 20, connects to 1 community
- [[alerts_summary()]] - degree 3, connects to 1 community