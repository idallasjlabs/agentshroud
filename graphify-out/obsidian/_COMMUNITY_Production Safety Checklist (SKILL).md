---
type: community
members: 19
---

# Production Safety Checklist (SKILL)

**Members:** 19 nodes

## Members
- [[dot-__init__()_150]] - code - gateway/ingest_api/event_bus.py
- [[dot-emit()_1]] - code - gateway/ingest_api/event_bus.py
- [[dot-get_recent()]] - code - gateway/ingest_api/event_bus.py
- [[dot-get_stats()_17]] - code - gateway/ingest_api/event_bus.py
- [[dot-subscribe()_1]] - code - gateway/ingest_api/event_bus.py
- [[dot-to_dict()_10]] - code - gateway/ingest_api/event_bus.py
- [[dot-unsubscribe()_1]] - code - gateway/ingest_api/event_bus.py
- [[3+ auth failures within 5 minutes escalates event severity to critical]] - concept - gateway/tests/test_event_bus.py
- [[A single gateway event]] - rationale - gateway/ingest_api/event_bus.py
- [[Any_56]] - code - gateway/ingest_api/event_bus.py
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
TABLE source_file, type FROM #community/Production_Safety_Checklist_SKILL
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_TestOutboundInfoFilter (2)_1]]
- 4 edges to [[_COMMUNITY_EgressFilterConfig (2) (2)_1]]
- 2 edges to [[_COMMUNITY_lifespan()]]
- 1 edge to [[_COMMUNITY_MiddlewareManager (4)]]
- 1 edge to [[_COMMUNITY__make_proxy()]]
- 1 edge to [[_COMMUNITY_UserSessionManager (3)]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager]]
- 1 edge to [[_COMMUNITY_TestProductionCompose]]
- 1 edge to [[_COMMUNITY_OpenClaw Host Hardening]]

## Top bridge nodes
- [[EventBus]] - degree 20, connects to 6 communities
- [[event_bus.py_1]] - degree 5, connects to 3 communities
- [[GatewayEvent]] - degree 7, connects to 2 communities
- [[test_api_alerts_endpoint_emits_bus_event()]] - degree 4, connects to 2 communities
- [[Any_56]] - degree 4, connects to 1 community
