---
type: community
members: 49
---

# Community 85

**Members:** 49 nodes

## Members
- [[3+ auth failures in 5 min escalates to critical]] - rationale - gateway/tests/test_event_bus.py
- [[Emitting with no subscribers doesn't raise]] - rationale - gateway/tests/test_event_bus.py
- [[Events have type, timestamp, summary, details, severity]] - rationale - gateway/tests/test_event_bus.py
- [[Helper to create a GatewayEvent with current timestamp]] - rationale - gateway/ingest_api/event_bus.py
- [[Limit param caps the number of returned items.]] - rationale - gateway/tests/test_soc_egress_endpoints.py
- [[Multiple subscribers all receive the same event]] - rationale - gateway/tests/test_event_bus.py
- [[Recent events are returned in order]] - rationale - gateway/tests/test_event_bus.py
- [[Returns empty result when scanner_result_history is empty.]] - rationale - gateway/tests/test_soc_egress_endpoints.py
- [[Returns scanner events from app_state.scanner_result_history.]] - rationale - gateway/tests/test_soc_egress_endpoints.py
- [[Stats track event counts]] - rationale - gateway/tests/test_event_bus.py
- [[Status query param filters by summary.status.]] - rationale - gateway/tests/test_soc_egress_endpoints.py
- [[Subscriber receives emitted events]] - rationale - gateway/tests/test_event_bus.py
- [[Unsubscribed callback stops receiving events]] - rationale - gateway/tests/test_event_bus.py
- [[bus()]] - code - gateway/tests/test_event_bus.py
- [[make_event()]] - code - gateway/ingest_api/event_bus.py
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
TABLE source_file, type FROM #community/Community_85
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Community 6]]
- 8 edges to [[_COMMUNITY_Community 62]]
- 6 edges to [[_COMMUNITY_Community 978]]
- 4 edges to [[_COMMUNITY_Community 1248]]
- 4 edges to [[_COMMUNITY_Community 93]]
- 3 edges to [[_COMMUNITY_Community 229]]
- 2 edges to [[_COMMUNITY_Community 34]]
- 2 edges to [[_COMMUNITY_Community 68]]
- 1 edge to [[_COMMUNITY_Community 59]]
- 1 edge to [[_COMMUNITY_Community 232]]
- 1 edge to [[_COMMUNITY_Community 223]]
- 1 edge to [[_COMMUNITY_Community 96]]
- 1 edge to [[_COMMUNITY_Community 17]]
- 1 edge to [[_COMMUNITY_Community 919]]
- 1 edge to [[_COMMUNITY_Community 309]]

## Top bridge nodes
- [[make_event()]] - degree 57, connects to 13 communities
- [[test_soc_egress_endpoints.py]] - degree 25, connects to 1 community
- [[test_event_bus.py]] - degree 12, connects to 1 community
- [[test_manage_soc_report_endpoint()]] - degree 3, connects to 1 community
- [[bus()]] - degree 2, connects to 1 community