---
type: community
cohesion: 0.29
members: 7
---

# Community 1013

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[.load_all()]] - code - gateway/approval_queue/store.py
- [[.load_pending()]] - code - gateway/approval_queue/store.py
- [[.save()]] - code - gateway/approval_queue/store.py
- [[ApprovalQueueItem_2]] - code - gateway/approval_queue/store.py
- [[Insert or replace an approval item.]] - rationale - gateway/approval_queue/store.py
- [[Load all items (for auditdebugging).]] - rationale - gateway/approval_queue/store.py
- [[Load all pending (non-expired, non-decided) items.          Items whose expires_]] - rationale - gateway/approval_queue/store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1013
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 23]]

## Top bridge nodes
- [[.load_all()]] - degree 3, connects to 1 community
- [[.load_pending()]] - degree 3, connects to 1 community
- [[.save()]] - degree 3, connects to 1 community