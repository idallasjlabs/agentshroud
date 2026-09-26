---
type: community
cohesion: 0.03
members: 102
---

# TestCollaboratorPromptClassifiers

**Cohesion:** 0.03 - loosely connected
**Members:** 102 nodes

## Members
- [[.test_scoped_ws_token_is_single_use()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ws_activity_accepts_scoped_token()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ws_activity_accepts_valid_token()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ws_approvals_accepts_valid_token()]] - code - gateway/tests/test_security_fixes.py
- [[3+ auth failures in 5 min escalates to critical]] - rationale - gateway/tests/test_event_bus.py
- [[Auth dependency that uses the app state config._1]] - rationale - gateway/ingest_api/routes/dashboard.py
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
- [[GET dashboard without auth returns 403]] - rationale - gateway/tests/test_dashboard.py
- [[GET dashboardstats returns JSON stats]] - rationale - gateway/tests/test_dashboard.py
- [[GET dashboardstats without auth returns 401]] - rationale - gateway/tests/test_dashboard.py
- [[Helper to create a GatewayEvent with current timestamp]] - rationale - gateway/ingest_api/event_bus.py
- [[JSON stats for dashboard]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Load contributor logs from multiple directories with de-dup by filename.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Multiple subscribers all receive the same event]] - rationale - gateway/tests/test_event_bus.py
- [[Path_2]] - code - gateway/ingest_api/routes/dashboard.py
- [[Recent events are returned in order]] - rationale - gateway/tests/test_event_bus.py
- [[Request_3]] - code - gateway/ingest_api/routes/dashboard.py
- [[Resolve contributor log directories (ordered, de-duplicated).]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Return a short-lived WS-only auth token for cookie-authenticated sessions.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Return collaborator data from the shared bot workspace volume.      Reads COLLAB]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Scoped WS token should be consumed after first use (single-use)]] - rationale - gateway/tests/test_security_fixes.py
- [[Serve the dashboard HTML (requires auth via query param or cookie)      On first]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Stats track event counts]] - rationale - gateway/tests/test_event_bus.py
- [[Subscriber receives emitted events]] - rationale - gateway/tests/test_event_bus.py
- [[Sync TestClient for WebSocket tests]] - rationale - gateway/tests/test_dashboard.py
- [[Unsubscribed callback stops receiving events]] - rationale - gateway/tests/test_event_bus.py
- [[Validate a WebSocket token (single-use, time-limited).]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[WS wsactivity accepts valid scoped WS token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsactivity should accept scoped ws_ token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsapprovals accepts valid scoped WS token]] - rationale - gateway/tests/test_security_fixes.py
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
TABLE source_file, type FROM #community/TestCollaboratorPromptClassifiers
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_SSHProxy]]
- 10 edges to [[_COMMUNITY_test_telegram_proxy_outbound.py]]
- 8 edges to [[_COMMUNITY_A2APolicyEngine]]
- 5 edges to [[_COMMUNITY_socrouter.py]]
- 5 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 4 edges to [[_COMMUNITY_ReportStore]]
- 3 edges to [[_COMMUNITY_TestOriginAwareAuthorization]]
- 2 edges to [[_COMMUNITY_RateLimiter]]
- 2 edges to [[_COMMUNITY_Production Safety Checklist (SKILL)]]
- 2 edges to [[_COMMUNITY_Socrates — Dialogue Architect]]
- 1 edge to [[_COMMUNITY_InjectionSeverity]]
- 1 edge to [[_COMMUNITY_GitGuard]]
- 1 edge to [[_COMMUNITY_AgentShroud v0.9.0 — Human Interface Testing Gui]]
- 1 edge to [[_COMMUNITY_StdioConnection]]
- 1 edge to [[_COMMUNITY_TestPathIsolationManager]]
- 1 edge to [[_COMMUNITY_chatbotmain.py]]
- 1 edge to [[_COMMUNITY_EgressPolicy]]
- 1 edge to [[_COMMUNITY_AgentShroud v1.0.0 Fortress Release Announcement]]

## Top bridge nodes
- [[make_event()]] - degree 57, connects to 13 communities
- [[dashboard.py]] - degree 23, connects to 6 communities
- [[test_dashboard.py]] - degree 31, connects to 2 communities
- [[soc_report()]] - degree 10, connects to 2 communities
- [[_build_egress_live_snapshot()]] - degree 10, connects to 2 communities