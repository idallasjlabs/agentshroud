---
type: community
cohesion: 0.10
members: 22
---

# test_dashboard_endpoints.py

**Cohesion:** 0.10 - loosely connected
**Members:** 22 nodes

## Members
- [[dot-__init__()_139]] - code - gateway/web/dashboard_endpoints.py
- [[LogBuffer]] - code - gateway/web/dashboard_endpoints.py
- [[Ring buffer for recent logaudit entries.]] - rationale - gateway/web/dashboard_endpoints.py
- [[When pipeline exists, stats should reflect its data.]] - rationale - gateway/tests/test_dashboard_endpoints.py
- [[auth_headers()_4]] - code - gateway/tests/test_dashboard_endpoints.py
- [[tail parameter is clamped to 1-100.]] - rationale - gateway/tests/test_dashboard_endpoints.py
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
TABLE source_file, type FROM #community/test_dashboard_endpointspy
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_dashboard_endpoints.py_1]]
- 2 edges to [[_COMMUNITY_dashboard_endpoints.py]]
- 1 edge to [[_COMMUNITY_dashboard_endpoints.py_2]]
- 1 edge to [[_COMMUNITY_ForwardRequest]]

## Top bridge nodes
- [[test_dashboard_endpoints.py]] - degree 20, connects to 2 communities
- [[LogBuffer]] - degree 8, connects to 2 communities
