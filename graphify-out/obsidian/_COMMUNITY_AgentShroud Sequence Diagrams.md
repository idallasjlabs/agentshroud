---
type: community
cohesion: 0.33
members: 6
---

# AgentShroud Sequence Diagrams

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[.__init__()_5]] - code - gateway/approval_queue/queue.py
- [[._load_pending_store()]] - code - gateway/approval_queue/queue.py
- [[ApprovalQueueConfig_1]] - code - gateway/approval_queue/queue.py
- [[Initialize approval queue          Args             config Approval queue conf]] - rationale - gateway/approval_queue/queue.py
- [[Load queue items from store file when present.]] - rationale - gateway/approval_queue/queue.py
- [[MFAGuard_1]] - code - gateway/approval_queue/queue.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Sequence_Diagrams
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[.__init__()_5]] - degree 5, connects to 1 community
- [[._load_pending_store()]] - degree 3, connects to 1 community