---
type: community
members: 19
---

# make_event

**Members:** 19 nodes

## Members
- [[dot-__init__()_142]] - code - gateway/ingest_api/event_bus.py
- [[dot-emit()_1]] - code - gateway/ingest_api/event_bus.py
- [[dot-get_recent()]] - code - gateway/ingest_api/event_bus.py
- [[dot-get_stats()_12]] - code - gateway/ingest_api/event_bus.py
- [[dot-subscribe()]] - code - gateway/ingest_api/event_bus.py
- [[dot-to_dict()_8]] - code - gateway/ingest_api/event_bus.py
- [[dot-unsubscribe()]] - code - gateway/ingest_api/event_bus.py
- [[3+ auth failures within 5 minutes escalates event severity to critical]] - concept - gateway/tests/test_event_bus.py
- [[A single gateway event]] - rationale - gateway/ingest_api/event_bus.py
- [[Any_53]] - code - gateway/ingest_api/event_bus.py
- [[Emit an event to all subscribers]] - rationale - gateway/ingest_api/event_bus.py
- [[EventBus]] - code - gateway/ingest_api/event_bus.py
- [[GatewayEvent]] - code - gateway/ingest_api/event_bus.py
- [[Regression (SCRUM-61) apialerts used to call event_bus.publish(),     a metho]] - rationale - gateway/tests/test_alert_telegram_relay.py
- [[Simple in-process event bus with async support]] - rationale - gateway/ingest_api/event_bus.py
- [[Subscribe to all events]] - rationale - gateway/ingest_api/event_bus.py
- [[Unsubscribe from events]] - rationale - gateway/ingest_api/event_bus.py
- [[event_bus.py_1]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[test_api_alerts_endpoint_emits_bus_event()]] - code - gateway/tests/test_alert_telegram_relay.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/make_event
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_AlertTelegramRelay]]
- 3 edges to [[_COMMUNITY_create_auth_dependency]]
- 3 edges to [[_COMMUNITY_test_dashboard.py]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_telegram_proxy.py (2)]]
- 2 edges to [[_COMMUNITY_make_event (2)]]
- 1 edge to [[_COMMUNITY__req]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig]]
- 1 edge to [[_COMMUNITY_event_bus.py]]
- 1 edge to [[_COMMUNITY_main.py]]

## Top bridge nodes
- [[EventBus]] - degree 25, connects to 8 communities
- [[event_bus.py_1]] - degree 5, connects to 3 communities
- [[GatewayEvent]] - degree 7, connects to 2 communities
- [[test_api_alerts_endpoint_emits_bus_event()]] - degree 4, connects to 2 communities
- [[Any_53]] - degree 4, connects to 1 community
