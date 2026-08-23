---
type: community
cohesion: 0.04
members: 79
---

# Dashboard

**Cohesion:** 0.04 - loosely connected
**Members:** 79 nodes

## Members
- [[.to_dict()_13]] - code - gateway/security/soc_correlation.py
- [[Any_61]] - code - gateway/security/soc_correlation.py
- [[Auth dependency that uses the app state config._1]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[AuthRequired_2]] - code - gateway/ingest_api/routes/dashboard.py
- [[Build compact egress dashboard snapshot for websocketAPI clients.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Consolidated SOC report for dashboardSIEM pull workflows.]] - rationale - gateway/ingest_api/main.py
- [[CorrelationSummary]] - code - gateway/security/soc_correlation.py
- [[Create a short-lived WebSocket-only token.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Dashboard HTML uses data attributes instead of onclick for approvals]] - rationale - gateway/tests/test_dashboard.py
- [[Fallback activity entries when tracker data is unavailableempty.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Fallback activity summary when tracker data is unavailableempty.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[GET dashboard includes Content-Security-Policy header]] - rationale - gateway/tests/test_dashboard.py
- [[GET dashboard with valid cookie auth returns HTML.]] - rationale - gateway/tests/test_e2e.py
- [[GET dashboard without auth returns 403]] - rationale - gateway/tests/test_dashboard.py
- [[GET dashboardstats returns JSON stats]] - rationale - gateway/tests/test_dashboard.py
- [[GET dashboardstats without auth returns 401]] - rationale - gateway/tests/test_dashboard.py
- [[JSON stats for dashboard]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Load contributor logs from multiple directories with de-dup by filename.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Path_2]] - code - gateway/ingest_api/routes/dashboard.py
- [[Request_3]] - code - gateway/ingest_api/routes/dashboard.py
- [[Resolve contributor log directories (ordered, de-duplicated).]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Return a short-lived WS-only auth token for cookie-authenticated sessions.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Return collaborator data from the shared bot workspace volume.      Reads COLLAB]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Serve the dashboard HTML (requires auth via query param or cookie)      On first]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Sync TestClient for WebSocket tests]] - rationale - gateway/tests/test_dashboard.py
- [[Validate a WebSocket token (single-use, time-limited).]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[WebSocket_4]] - code - gateway/ingest_api/routes/dashboard.py
- [[WebSocket wsactivity connects and authenticates via scoped WS token]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsactivity receives emitted events]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsactivity rejects bad auth during handshake]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsegress connects and emits egress snapshot.]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsegress should forward auth_ events for SOC visibility.]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsegress should forward privacy_ events.]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsegress should forward scanner_result events.]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket for real-time activity feed]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[WebSocket stream specialized for egresssecurity dashboard updates.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[_build_activity_entries_from_contributor_logs()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_build_activity_summary_from_contributor_logs()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_build_egress_live_snapshot()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_create_ws_token()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_load_contributor_logs()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_parse_collaborator_log_dirs()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_renderCorrelation()]] - code - gateway/soc/static/soc.js
- [[_validate_ws_token()]] - code - gateway/ingest_api/routes/dashboard.py
- [[activity_websocket()]] - code - gateway/ingest_api/routes/dashboard.py
- [[auth_dep()_2]] - code - gateway/ingest_api/routes/dashboard.py
- [[build_correlation_summary()]] - code - gateway/security/soc_correlation.py
- [[dashboard.py]] - code - gateway/ingest_api/routes/dashboard.py
- [[dashboard_stats()]] - code - gateway/ingest_api/routes/dashboard.py
- [[dashboard_ws_token()]] - code - gateway/ingest_api/routes/dashboard.py
- [[egress_websocket()]] - code - gateway/ingest_api/routes/dashboard.py
- [[get_collaborators()]] - code - gateway/ingest_api/routes/dashboard.py
- [[serve_dashboard()]] - code - gateway/ingest_api/routes/dashboard.py
- [[soc_correlation.py]] - code - gateway/security/soc_correlation.py
- [[soc_report()]] - code - gateway/ingest_api/main.py
- [[sync_client()]] - code - gateway/tests/test_dashboard.py
- [[test_build_activity_entries_from_contributor_logs()]] - code - gateway/tests/test_dashboard.py
- [[test_build_activity_entries_from_contributor_logs_accepts_non_bullet_and_zulu_time()]] - code - gateway/tests/test_dashboard.py
- [[test_build_activity_summary_from_contributor_logs()]] - code - gateway/tests/test_dashboard.py
- [[test_build_activity_summary_from_contributor_logs_accepts_non_bullet_lines()]] - code - gateway/tests/test_dashboard.py
- [[test_build_egress_live_snapshot_enriches_pending_metrics()]] - code - gateway/tests/test_dashboard.py
- [[test_collaborators_endpoint_reads_configured_contributor_sources()]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard.py]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard_has_csp_header()]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard_requires_auth()]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard_returns_html()]] - code - gateway/tests/test_e2e.py
- [[test_dashboard_serves_html()]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard_stats_endpoint()]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard_stats_requires_auth()]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard_xss_prevention()]] - code - gateway/tests/test_dashboard.py
- [[test_load_contributor_logs_reads_multiple_dirs_and_dedupes()]] - code - gateway/tests/test_dashboard.py
- [[test_parse_collaborator_log_dirs_dedupes_and_preserves_order()]] - code - gateway/tests/test_dashboard.py
- [[test_ws_activity_connects()]] - code - gateway/tests/test_dashboard.py
- [[test_ws_activity_receives_events()]] - code - gateway/tests/test_dashboard.py
- [[test_ws_activity_requires_auth()]] - code - gateway/tests/test_dashboard.py
- [[test_ws_egress_connects_and_snapshot()]] - code - gateway/tests/test_dashboard.py
- [[test_ws_egress_receives_auth_event()]] - code - gateway/tests/test_dashboard.py
- [[test_ws_egress_receives_privacy_event()]] - code - gateway/tests/test_dashboard.py
- [[test_ws_egress_receives_scanner_event()]] - code - gateway/tests/test_dashboard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Dashboard
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Soc Egress Endpoints]]
- 11 edges to [[_COMMUNITY_Ingest API Main & Models]]
- 6 edges to [[_COMMUNITY_SOC Router (Collaborator Mgmt)]]
- 3 edges to [[_COMMUNITY_Auth]]
- 3 edges to [[_COMMUNITY_Security Fixes & SSH Write Endpoint]]
- 3 edges to [[_COMMUNITY_Soc (static)]]
- 2 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 2 edges to [[_COMMUNITY_Docs Accuracy]]
- 2 edges to [[_COMMUNITY_Security Fixes]]
- 1 edge to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 1 edge to [[_COMMUNITY_Migrate Cve Registry Ghsa (scripts)]]
- 1 edge to [[_COMMUNITY_Collaborator Greeter]]

## Top bridge nodes
- [[dashboard.py]] - degree 23, connects to 5 communities
- [[build_correlation_summary()]] - degree 14, connects to 5 communities
- [[test_dashboard.py]] - degree 31, connects to 2 communities
- [[_create_ws_token()]] - degree 15, connects to 2 communities
- [[soc_report()]] - degree 10, connects to 1 community