---
type: community
cohesion: 0.29
members: 8
---

# Module Group 418

**Cohesion:** 0.29 - loosely connected
**Members:** 8 nodes

## Members
- [[.emit()]] - code - gateway/ingest_api/event_bus.py
- [[.get_recent()]] - code - gateway/ingest_api/event_bus.py
- [[.get_stats()]] - code - gateway/ingest_api/event_bus.py
- [[.to_dict()]] - code - gateway/ingest_api/event_bus.py
- [[A single gateway event]] - rationale - gateway/ingest_api/event_bus.py
- [[Any_4]] - code - gateway/ingest_api/event_bus.py
- [[Emit an event to all subscribers]] - rationale - gateway/ingest_api/event_bus.py
- [[GatewayEvent]] - code - gateway/ingest_api/event_bus.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_418
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 2 edges to [[_COMMUNITY_Dashboard Routes & WebSocket]]

## Top bridge nodes
- [[GatewayEvent]] - degree 5, connects to 2 communities
- [[Any_4]] - degree 4, connects to 1 community
- [[.emit()]] - degree 3, connects to 1 community
- [[.get_recent()]] - degree 3, connects to 1 community
- [[.get_stats()]] - degree 2, connects to 1 community