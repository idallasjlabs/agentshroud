---
type: community
cohesion: 0.13
members: 21
---

# Community 423

**Cohesion:** 0.13 - loosely connected
**Members:** 21 nodes

## Members
- [[dot-_append_audit_event()]] - code - gateway/approval_queue/queue.py
- [[dot-_expire_stale()]] - code - gateway/approval_queue/queue.py
- [[dot-_persist_pending_store()]] - code - gateway/approval_queue/queue.py
- [[dot-broadcast()_1]] - code - gateway/approval_queue/queue.py
- [[dot-cleanup_decided()]] - code - gateway/approval_queue/queue.py
- [[dot-decide()_1]] - code - gateway/approval_queue/queue.py
- [[dot-get_item()_2]] - code - gateway/approval_queue/queue.py
- [[dot-get_pending()_1]] - code - gateway/approval_queue/queue.py
- [[dot-submit()_1]] - code - gateway/approval_queue/queue.py
- [[Add an action to the approval queue          Args             request Approval]] - rationale - gateway/approval_queue/queue.py
- [[Any_54]] - code - gateway/approval_queue/queue.py
- [[ApprovalQueueItem_3]] - code - gateway/approval_queue/queue.py
- [[ApprovalRequest_4]] - code - gateway/approval_queue/queue.py
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
TABLE source_file, type FROM #community/Community_423
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Approval Queue (WebSocket)]]
- 1 edge to [[_COMMUNITY_SOC Service Manager (Container Engine)]]

## Top bridge nodes
- [[dot-decide()_1]] - degree 7, connects to 2 communities
- [[dot-submit()_1]] - degree 7, connects to 1 community
- [[dot-_append_audit_event()]] - degree 6, connects to 1 community
- [[dot-broadcast()_1]] - degree 6, connects to 1 community
- [[dot-_expire_stale()]] - degree 6, connects to 1 community