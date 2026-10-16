---
type: community
cohesion: 0.05
members: 53
---

# dashboard_endpoints.py

**Cohesion:** 0.05 - loosely connected
**Members:** 53 nodes

## Members
- [[dot-__init__()_103]] - code - gateway/web/dashboard_endpoints.py
- [[dot-__init__()_104]] - code - gateway/web/dashboard_endpoints.py
- [[dot-append()]] - code - gateway/web/dashboard_endpoints.py
- [[dot-emit()]] - code - gateway/web/dashboard_endpoints.py
- [[dot-push()_2]] - code - gateway/web/dashboard_endpoints.py
- [[dot-recent()]] - code - gateway/web/dashboard_endpoints.py
- [[dot-summary()]] - code - gateway/web/dashboard_endpoints.py
- [[dot-tail()]] - code - gateway/web/dashboard_endpoints.py
- [[Alert]] - code - gateway/web/dashboard_endpoints.py
- [[Alert counts by severity.]] - rationale - gateway/web/dashboard_endpoints.py
- [[AlertStore]] - code - gateway/web/dashboard_endpoints.py
- [[Any_33]] - code - gateway/web/dashboard_endpoints.py
- [[Attach BufferHandler to the root agentshroud logger.]] - rationale - gateway/web/dashboard_endpoints.py
- [[BufferHandler]] - code - gateway/web/dashboard_endpoints.py
- [[Live Dashboard Module Badge Icon]] - image - branding/icons/modules/live-dashboard-256x256.png
- [[LogBuffer]] - code - gateway/web/dashboard_endpoints.py
- [[LogRecord_2]] - code - gateway/web/dashboard_endpoints.py
- [[Logging handler that pushes records into the LogBuffer.]] - rationale - gateway/web/dashboard_endpoints.py
- [[Proxy statistics (requests allowedblockedflagged).]] - rationale - gateway/web/dashboard_endpoints.py
- [[Recent securityaudit log entries.      Optional ``bot=`` query parameter restr]] - rationale - gateway/web/dashboard_endpoints.py
- [[Ring buffer for recent logaudit entries.]] - rationale - gateway/web/dashboard_endpoints.py
- [[SSH host connectivity status.]] - rationale - gateway/web/dashboard_endpoints.py
- [[Simple in-memory alert store. Thread-safe enough for single-process use.]] - rationale - gateway/web/dashboard_endpoints.py
- [[TCP connect to port 22 to check if host is reachable.]] - rationale - gateway/web/dashboard_endpoints.py
- [[Test Dashboard Endpoints Suite]] - code - gateway/tests/test_dashboard_endpoints.py
- [[When pipeline exists, stats should reflect its data.]] - rationale - gateway/tests/test_dashboard_endpoints.py
- [[_check_host()]] - code - gateway/web/dashboard_endpoints.py
- [[_tcp_check()]] - code - gateway/web/dashboard_endpoints.py
- [[alerts_summary()]] - code - gateway/web/dashboard_endpoints.py
- [[auth_headers()_2]] - code - gateway/tests/test_dashboard_endpoints.py
- [[dashboard_endpoints.py]] - code - gateway/web/dashboard_endpoints.py
- [[install_log_handler()]] - code - gateway/web/dashboard_endpoints.py
- [[logs_recent()]] - code - gateway/web/dashboard_endpoints.py
- [[proxy_status()_1]] - code - gateway/web/dashboard_endpoints.py
- [[ssh_hosts()_1]] - code - gateway/web/dashboard_endpoints.py
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
TABLE source_file, type FROM #community/dashboard_endpointspy
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_ForwardRequest]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]

## Top bridge nodes
- [[dashboard_endpoints.py]] - degree 15, connects to 3 communities
- [[install_log_handler()]] - degree 5, connects to 2 communities
- [[test_dashboard_endpoints.py]] - degree 20, connects to 1 community
- [[Live Dashboard Module Badge Icon]] - degree 2, connects to 1 community
