---
type: community
members: 21
---

# Community 255

**Members:** 21 nodes

## Members
- [[._append_audit_event()]] - code - gateway/approval_queue/queue.py
- [[._expire_stale()]] - code - gateway/approval_queue/queue.py
- [[._persist_pending_store()]] - code - gateway/approval_queue/queue.py
- [[.broadcast()_1]] - code - gateway/approval_queue/queue.py
- [[.cleanup_decided()]] - code - gateway/approval_queue/queue.py
- [[.decide()_1]] - code - gateway/approval_queue/queue.py
- [[.get_item()_1]] - code - gateway/approval_queue/queue.py
- [[.get_pending()_1]] - code - gateway/approval_queue/queue.py
- [[.submit()_1]] - code - gateway/approval_queue/queue.py
- [[Add an action to the approval queue          Args             request Approval]] - rationale - gateway/approval_queue/queue.py
- [[Any_2]] - code - gateway/approval_queue/queue.py
- [[ApprovalQueueItem_1]] - code - gateway/approval_queue/queue.py
- [[ApprovalRequest_2]] - code - gateway/approval_queue/queue.py
- [[Best-effort JSONL persistence for queue lifecycle events.]] - rationale - gateway/approval_queue/queue.py
- [[Check all pending items and expire those past timeout          Returns]] - rationale - gateway/approval_queue/queue.py
- [[Fetch a single queue item by ID          Args             request_id Request U]] - rationale - gateway/approval_queue/queue.py
- [[Get all pending (not expired, not decided) items          First expires any stal]] - rationale - gateway/approval_queue/queue.py
- [[Persist queue items to disk for restart durability (best effort).          Uses]] - rationale - gateway/approval_queue/queue.py
- [[Process an approval decision          Args             request_id Request UUID]] - rationale - gateway/approval_queue/queue.py
- [[Remove decided (approvedrejectedexpired) items older than max_age_seconds.]] - rationale - gateway/approval_queue/queue.py
- [[Send a JSON message to all connected WebSocket clients          Silently removes]] - rationale - gateway/approval_queue/queue.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_255
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 486]]

## Top bridge nodes
- [[.decide()_1]] - degree 7, connects to 2 communities
- [[.submit()_1]] - degree 7, connects to 1 community
- [[._expire_stale()]] - degree 6, connects to 1 community
- [[.broadcast()_1]] - degree 6, connects to 1 community
- [[._append_audit_event()]] - degree 6, connects to 1 community