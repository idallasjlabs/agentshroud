---
type: community
members: 38
---

# EventBus

**Members:** 38 nodes

## Members
- [[dot-__init__()_6]] - code - gateway/ingest_api/event_bus.py
- [[dot-emit()]] - code - gateway/ingest_api/event_bus.py
- [[dot-get_recent()]] - code - gateway/ingest_api/event_bus.py
- [[dot-get_stats()]] - code - gateway/ingest_api/event_bus.py
- [[dot-subscribe()]] - code - gateway/ingest_api/event_bus.py
- [[dot-to_dict()]] - code - gateway/ingest_api/event_bus.py
- [[dot-unsubscribe()]] - code - gateway/ingest_api/event_bus.py
- [[3+ auth failures in 5 min escalates to critical]] - rationale - gateway/tests/test_event_bus.py
- [[A single gateway event]] - rationale - gateway/ingest_api/event_bus.py
- [[Any_7]] - code
- [[Emit an event to all subscribers]] - rationale - gateway/ingest_api/event_bus.py
- [[Emitting with no subscribers doesn't raise]] - rationale - gateway/tests/test_event_bus.py
- [[EventBus]] - code - gateway/ingest_api/event_bus.py
- [[Events have type, timestamp, summary, details, severity]] - rationale - gateway/tests/test_event_bus.py
- [[GatewayEvent]] - code - gateway/ingest_api/event_bus.py
- [[Multiple subscribers all receive the same event]] - rationale - gateway/tests/test_event_bus.py
- [[Recent events are returned in order]] - rationale - gateway/tests/test_event_bus.py
- [[Simple in-process event bus with async support]] - rationale - gateway/ingest_api/event_bus.py
- [[Stats track event counts]] - rationale - gateway/tests/test_event_bus.py
- [[Subscribe to all events]] - rationale - gateway/ingest_api/event_bus.py
- [[Subscriber receives emitted events]] - rationale - gateway/tests/test_event_bus.py
- [[Unsubscribe from events]] - rationale - gateway/ingest_api/event_bus.py
- [[Unsubscribed callback stops receiving events]] - rationale - gateway/tests/test_event_bus.py
- [[asyncio_2]] - code
- [[bus()]] - code - gateway/tests/test_event_bus.py
- [[cb()]] - code - gateway/tests/test_event_bus.py
- [[cb()_1]] - code - gateway/tests/test_event_bus.py
- [[fixture_13]] - code
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
TABLE source_file, type FROM #community/EventBus
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_ingest_apimain.py]]
- 3 edges to [[_COMMUNITY_AlertTelegramRelay]]
- 3 edges to [[_COMMUNITY__coerce_to_ws_event]]
- 2 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 1 edge to [[_COMMUNITY_SOCWebSocketHandler]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_test_soc_edge.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[EventBus]] - degree 22, connects to 8 communities
- [[GatewayEvent]] - degree 7, connects to 2 communities
- [[test_event_bus.py]] - degree 13, connects to 1 community
- [[test_async_subscriber()]] - degree 5, connects to 1 community
- [[test_unsubscribe_stops_events()]] - degree 5, connects to 1 community
