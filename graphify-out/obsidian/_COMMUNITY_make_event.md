---
type: community
cohesion: 0.07
members: 41
---

# make_event

**Cohesion:** 0.07 - loosely connected
**Members:** 41 nodes

## Members
- [[dot-__init__()_60]] - code - gateway/ingest_api/event_bus.py
- [[dot-emit()]] - code - gateway/ingest_api/event_bus.py
- [[dot-get_recent()]] - code - gateway/ingest_api/event_bus.py
- [[dot-get_stats()_3]] - code - gateway/ingest_api/event_bus.py
- [[dot-subscribe()_1]] - code - gateway/ingest_api/event_bus.py
- [[dot-to_dict()_7]] - code - gateway/ingest_api/event_bus.py
- [[dot-unsubscribe()_1]] - code - gateway/ingest_api/event_bus.py
- [[3+ auth failures in 5 min escalates to critical]] - rationale - gateway/tests/test_event_bus.py
- [[3+ auth failures within 5 minutes escalates event severity to critical]] - concept - gateway/tests/test_event_bus.py
- [[A single gateway event]] - rationale - gateway/ingest_api/event_bus.py
- [[Any_24]] - code - gateway/ingest_api/event_bus.py
- [[Emit an event to all subscribers]] - rationale - gateway/ingest_api/event_bus.py
- [[Emitting with no subscribers doesn't raise]] - rationale - gateway/tests/test_event_bus.py
- [[EventBus]] - code - gateway/ingest_api/event_bus.py
- [[Events have type, timestamp, summary, details, severity]] - rationale - gateway/tests/test_event_bus.py
- [[GatewayEvent]] - code - gateway/ingest_api/event_bus.py
- [[Helper to create a GatewayEvent with current timestamp]] - rationale - gateway/ingest_api/event_bus.py
- [[Multiple subscribers all receive the same event]] - rationale - gateway/tests/test_event_bus.py
- [[Recent events are returned in order]] - rationale - gateway/tests/test_event_bus.py
- [[Regression (SCRUM-61) apialerts used to call event_bus.publish(),     a metho]] - rationale - gateway/tests/test_alert_telegram_relay.py
- [[Simple in-process event bus with async support]] - rationale - gateway/ingest_api/event_bus.py
- [[Stats track event counts]] - rationale - gateway/tests/test_event_bus.py
- [[Subscribe to all events]] - rationale - gateway/ingest_api/event_bus.py
- [[Subscriber receives emitted events]] - rationale - gateway/tests/test_event_bus.py
- [[Unsubscribe from events]] - rationale - gateway/ingest_api/event_bus.py
- [[Unsubscribed callback stops receiving events]] - rationale - gateway/tests/test_event_bus.py
- [[bus()]] - code - gateway/tests/test_event_bus.py
- [[event_bus.py]] - code - gateway/ingest_api/event_bus.py
- [[event_bus.py_1]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[make_event()]] - code - gateway/ingest_api/event_bus.py
- [[test_api_alerts_endpoint_emits_bus_event()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[test_async_subscriber()]] - code - gateway/tests/test_event_bus.py
- [[test_auth_failure_escalation()]] - code - gateway/tests/test_event_bus.py
- [[test_emit_no_subscribers_no_error()]] - code - gateway/tests/test_event_bus.py
- [[test_emit_to_multiple_subscribers()]] - code - gateway/tests/test_event_bus.py
- [[test_event_bus.py]] - code - gateway/tests/test_event_bus.py
- [[test_event_has_required_fields()]] - code - gateway/tests/test_event_bus.py
- [[test_get_recent()]] - code - gateway/tests/test_event_bus.py
- [[test_get_stats()]] - code - gateway/tests/test_event_bus.py
- [[test_subscribe_receive_events()]] - code - gateway/tests/test_event_bus.py
- [[test_unsubscribe_stops_events()]] - code - gateway/tests/test_event_bus.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/make_event
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_DataLedger]]
- 7 edges to [[_COMMUNITY_test_dashboard.py]]
- 7 edges to [[_COMMUNITY_AlertTelegramRelay]]
- 3 edges to [[_COMMUNITY_TestEgressApprovalQueue_1]]
- 3 edges to [[_COMMUNITY_AgentRegistry]]
- 3 edges to [[_COMMUNITY_test_forward_stream.py]]
- 3 edges to [[_COMMUNITY_activity_websocket]]
- 3 edges to [[_COMMUNITY_EgressFilterConfig]]
- 3 edges to [[_COMMUNITY_test_soc_egress_endpoints.py]]
- 2 edges to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_UserSessionManager]]
- 1 edge to [[_COMMUNITY_main.py]]
- 1 edge to [[_COMMUNITY_ForwardRequest]]
- 1 edge to [[_COMMUNITY_dot-process_tool_call]]
- 1 edge to [[_COMMUNITY_dot-_filter_outbound]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager_1]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py_1]]
- 1 edge to [[_COMMUNITY_TestEgressApprovalQueue]]
- 1 edge to [[_COMMUNITY__req]]
- 1 edge to [[_COMMUNITY_event_bus.py]]

## Top bridge nodes
- [[make_event()]] - degree 46, connects to 13 communities
- [[EventBus]] - degree 25, connects to 6 communities
- [[event_bus.py]] - degree 8, connects to 4 communities
- [[event_bus.py_1]] - degree 5, connects to 2 communities
- [[test_api_alerts_endpoint_emits_bus_event()]] - degree 4, connects to 2 communities
