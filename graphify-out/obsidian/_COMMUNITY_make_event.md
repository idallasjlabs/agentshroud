---
type: community
members: 20
---

# make_event

**Members:** 20 nodes

## Members
- [[dot-__init__()_147]] - code - gateway/ingest_api/event_bus.py
- [[dot-emit()_1]] - code - gateway/ingest_api/event_bus.py
- [[dot-get_recent()]] - code - gateway/ingest_api/event_bus.py
- [[dot-get_stats()_13]] - code - gateway/ingest_api/event_bus.py
- [[dot-subscribe()_1]] - code - gateway/ingest_api/event_bus.py
- [[dot-to_dict()_11]] - code - gateway/ingest_api/event_bus.py
- [[dot-unsubscribe()_1]] - code - gateway/ingest_api/event_bus.py
- [[3+ auth failures within 5 minutes escalates event severity to critical]] - concept - gateway/tests/test_event_bus.py
- [[A single gateway event]] - rationale - gateway/ingest_api/event_bus.py
- [[Any_57]] - code - gateway/ingest_api/event_bus.py
- [[Emit an event to all subscribers]] - rationale - gateway/ingest_api/event_bus.py
- [[EventBus]] - code - gateway/ingest_api/event_bus.py
- [[GatewayEvent]] - code - gateway/ingest_api/event_bus.py
- [[Regression (SCRUM-61) apialerts used to call event_bus.publish(),     a metho]] - rationale - gateway/tests/test_alert_telegram_relay.py
- [[Simple in-process event bus with async support]] - rationale - gateway/ingest_api/event_bus.py
- [[Subscribe to all events]] - rationale - gateway/ingest_api/event_bus.py
- [[Unsubscribe from events]] - rationale - gateway/ingest_api/event_bus.py
- [[event_bus.py]] - code - gateway/ingest_api/event_bus.py
- [[event_bus.py_1]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[test_api_alerts_endpoint_emits_bus_event()]] - code - gateway/tests/test_alert_telegram_relay.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/make_event
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_soc_egress_endpoints.py]]
- 4 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 4 edges to [[_COMMUNITY_AlertTelegramRelay]]
- 3 edges to [[_COMMUNITY_agentshroud-blueteamSKILL.md (3)]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig (5)]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig]]
- 1 edge to [[_COMMUNITY_create_auth_dependency (2)]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py (2)]]
- 1 edge to [[_COMMUNITY_create_auth_dependency (3)]]
- 1 edge to [[_COMMUNITY_test_dashboard.py]]
- 1 edge to [[_COMMUNITY_event_bus.py]]
- 1 edge to [[_COMMUNITY_main.py_1]]

## Top bridge nodes
- [[EventBus]] - degree 25, connects to 7 communities
- [[event_bus.py]] - degree 8, connects to 6 communities
- [[event_bus.py_1]] - degree 5, connects to 3 communities
- [[test_api_alerts_endpoint_emits_bus_event()]] - degree 4, connects to 2 communities
- [[GatewayEvent]] - degree 7, connects to 1 community
