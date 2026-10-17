---
type: community
members: 6
---

# Git Workflow Guardian (GIT-GUARD)

**Members:** 6 nodes

## Members
- [[dot-__init__()_42]] - code - gateway/approval_queue/queue.py
- [[dot-_load_pending_store()]] - code - gateway/approval_queue/queue.py
- [[ApprovalQueueConfig]] - code - gateway/approval_queue/queue.py
- [[Initialize approval queue          Args             config Approval queue conf]] - rationale - gateway/approval_queue/queue.py
- [[Load queue items from store file when present.]] - rationale - gateway/approval_queue/queue.py
- [[MFAGuard]] - code - gateway/approval_queue/queue.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Git_Workflow_Guardian_GIT-GUARD
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig]]

## Top bridge nodes
- [[dot-__init__()_42]] - degree 5, connects to 1 community
- [[dot-_load_pending_store()]] - degree 3, connects to 1 community
