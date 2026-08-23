---
type: community
cohesion: 0.05
members: 53
---

# Dashboard Endpoints (web)

**Cohesion:** 0.05 - loosely connected
**Members:** 53 nodes

## Members
- [[.__init__()_197]] - code - gateway/web/dashboard_endpoints.py
- [[.__init__()_198]] - code - gateway/web/dashboard_endpoints.py
- [[.append()_1]] - code - gateway/web/dashboard_endpoints.py
- [[.emit()_1]] - code - gateway/web/dashboard_endpoints.py
- [[.push()_4]] - code - gateway/web/dashboard_endpoints.py
- [[.recent()]] - code - gateway/web/dashboard_endpoints.py
- [[.summary()_1]] - code - gateway/web/dashboard_endpoints.py
- [[.tail()]] - code - gateway/web/dashboard_endpoints.py
- [[Alert]] - code - gateway/web/dashboard_endpoints.py
- [[Alert counts by severity.]] - rationale - gateway/web/dashboard_endpoints.py
- [[AlertStore]] - code - gateway/web/dashboard_endpoints.py
- [[Any_74]] - code - gateway/web/dashboard_endpoints.py
- [[BufferHandler]] - code - gateway/web/dashboard_endpoints.py
- [[HTTPAuthorizationCredentials_1]] - code - gateway/web/api.py
- [[LogBuffer]] - code - gateway/web/dashboard_endpoints.py
- [[LogRecord_2]] - code - gateway/web/dashboard_endpoints.py
- [[Logging handler that pushes records into the LogBuffer.]] - rationale - gateway/web/dashboard_endpoints.py
- [[Proxy statistics (requests allowedblockedflagged).]] - rationale - gateway/web/dashboard_endpoints.py
- [[Recent securityaudit log entries.      Optional ``bot=`` query parameter restr]] - rationale - gateway/web/dashboard_endpoints.py
- [[Require valid Bearer token for all management endpoints.]] - rationale - gateway/web/api.py
- [[Ring buffer for recent logaudit entries.]] - rationale - gateway/web/dashboard_endpoints.py
- [[SSH host connectivity status.]] - rationale - gateway/web/dashboard_endpoints.py
- [[Simple in-memory alert store. Thread-safe enough for single-process use.]] - rationale - gateway/web/dashboard_endpoints.py
- [[TCP connect to port 22 to check if host is reachable.]] - rationale - gateway/web/dashboard_endpoints.py
- [[Test Dashboard Endpoints Suite]] - code - gateway/tests/test_dashboard_endpoints.py
- [[When pipeline exists, stats should reflect its data.]] - rationale - gateway/tests/test_dashboard_endpoints.py
- [[_check_host()]] - code - gateway/web/dashboard_endpoints.py
- [[_tcp_check()]] - code - gateway/web/dashboard_endpoints.py
- [[alerts_summary()]] - code - gateway/web/dashboard_endpoints.py
- [[auth_headers()_1]] - code - gateway/tests/test_dashboard_endpoints.py
- [[dashboard_endpoints.py]] - code - gateway/web/dashboard_endpoints.py
- [[logs_recent()]] - code - gateway/web/dashboard_endpoints.py
- [[proxy_status()_1]] - code - gateway/web/dashboard_endpoints.py
- [[require_auth()_1]] - code - gateway/web/api.py
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
TABLE source_file, type FROM #community/Dashboard_Endpoints_web
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 3 edges to [[_COMMUNITY_Api (web)]]
- 3 edges to [[_COMMUNITY_Web Api Coverage]]
- 2 edges to [[_COMMUNITY_Citation Verifier]]
- 1 edge to [[_COMMUNITY_Auth]]
- 1 edge to [[_COMMUNITY_Config]]
- 1 edge to [[_COMMUNITY_Ingest API Main & Models]]
- 1 edge to [[_COMMUNITY_Collaborator Greeter]]
- 1 edge to [[_COMMUNITY_Intel Endpoint]]
- 1 edge to [[_COMMUNITY_Key Rotation]]
- 1 edge to [[_COMMUNITY_Killswitch Monitor & Observatory Mode]]
- 1 edge to [[_COMMUNITY_Runtime Engines]]
- 1 edge to [[_COMMUNITY_Skill Guard]]
- 1 edge to [[_COMMUNITY_Skills Manifest Sync]]
- 1 edge to [[_COMMUNITY_Management (web)]]
- 1 edge to [[_COMMUNITY_Icon 64x64 (app)]]

## Top bridge nodes
- [[require_auth()_1]] - degree 16, connects to 11 communities
- [[dashboard_endpoints.py]] - degree 16, connects to 4 communities
- [[HTTPAuthorizationCredentials_1]] - degree 4, connects to 2 communities
- [[test_dashboard_endpoints.py]] - degree 20, connects to 1 community
- [[BufferHandler]] - degree 4, connects to 1 community