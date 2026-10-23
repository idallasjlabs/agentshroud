---
type: community
cohesion: 0.40
members: 5
---

# .connect()

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[dot-connect()]] - code - gateway/approval_queue/queue.py
- [[dot-disconnect()]] - code - gateway/approval_queue/queue.py
- [[Accept a WebSocket connection and add to connected set          Args]] - rationale - gateway/approval_queue/queue.py
- [[Remove a WebSocket connection from connected set          Args             webs]] - rationale - gateway/approval_queue/queue.py
- [[WebSocket]] - code - gateway/approval_queue/queue.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/connect
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_MCPPermissionManager]]

## Top bridge nodes
- [[dot-connect()]] - degree 3, connects to 1 community
- [[dot-disconnect()]] - degree 3, connects to 1 community
