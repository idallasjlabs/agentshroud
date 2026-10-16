---
type: community
cohesion: 0.15
members: 17
---

# make_event

**Cohesion:** 0.15 - loosely connected
**Members:** 17 nodes

## Members
- [[dot-__init__()_137]] - code - gateway/ingest_api/event_bus.py
- [[dot-emit()_1]] - code - gateway/ingest_api/event_bus.py
- [[dot-get_recent()]] - code - gateway/ingest_api/event_bus.py
- [[dot-get_stats()_13]] - code - gateway/ingest_api/event_bus.py
- [[dot-subscribe()_1]] - code - gateway/ingest_api/event_bus.py
- [[dot-to_dict()_9]] - code - gateway/ingest_api/event_bus.py
- [[dot-unsubscribe()_1]] - code - gateway/ingest_api/event_bus.py
- [[3+ auth failures within 5 minutes escalates event severity to critical]] - concept - gateway/tests/test_event_bus.py
- [[A single gateway event]] - rationale - gateway/ingest_api/event_bus.py
- [[Any_51]] - code - gateway/ingest_api/event_bus.py
- [[Emit an event to all subscribers]] - rationale - gateway/ingest_api/event_bus.py
- [[EventBus]] - code - gateway/ingest_api/event_bus.py
- [[GatewayEvent]] - code - gateway/ingest_api/event_bus.py
- [[Simple in-process event bus with async support]] - rationale - gateway/ingest_api/event_bus.py
- [[Subscribe to all events]] - rationale - gateway/ingest_api/event_bus.py
- [[Unsubscribe from events]] - rationale - gateway/ingest_api/event_bus.py
- [[event_bus.py]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/make_event
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_PIIConfig]]
- 4 edges to [[_COMMUNITY_AlertTelegramRelay]]
- 3 edges to [[_COMMUNITY_test_dashboard.py]]
- 3 edges to [[_COMMUNITY_create_auth_dependency]]
- 2 edges to [[_COMMUNITY_make_event_1]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_ForwardRequest]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_event_bus.py]]
- 1 edge to [[_COMMUNITY_main.py]]

## Top bridge nodes
- [[EventBus]] - degree 25, connects to 7 communities
- [[event_bus.py]] - degree 5, connects to 3 communities
- [[GatewayEvent]] - degree 7, connects to 2 communities
- [[Any_51]] - degree 4, connects to 1 community
