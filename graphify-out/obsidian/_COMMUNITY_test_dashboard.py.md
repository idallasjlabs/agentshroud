---
type: community
cohesion: 0.04
members: 66
---

# test_dashboard.py

**Cohesion:** 0.04 - loosely connected
**Members:** 66 nodes

## Members
- [[dot-test_scoped_ws_token_is_single_use()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_activity_accepts_scoped_token()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_activity_accepts_valid_token()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_approvals_accepts_valid_token()]] - code - gateway/tests/test_security_fixes.py
- [[Auth dependency that uses the app state config._3]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[AuthRequired_4]] - code - gateway/ingest_api/routes/dashboard.py
- [[Create a short-lived WebSocket-only token.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Dashboard HTML uses data attributes instead of onclick for approvals]] - rationale - gateway/tests/test_dashboard.py
- [[Fallback activity entries when tracker data is unavailableempty.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Fallback activity summary when tracker data is unavailableempty.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[GET dashboard includes Content-Security-Policy header]] - rationale - gateway/tests/test_dashboard.py
- [[GET dashboard without auth returns 403]] - rationale - gateway/tests/test_dashboard.py
- [[GET dashboardstats returns JSON stats]] - rationale - gateway/tests/test_dashboard.py
- [[GET dashboardstats without auth returns 401]] - rationale - gateway/tests/test_dashboard.py
- [[JSON stats for dashboard]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Load contributor logs from multiple directories with de-dup by filename.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Path_58]] - code - gateway/ingest_api/routes/dashboard.py
- [[Request_7]] - code - gateway/ingest_api/routes/dashboard.py
- [[Resolve contributor log directories (ordered, de-duplicated).]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Return a short-lived WS-only auth token for cookie-authenticated sessions.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Return collaborator data from the shared bot workspace volume.      Reads COLLAB]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Scoped WS token should be consumed after first use (single-use)]] - rationale - gateway/tests/test_security_fixes.py
- [[Serve the dashboard HTML (requires auth via query param or cookie)      On first]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Sync TestClient for WebSocket tests_1]] - rationale - gateway/tests/test_dashboard.py
- [[WS wsactivity accepts valid scoped WS token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsactivity should accept scoped ws_ token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsapprovals accepts valid scoped WS token]] - rationale - gateway/tests/test_security_fixes.py
- [[WebSocket wsactivity connects and authenticates via scoped WS token]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsactivity receives emitted events]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsactivity rejects bad auth during handshake]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsegress connects and emits egress snapshot.]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsegress should forward auth_ events for SOC visibility.]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsegress should forward privacy_ events.]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsegress should forward scanner_result events.]] - rationale - gateway/tests/test_dashboard.py
- [[_build_activity_entries_from_contributor_logs()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_build_activity_summary_from_contributor_logs()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_create_ws_token()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_load_contributor_logs()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_parse_collaborator_log_dirs()]] - code - gateway/ingest_api/routes/dashboard.py
- [[auth_dep()_4]] - code - gateway/ingest_api/routes/dashboard.py
- [[dashboard.py]] - code - gateway/ingest_api/routes/dashboard.py
- [[dashboard_stats()]] - code - gateway/ingest_api/routes/dashboard.py
- [[dashboard_ws_token()]] - code - gateway/ingest_api/routes/dashboard.py
- [[get_collaborators()]] - code - gateway/ingest_api/routes/dashboard.py
- [[serve_dashboard()]] - code - gateway/ingest_api/routes/dashboard.py
- [[sync_client()_1]] - code - gateway/tests/test_dashboard.py
- [[test_build_activity_entries_from_contributor_logs()]] - code - gateway/tests/test_dashboard.py
- [[test_build_activity_entries_from_contributor_logs_accepts_non_bullet_and_zulu_time()]] - code - gateway/tests/test_dashboard.py
- [[test_build_activity_summary_from_contributor_logs()]] - code - gateway/tests/test_dashboard.py
- [[test_build_activity_summary_from_contributor_logs_accepts_non_bullet_lines()]] - code - gateway/tests/test_dashboard.py
- [[test_collaborators_endpoint_reads_configured_contributor_sources()]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard.py]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard_has_csp_header()]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard_requires_auth()_1]] - code - gateway/tests/test_dashboard.py
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
TABLE source_file, type FROM #community/test_dashboardpy
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_make_event]]
- 7 edges to [[_COMMUNITY_activity_websocket]]
- 6 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 3 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_create_auth_dependency]]
- 2 edges to [[_COMMUNITY_ForwardRequest]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_test_e2e.py]]

## Top bridge nodes
- [[dashboard.py]] - degree 22, connects to 7 communities
- [[test_dashboard.py]] - degree 31, connects to 4 communities
- [[_create_ws_token()]] - degree 15, connects to 1 community
- [[dashboard_stats()]] - degree 5, connects to 1 community
- [[dashboard_ws_token()]] - degree 5, connects to 1 community
