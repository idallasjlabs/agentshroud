---
type: community
members: 15
---

# ._append_audit_event

**Members:** 15 nodes

## Members
- [[dot-_append_audit_event()]] - code - gateway/approval_queue/queue.py
- [[dot-_expire_stale()]] - code - gateway/approval_queue/queue.py
- [[dot-_persist_pending_store()]] - code - gateway/approval_queue/queue.py
- [[dot-broadcast()_1]] - code - gateway/approval_queue/queue.py
- [[dot-cleanup_decided()]] - code - gateway/approval_queue/queue.py
- [[dot-decide()_1]] - code - gateway/approval_queue/queue.py
- [[dot-get_pending()_2]] - code - gateway/approval_queue/queue.py
- [[Any_87]] - code
- [[Best-effort JSONL persistence for queue lifecycle events.]] - rationale - gateway/approval_queue/queue.py
- [[Check all pending items and expire those past timeout Returns List of expired…]] - rationale - gateway/approval_queue/queue.py
- [[Get all pending (not expired, not decided) items First expires any stale items.…]] - rationale - gateway/approval_queue/queue.py
- [[Persist queue items to disk for restart durability (best effort). Uses atomic…]] - rationale - gateway/approval_queue/queue.py
- [[Process an approval decision Args request_id Request UUID approved Whether…]] - rationale - gateway/approval_queue/queue.py
- [[Remove decided (approvedrejectedexpired) items older than max_age_seconds.…]] - rationale - gateway/approval_queue/queue.py
- [[Send a JSON message to all connected WebSocket clients Silently removes clients…]] - rationale - gateway/approval_queue/queue.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_append_audit_event
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 5 edges to [[_COMMUNITY_test_mfa_guard.py]]

## Top bridge nodes
- [[dot-_append_audit_event()]] - degree 6, connects to 2 communities
- [[dot-broadcast()_1]] - degree 6, connects to 2 communities
- [[dot-decide()_1]] - degree 6, connects to 2 communities
- [[dot-_persist_pending_store()]] - degree 6, connects to 2 communities
- [[dot-get_pending()_2]] - degree 4, connects to 2 communities
