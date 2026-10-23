---
type: community
cohesion: 0.33
members: 6
---

# iot_button_register_cb (2)

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[dot-__init__()_34]] - code - gateway/approval_queue/queue.py
- [[dot-_load_pending_store()]] - code - gateway/approval_queue/queue.py
- [[ApprovalQueueConfig]] - code - gateway/approval_queue/queue.py
- [[Initialize approval queue          Args             config Approval queue conf]] - rationale - gateway/approval_queue/queue.py
- [[Load queue items from store file when present.]] - rationale - gateway/approval_queue/queue.py
- [[MFAGuard]] - code - gateway/approval_queue/queue.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/iot_button_register_cb_2
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_MCPPermissionManager]]

## Top bridge nodes
- [[dot-__init__()_34]] - degree 5, connects to 1 community
- [[dot-_load_pending_store()]] - degree 3, connects to 1 community
