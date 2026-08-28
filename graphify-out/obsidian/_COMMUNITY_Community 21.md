---
type: community
cohesion: 0.03
members: 121
---

# Community 21

**Cohesion:** 0.03 - loosely connected
**Members:** 121 nodes

## Members
- [[.__init__()_12]] - code - gateway/ingest_api/event_bus.py
- [[.emit()]] - code - gateway/ingest_api/event_bus.py
- [[.get_recent()]] - code - gateway/ingest_api/event_bus.py
- [[.get_stats()]] - code - gateway/ingest_api/event_bus.py
- [[.subscribe()]] - code - gateway/ingest_api/event_bus.py
- [[.test_scoped_ws_token_is_single_use()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ws_activity_accepts_scoped_token()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ws_activity_accepts_valid_token()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ws_approvals_accepts_valid_token()]] - code - gateway/tests/test_security_fixes.py
- [[.to_dict()]] - code - gateway/ingest_api/event_bus.py
- [[.unsubscribe()]] - code - gateway/ingest_api/event_bus.py
- [[3+ auth failures in 5 min escalates to critical]] - rationale - gateway/tests/test_event_bus.py
- [[3+ auth failures within 5 minutes escalates event severity to critical]] - concept - gateway/tests/test_event_bus.py
- [[A single gateway event]] - rationale - gateway/ingest_api/event_bus.py
- [[Any_6]] - code - gateway/ingest_api/event_bus.py
- [[Auth dependency that uses the app state config._1]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[AuthRequired_2]] - code - gateway/ingest_api/routes/dashboard.py
- [[Build compact egress dashboard snapshot for websocketAPI clients.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Consolidated SOC report for dashboardSIEM pull workflows.]] - rationale - gateway/ingest_api/main.py
- [[Create a short-lived WebSocket-only token.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Dashboard HTML uses data attributes instead of onclick for approvals]] - rationale - gateway/tests/test_dashboard.py
- [[Emit an event to all subscribers]] - rationale - gateway/ingest_api/event_bus.py
- [[Emitting with no subscribers doesn't raise]] - rationale - gateway/tests/test_event_bus.py
- [[EventBus]] - code - gateway/ingest_api/event_bus.py
- [[Events have type, timestamp, summary, details, severity]] - rationale - gateway/tests/test_event_bus.py
- [[Fallback activity entries when tracker data is unavailableempty.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Fallback activity summary when tracker data is unavailableempty.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[GET dashboard includes Content-Security-Policy header]] - rationale - gateway/tests/test_dashboard.py
- [[GET dashboard without auth returns 403]] - rationale - gateway/tests/test_dashboard.py
- [[GET dashboardstats returns JSON stats]] - rationale - gateway/tests/test_dashboard.py
- [[GET dashboardstats without auth returns 401]] - rationale - gateway/tests/test_dashboard.py
- [[GatewayEvent]] - code - gateway/ingest_api/event_bus.py
- [[Helper to create a GatewayEvent with current timestamp]] - rationale - gateway/ingest_api/event_bus.py
- [[JSON stats for dashboard]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Load contributor logs from multiple directories with de-dup by filename.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Multiple subscribers all receive the same event]] - rationale - gateway/tests/test_event_bus.py
- [[Path_2]] - code - gateway/ingest_api/routes/dashboard.py
- [[Recent events are returned in order]] - rationale - gateway/tests/test_event_bus.py
- [[Regression (SCRUM-61) apialerts used to call event_bus.publish(),     a metho]] - rationale - gateway/tests/test_alert_telegram_relay.py
- [[Request_4]] - code - gateway/ingest_api/routes/dashboard.py
- [[Resolve contributor log directories (ordered, de-duplicated).]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Return a short-lived WS-only auth token for cookie-authenticated sessions.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Return collaborator data from the shared bot workspace volume.      Reads COLLAB]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Scoped WS token should be consumed after first use (single-use)]] - rationale - gateway/tests/test_security_fixes.py
- [[Serve the dashboard HTML (requires auth via query param or cookie)      On first]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Simple in-process event bus with async support]] - rationale - gateway/ingest_api/event_bus.py
- [[Stats track event counts]] - rationale - gateway/tests/test_event_bus.py
- [[Subscribe to all events]] - rationale - gateway/ingest_api/event_bus.py
- [[Subscriber receives emitted events]] - rationale - gateway/tests/test_event_bus.py
- [[Sync TestClient for WebSocket tests]] - rationale - gateway/tests/test_dashboard.py
- [[Unsubscribe from events]] - rationale - gateway/ingest_api/event_bus.py
- [[Unsubscribed callback stops receiving events]] - rationale - gateway/tests/test_event_bus.py
- [[Validate a WebSocket token (single-use, time-limited).]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[WS wsactivity accepts valid scoped WS token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsactivity should accept scoped ws_ token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsapprovals accepts valid scoped WS token]] - rationale - gateway/tests/test_security_fixes.py
- [[WebSocket_4]] - code - gateway/ingest_api/routes/approval.py
- [[WebSocket_5]] - code - gateway/ingest_api/routes/dashboard.py
- [[WebSocket wsactivity connects and authenticates via scoped WS token]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsactivity receives emitted events]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsactivity rejects bad auth during handshake]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsegress connects and emits egress snapshot.]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsegress should forward auth_ events for SOC visibility.]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsegress should forward privacy_ events.]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket wsegress should forward scanner_result events.]] - rationale - gateway/tests/test_dashboard.py
- [[WebSocket endpoint for real-time approval notifications      Protocol     1. Cl]] - rationale - gateway/ingest_api/routes/approval.py
- [[WebSocket for real-time activity feed]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[WebSocket stream specialized for egresssecurity dashboard updates.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[_build_activity_entries_from_contributor_logs()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_build_activity_summary_from_contributor_logs()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_build_egress_live_snapshot()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_create_ws_token()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_load_contributor_logs()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_parse_collaborator_log_dirs()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_validate_ws_token()]] - code - gateway/ingest_api/routes/dashboard.py
- [[activity_websocket()]] - code - gateway/ingest_api/routes/dashboard.py
- [[approval_websocket()]] - code - gateway/ingest_api/routes/approval.py
- [[auth_dep()_2]] - code - gateway/ingest_api/routes/dashboard.py
- [[bus()]] - code - gateway/tests/test_event_bus.py
- [[dashboard.py]] - code - gateway/ingest_api/routes/dashboard.py
- [[dashboard_stats()]] - code - gateway/ingest_api/routes/dashboard.py
- [[dashboard_ws_token()]] - code - gateway/ingest_api/routes/dashboard.py
- [[egress_websocket()]] - code - gateway/ingest_api/routes/dashboard.py
- [[event_bus.py_1]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[get_collaborators()]] - code - gateway/ingest_api/routes/dashboard.py
- [[make_event()]] - code - gateway/ingest_api/event_bus.py
- [[serve_dashboard()]] - code - gateway/ingest_api/routes/dashboard.py
- [[soc_report()]] - code - gateway/ingest_api/main.py
- [[sync_client()]] - code - gateway/tests/test_dashboard.py
- [[test_api_alerts_endpoint_emits_bus_event()]] - code - gateway/tests/test_alert_telegram_relay.py
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
- [[test_dashboard_stats_endpoint()]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard_stats_requires_auth()]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard_xss_prevention()]] - code - gateway/tests/test_dashboard.py
- [[test_emit_no_subscribers_no_error()]] - code - gateway/tests/test_event_bus.py
- [[test_emit_to_multiple_subscribers()]] - code - gateway/tests/test_event_bus.py
- [[test_event_bus.py]] - code - gateway/tests/test_event_bus.py
- [[test_event_has_required_fields()]] - code - gateway/tests/test_event_bus.py
- [[test_get_recent()]] - code - gateway/tests/test_event_bus.py
- [[test_get_stats()_1]] - code - gateway/tests/test_event_bus.py
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
TABLE source_file, type FROM #community/Community_21
SORT file.name ASC
```

## Connections to other communities
- 31 edges to [[_COMMUNITY_Ingest API & Approval Routes]]
- 8 edges to [[_COMMUNITY_Community 124]]
- 5 edges to [[_COMMUNITY_SOC Collaborators]]
- 5 edges to [[_COMMUNITY_Community 15]]
- 4 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 4 edges to [[_COMMUNITY_Community 20]]
- 3 edges to [[_COMMUNITY_Community 26]]
- 3 edges to [[_COMMUNITY_Community 65]]
- 3 edges to [[_COMMUNITY_Community 197]]
- 2 edges to [[_COMMUNITY_Middleware & Lifespan]]
- 2 edges to [[_COMMUNITY_Community 159]]
- 2 edges to [[_COMMUNITY_Community 78]]
- 1 edge to [[_COMMUNITY_RBAC & SOC Realtime]]
- 1 edge to [[_COMMUNITY_Community 39]]
- 1 edge to [[_COMMUNITY_Community 473]]
- 1 edge to [[_COMMUNITY_Community 49]]
- 1 edge to [[_COMMUNITY_Community 70]]
- 1 edge to [[_COMMUNITY_Community 420]]
- 1 edge to [[_COMMUNITY_Community 884]]
- 1 edge to [[_COMMUNITY_Community 85]]

## Top bridge nodes
- [[make_event()]] - degree 57, connects to 12 communities
- [[EventBus]] - degree 25, connects to 6 communities
- [[dashboard.py]] - degree 23, connects to 4 communities
- [[test_dashboard.py]] - degree 31, connects to 2 communities
- [[soc_report()]] - degree 10, connects to 2 communities