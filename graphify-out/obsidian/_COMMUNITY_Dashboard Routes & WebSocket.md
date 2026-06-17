---
type: community
cohesion: 0.03
members: 95
---

# Dashboard Routes & WebSocket

**Cohesion:** 0.03 - loosely connected
**Members:** 95 nodes

## Members
- [[.test_scoped_ws_token_is_single_use()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ws_activity_accepts_scoped_token()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ws_activity_accepts_valid_token()]] - code - gateway/tests/test_security_fixes.py
- [[3+ auth failures in 5 min escalates to critical]] - rationale - gateway/tests/test_event_bus.py
- [[AuthRequired_2]] - code - gateway/ingest_api/routes/dashboard.py
- [[Build compact egress dashboard snapshot for websocketAPI clients.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Consolidated SOC report for dashboardSIEM pull workflows.]] - rationale - gateway/ingest_api/main.py
- [[Create a short-lived WebSocket-only token.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Dashboard HTML uses data attributes instead of onclick for approvals]] - rationale - gateway/tests/test_dashboard.py
- [[Emitting with no subscribers doesn't raise]] - rationale - gateway/tests/test_event_bus.py
- [[Events have type, timestamp, summary, details, severity]] - rationale - gateway/tests/test_event_bus.py
- [[Fallback activity entries when tracker data is unavailableempty.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Fallback activity summary when tracker data is unavailableempty.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[GET dashboard includes Content-Security-Policy header]] - rationale - gateway/tests/test_dashboard.py
- [[GET dashboard with valid cookie serves HTML]] - rationale - gateway/tests/test_dashboard.py
- [[GET dashboard without auth returns 403]] - rationale - gateway/tests/test_dashboard.py
- [[GET dashboardstats returns JSON stats]] - rationale - gateway/tests/test_dashboard.py
- [[GET dashboardstats without auth returns 401]] - rationale - gateway/tests/test_dashboard.py
- [[Helper to create a GatewayEvent with current timestamp]] - rationale - gateway/ingest_api/event_bus.py
- [[JSON stats for dashboard]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Load contributor logs from multiple directories with de-dup by filename.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Multiple subscribers all receive the same event]] - rationale - gateway/tests/test_event_bus.py
- [[Path_2]] - code - gateway/ingest_api/routes/dashboard.py
- [[Recent events are returned in order]] - rationale - gateway/tests/test_event_bus.py
- [[Request_2]] - code - gateway/ingest_api/routes/dashboard.py
- [[Resolve contributor log directories (ordered, de-duplicated).]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Return a short-lived WS-only auth token for cookie-authenticated sessions.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Return collaborator data from the shared bot workspace volume.      Reads COLLAB]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Scoped WS token should be consumed after first use (single-use)]] - rationale - gateway/tests/test_security_fixes.py
- [[Serve the dashboard HTML (requires auth via query param or cookie)      On first]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Stats track event counts]] - rationale - gateway/tests/test_event_bus.py
- [[Subscriber receives emitted events]] - rationale - gateway/tests/test_event_bus.py
- [[Sync TestClient for WebSocket tests]] - rationale - gateway/tests/test_dashboard.py
- [[Unsubscribed callback stops receiving events]] - rationale - gateway/tests/test_event_bus.py
- [[WS wsactivity accepts valid scoped WS token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsactivity should accept scoped ws_ token]] - rationale - gateway/tests/test_security_fixes.py
- [[WebSocket_3]] - code - gateway/ingest_api/routes/approval.py
- [[WebSocket_4]] - code - gateway/ingest_api/routes/dashboard.py
- [[WebSocket wsactivity connects and authenticates via scoped WS token]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsactivity receives emitted events]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsactivity rejects bad auth during handshake]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsegress connects and emits egress snapshot.]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsegress should forward auth_ events for SOC visibility.]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsegress should forward privacy_ events.]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsegress should forward scanner_result events.]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket endpoint for real-time approval notifications      Protocol     1. Cl]] - rationale - gateway/ingest_api/routes/approval.py
- [[WebSocket stream specialized for egresssecurity dashboard updates.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[_build_activity_entries_from_contributor_logs()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_build_activity_summary_from_contributor_logs()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_build_egress_live_snapshot()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_create_ws_token()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_load_contributor_logs()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_parse_collaborator_log_dirs()]] - code - gateway/ingest_api/routes/dashboard.py
- [[approval_websocket()]] - code - gateway/ingest_api/routes/approval.py
- [[bus()]] - code - gateway/tests/test_event_bus.py
- [[dashboard_stats()]] - code - gateway/ingest_api/routes/dashboard.py
- [[dashboard_ws_token()]] - code - gateway/ingest_api/routes/dashboard.py
- [[egress_websocket()]] - code - gateway/ingest_api/routes/dashboard.py
- [[get_collaborators()]] - code - gateway/ingest_api/routes/dashboard.py
- [[make_event()]] - code - gateway/ingest_api/event_bus.py
- [[serve_dashboard()]] - code - gateway/ingest_api/routes/dashboard.py
- [[soc_report()]] - code - gateway/ingest_api/main.py
- [[sync_client()]] - code - gateway/tests/test_dashboard.py
- [[test_async_subscriber()]] - code - gateway/tests/test_event_bus.py
- [[test_auth_failure_escalation()]] - code - gateway/tests/test_event_bus.py
- [[test_build_activity_entries_from_contributor_logs()]] - code - gateway/tests/test_dashboard.py
- [[test_build_activity_entries_from_contributor_logs_accepts_non_bullet_and_zulu_time()]] - code - gateway/tests/test_dashboard.py
- [[test_build_activity_summary_from_contributor_logs()]] - code - gateway/tests/test_dashboard.py
- [[test_build_activity_summary_from_contributor_logs_accepts_non_bullet_lines()]] - code - gateway/tests/test_dashboard.py
- [[test_build_egress_live_snapshot_enriches_pending_metrics()]] - code - gateway/tests/test_dashboard.py
- [[test_collaborators_endpoint_reads_configured_contributor_sources()]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard.py]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard_has_csp_header()]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard_requires_auth()]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard_serves_html()]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard_stats_endpoint()]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard_stats_requires_auth()]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard_xss_prevention()]] - code - gateway/tests/test_dashboard.py
- [[test_emit_no_subscribers_no_error()]] - code - gateway/tests/test_event_bus.py
- [[test_emit_to_multiple_subscribers()]] - code - gateway/tests/test_event_bus.py
- [[test_event_bus.py]] - code - gateway/tests/test_event_bus.py
- [[test_event_has_required_fields()]] - code - gateway/tests/test_event_bus.py
- [[test_get_recent()]] - code - gateway/tests/test_event_bus.py
- [[test_get_stats()]] - code - gateway/tests/test_event_bus.py
- [[test_load_contributor_logs_reads_multiple_dirs_and_dedupes()]] - code - gateway/tests/test_dashboard.py
- [[test_parse_collaborator_log_dirs_dedupes_and_preserves_order()]] - code - gateway/tests/test_dashboard.py
- [[test_subscribe_receive_events()]] - code - gateway/tests/test_event_bus.py
- [[test_unsubscribe_stops_events()]] - code - gateway/tests/test_event_bus.py
- [[test_ws_activity_connects()]] - code - gateway/tests/test_dashboard.py
- [[test_ws_activity_receives_events()]] - code - gateway/tests/test_dashboard.py
- [[test_ws_activity_requires_auth()]] - code - gateway/tests/test_dashboard.py
- [[test_ws_egress_connects_and_snapshot()]] - code - gateway/tests/test_dashboard.py
- [[test_ws_egress_receives_auth_event()]] - code - gateway/tests/test_dashboard.py
- [[test_ws_egress_receives_privacy_event()]] - code - gateway/tests/test_dashboard.py
- [[test_ws_egress_receives_scanner_event()]] - code - gateway/tests/test_dashboard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Dashboard_Routes__WebSocket
SORT file.name ASC
```

## Connections to other communities
- 38 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 4 edges to [[_COMMUNITY_SOC Router & Correlation]]
- 3 edges to [[_COMMUNITY_Module Group 171]]
- 3 edges to [[_COMMUNITY_Module Group 132]]
- 2 edges to [[_COMMUNITY_Module Group 418]]
- 2 edges to [[_COMMUNITY_Module Group 364]]
- 2 edges to [[_COMMUNITY_Module Group 195]]
- 2 edges to [[_COMMUNITY_Module Group 334]]
- 2 edges to [[_COMMUNITY_Module Group 71]]
- 1 edge to [[_COMMUNITY_Module Group 348]]
- 1 edge to [[_COMMUNITY_MCP Inspector & Audit]]
- 1 edge to [[_COMMUNITY_Module Group 205]]
- 1 edge to [[_COMMUNITY_Module Group 208]]
- 1 edge to [[_COMMUNITY_Module Group 160]]
- 1 edge to [[_COMMUNITY_Module Group 200]]
- 1 edge to [[_COMMUNITY_Module Group 522]]
- 1 edge to [[_COMMUNITY_Module Group 240]]
- 1 edge to [[_COMMUNITY_Module Group 311]]
- 1 edge to [[_COMMUNITY_Module Group 337]]

## Top bridge nodes
- [[make_event()]] - degree 51, connects to 15 communities
- [[_create_ws_token()]] - degree 14, connects to 2 communities
- [[_build_egress_live_snapshot()]] - degree 10, connects to 2 communities
- [[soc_report()]] - degree 9, connects to 2 communities
- [[dashboard_ws_token()]] - degree 5, connects to 2 communities