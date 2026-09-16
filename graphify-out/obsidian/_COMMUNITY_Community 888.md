---
type: community
cohesion: 0.22
members: 10
---

# Community 888

**Cohesion:** 0.22 - loosely connected
**Members:** 10 nodes

## Members
- [[Validate a WebSocket token (single-use, time-limited).]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[WebSocket_6]] - code - gateway/ingest_api/routes/approval.py
- [[WebSocket_7]] - code - gateway/ingest_api/routes/dashboard.py
- [[WebSocket endpoint for real-time approval notifications      Protocol     1. Cl]] - rationale - gateway/ingest_api/routes/approval.py
- [[WebSocket for real-time activity feed]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[WebSocket stream specialized for egresssecurity dashboard updates.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[_validate_ws_token()]] - code - gateway/ingest_api/routes/dashboard.py
- [[activity_websocket()]] - code - gateway/ingest_api/routes/dashboard.py
- [[approval_websocket()]] - code - gateway/ingest_api/routes/approval.py
- [[egress_websocket()]] - code - gateway/ingest_api/routes/dashboard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_888
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Community 65]]
- 3 edges to [[_COMMUNITY_Community 116]]
- 2 edges to [[_COMMUNITY_Approval Routing & Event Bus]]

## Top bridge nodes
- [[activity_websocket()]] - degree 6, connects to 2 communities
- [[egress_websocket()]] - degree 6, connects to 2 communities
- [[_validate_ws_token()]] - degree 6, connects to 2 communities
- [[approval_websocket()]] - degree 5, connects to 2 communities