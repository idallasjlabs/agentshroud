---
type: community
cohesion: 0.67
members: 3
---

# .test_collaborator_web_access_request_queues_own

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[WebSocket_9]] - code - gateway/ingest_api/main.py
- [[WebSocket relay for Slack Socket Mode inbound traffic.      Bot connects here (w]] - rationale - gateway/ingest_api/main.py
- [[slack_ws_relay()]] - code - gateway/ingest_api/main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_collaborator_web_access_request_queues_own
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_SSHProxy]]

## Top bridge nodes
- [[slack_ws_relay()]] - degree 4, connects to 1 community