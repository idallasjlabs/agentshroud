---
type: community
cohesion: 0.03
members: 78
---

# Soc Egress Endpoints

**Cohesion:** 0.03 - loosely connected
**Members:** 78 nodes

## Members
- [[.emit()]] - code - gateway/ingest_api/event_bus.py
- [[.get_recent()]] - code - gateway/ingest_api/event_bus.py
- [[.get_stats()]] - code - gateway/ingest_api/event_bus.py
- [[.to_dict()]] - code - gateway/ingest_api/event_bus.py
- [[3+ auth failures in 5 min escalates to critical]] - rationale - gateway/tests/test_event_bus.py
- [[A single gateway event]] - rationale - gateway/ingest_api/event_bus.py
- [[Any_6]] - code - gateway/ingest_api/event_bus.py
- [[ApprovalDecision_1]] - code - gateway/ingest_api/routes/approval.py
- [[ApprovalDecision]] - code - gateway/ingest_api/models.py
- [[ApprovalRequest_4]] - code - gateway/ingest_api/routes/approval.py
- [[Approve or reject a pending action      Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Auth dependency that uses the app state config.]] - rationale - gateway/ingest_api/routes/approval.py
- [[AuthRequired_1]] - code - gateway/ingest_api/routes/approval.py
- [[Emit an event to all subscribers]] - rationale - gateway/ingest_api/event_bus.py
- [[Emitting with no subscribers doesn't raise]] - rationale - gateway/tests/test_event_bus.py
- [[Events have type, timestamp, summary, details, severity]] - rationale - gateway/tests/test_event_bus.py
- [[GatewayEvent]] - code - gateway/ingest_api/event_bus.py
- [[Helper to create a GatewayEvent with current timestamp]] - rationale - gateway/ingest_api/event_bus.py
- [[Limit param caps the number of returned items.]] - rationale - gateway/tests/test_soc_egress_endpoints.py
- [[List all pending approval requests      Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Multiple subscribers all receive the same event]] - rationale - gateway/tests/test_event_bus.py
- [[Recent events are returned in order]] - rationale - gateway/tests/test_event_bus.py
- [[Request_2]] - code - gateway/ingest_api/routes/approval.py
- [[Returns empty result when scanner_result_history is empty.]] - rationale - gateway/tests/test_soc_egress_endpoints.py
- [[Returns scanner events from app_state.scanner_result_history.]] - rationale - gateway/tests/test_soc_egress_endpoints.py
- [[Stats track event counts]] - rationale - gateway/tests/test_event_bus.py
- [[Status query param filters by summary.status.]] - rationale - gateway/tests/test_soc_egress_endpoints.py
- [[Submit an action for human approval      Called by agents when attempting sensit]] - rationale - gateway/ingest_api/routes/approval.py
- [[Subscriber receives emitted events]] - rationale - gateway/tests/test_event_bus.py
- [[Unsubscribed callback stops receiving events]] - rationale - gateway/tests/test_event_bus.py
- [[User's decision on a pending approval request]] - rationale - gateway/ingest_api/models.py
- [[WebSocket_3]] - code - gateway/ingest_api/routes/approval.py
- [[WebSocket endpoint for real-time approval notifications      Protocol     1. Cl]] - rationale - gateway/ingest_api/routes/approval.py
- [[app_state]] - code - gateway/ingest_api/main.py
- [[approval.py]] - code - gateway/ingest_api/routes/approval.py
- [[approval_websocket()]] - code - gateway/ingest_api/routes/approval.py
- [[auth_dep()_1]] - code - gateway/ingest_api/routes/approval.py
- [[bus()]] - code - gateway/tests/test_event_bus.py
- [[decide_approval()]] - code - gateway/ingest_api/routes/approval.py
- [[event_bus.py]] - code - gateway/ingest_api/event_bus.py
- [[event_bus.py_1]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[list_pending_approvals()]] - code - gateway/ingest_api/routes/approval.py
- [[make_event()]] - code - gateway/ingest_api/event_bus.py
- [[submit_approval_request()]] - code - gateway/ingest_api/routes/approval.py
- [[test_async_subscriber()]] - code - gateway/tests/test_event_bus.py
- [[test_auth_failure_escalation()]] - code - gateway/tests/test_event_bus.py
- [[test_emit_no_subscribers_no_error()]] - code - gateway/tests/test_event_bus.py
- [[test_emit_to_multiple_subscribers()]] - code - gateway/tests/test_event_bus.py
- [[test_event_bus.py]] - code - gateway/tests/test_event_bus.py
- [[test_event_has_required_fields()]] - code - gateway/tests/test_event_bus.py
- [[test_get_recent()]] - code - gateway/tests/test_event_bus.py
- [[test_get_stats()_1]] - code - gateway/tests/test_event_bus.py
- [[test_manage_egress_add_remove_rule_and_risk()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_egress_emergency_toggle()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_egress_log_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_egress_pending_endpoint_includes_summary()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_egress_rules_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_privacy_policy_and_audit_endpoints()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_scan_all_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_scanners_history_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_scanners_summary_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_soc_correlation_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_soc_events_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_soc_export_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_soc_export_invalid_format()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_soc_report_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_soc_report_falls_back_to_contributor_logs()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_outbound_quarantine_endpoints()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_quarantine_list_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_quarantine_release_and_discard_flow()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_quarantine_summary_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_soc_egress_endpoints.py]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_soc_scanners_recent_empty()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_soc_scanners_recent_limit()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_soc_scanners_recent_returns_history()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_soc_scanners_recent_status_filter()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_subscribe_receive_events()]] - code - gateway/tests/test_event_bus.py
- [[test_unsubscribe_stops_events()]] - code - gateway/tests/test_event_bus.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Soc_Egress_Endpoints
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_Ingest API Main & Models]]
- 11 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 11 edges to [[_COMMUNITY_Dashboard]]
- 4 edges to [[_COMMUNITY_Egress Approval (security)]]
- 3 edges to [[_COMMUNITY_Auth]]
- 3 edges to [[_COMMUNITY_Forward (routes)]]
- 3 edges to [[_COMMUNITY_Alert Telegram Relay]]
- 2 edges to [[_COMMUNITY_Egress Filter (security)]]
- 2 edges to [[_COMMUNITY_Aiosqlite (05 - Dependencies)]]
- 2 edges to [[_COMMUNITY_Main Simple]]
- 1 edge to [[_COMMUNITY_Router (soc)]]
- 1 edge to [[_COMMUNITY_Mcp Permissions]]
- 1 edge to [[_COMMUNITY_Mcp Proxy (proxy)]]
- 1 edge to [[_COMMUNITY_Group Config & Collaborator Responses]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Core]]
- 1 edge to [[_COMMUNITY_Agentshroud.yaml (03 - Configuration)]]
- 1 edge to [[_COMMUNITY_Approval Queue]]
- 1 edge to [[_COMMUNITY_Queue (approval_queue)]]
- 1 edge to [[_COMMUNITY_Soc Bots]]
- 1 edge to [[_COMMUNITY_Collaborator Greeter]]
- 1 edge to [[_COMMUNITY_Event Bus.py (Gateway Core)]]
- 1 edge to [[_COMMUNITY_System overview (00 - START HERE)]]
- 1 edge to [[_COMMUNITY_V1 Models Synthetic]]

## Top bridge nodes
- [[make_event()]] - degree 57, connects to 11 communities
- [[approval.py]] - degree 16, connects to 7 communities
- [[event_bus.py]] - degree 9, connects to 4 communities
- [[ApprovalDecision]] - degree 6, connects to 3 communities
- [[event_bus.py_1]] - degree 5, connects to 3 communities