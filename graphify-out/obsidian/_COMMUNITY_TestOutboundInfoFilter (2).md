---
type: community
cohesion: 0.04
members: 67
---

# TestOutboundInfoFilter (2)

**Cohesion:** 0.04 - loosely connected
**Members:** 67 nodes

## Members
- [[dot-__init__()_191]] - code - gateway/ingest_api/event_bus.py
- [[dot-emit()_1]] - code - gateway/ingest_api/event_bus.py
- [[dot-get_recent()]] - code - gateway/ingest_api/event_bus.py
- [[dot-get_stats()_18]] - code - gateway/ingest_api/event_bus.py
- [[dot-subscribe()_1]] - code - gateway/ingest_api/event_bus.py
- [[dot-to_dict()_15]] - code - gateway/ingest_api/event_bus.py
- [[dot-unsubscribe()_1]] - code - gateway/ingest_api/event_bus.py
- [[3+ auth failures in 5 min escalates to critical]] - rationale - gateway/tests/test_event_bus.py
- [[3+ auth failures within 5 minutes escalates event severity to critical]] - concept - gateway/tests/test_event_bus.py
- [[A single gateway event]] - rationale - gateway/ingest_api/event_bus.py
- [[Any_79]] - code - gateway/ingest_api/event_bus.py
- [[Emit an event to all subscribers]] - rationale - gateway/ingest_api/event_bus.py
- [[Emitting with no subscribers doesn't raise]] - rationale - gateway/tests/test_event_bus.py
- [[EventBus]] - code - gateway/ingest_api/event_bus.py
- [[Events have type, timestamp, summary, details, severity]] - rationale - gateway/tests/test_event_bus.py
- [[GatewayEvent]] - code - gateway/ingest_api/event_bus.py
- [[Helper to create a GatewayEvent with current timestamp]] - rationale - gateway/ingest_api/event_bus.py
- [[Limit param caps the number of returned items.]] - rationale - gateway/tests/test_soc_egress_endpoints.py
- [[Multiple subscribers all receive the same event]] - rationale - gateway/tests/test_event_bus.py
- [[Recent events are returned in order]] - rationale - gateway/tests/test_event_bus.py
- [[Returns empty result when scanner_result_history is empty.]] - rationale - gateway/tests/test_soc_egress_endpoints.py
- [[Returns scanner events from app_state.scanner_result_history.]] - rationale - gateway/tests/test_soc_egress_endpoints.py
- [[Simple in-process event bus with async support]] - rationale - gateway/ingest_api/event_bus.py
- [[Stats track event counts]] - rationale - gateway/tests/test_event_bus.py
- [[Status query param filters by summary.status.]] - rationale - gateway/tests/test_soc_egress_endpoints.py
- [[Subscribe to all events]] - rationale - gateway/ingest_api/event_bus.py
- [[Subscriber receives emitted events]] - rationale - gateway/tests/test_event_bus.py
- [[Unsubscribe from events]] - rationale - gateway/ingest_api/event_bus.py
- [[Unsubscribed callback stops receiving events]] - rationale - gateway/tests/test_event_bus.py
- [[bus()]] - code - gateway/tests/test_event_bus.py
- [[event_bus.py_1]] - code - gateway/ingest_api/event_bus.py
- [[event_bus.py_2]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[make_event()]] - code - gateway/ingest_api/event_bus.py
- [[test_async_subscriber()]] - code - gateway/tests/test_event_bus.py
- [[test_auth_failure_escalation()]] - code - gateway/tests/test_event_bus.py
- [[test_emit_no_subscribers_no_error()]] - code - gateway/tests/test_event_bus.py
- [[test_emit_to_multiple_subscribers()]] - code - gateway/tests/test_event_bus.py
- [[test_event_bus.py]] - code - gateway/tests/test_event_bus.py
- [[test_event_has_required_fields()]] - code - gateway/tests/test_event_bus.py
- [[test_get_recent()]] - code - gateway/tests/test_event_bus.py
- [[test_get_stats()_2]] - code - gateway/tests/test_event_bus.py
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
TABLE source_file, type FROM #community/TestOutboundInfoFilter_2
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 6 edges to [[_COMMUNITY_AlertTelegramRelay]]
- 4 edges to [[_COMMUNITY_SkillGuard]]
- 4 edges to [[_COMMUNITY_create_auth_dependency()]]
- 3 edges to [[_COMMUNITY_UserSessionManager (2) (2)]]
- 3 edges to [[_COMMUNITY_MCPPermissionManager]]
- 2 edges to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 2 edges to [[_COMMUNITY_UserSessionManager (3)]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_colima-health-check.sh]]
- 1 edge to [[_COMMUNITY_What Does OpenClaw Actually Need to Write]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Value Proposition]]
- 1 edge to [[_COMMUNITY_AlertDispatcher (2)]]
- 1 edge to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_OpenClaw Host Hardening]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py (2)]]
- 1 edge to [[_COMMUNITY_MiddlewareManager (4)]]

## Top bridge nodes
- [[make_event()]] - degree 46, connects to 11 communities
- [[EventBus]] - degree 20, connects to 4 communities
- [[event_bus.py_1]] - degree 7, connects to 4 communities
- [[event_bus.py_2]] - degree 5, connects to 2 communities
- [[test_soc_egress_endpoints.py]] - degree 25, connects to 1 community
