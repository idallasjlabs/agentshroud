---
type: community
members: 40
---

# Community 439

**Members:** 40 nodes

## Members
- [[.__init__()_5]] - code - gateway/approval_queue/queue.py
- [[._append_audit_event()]] - code - gateway/approval_queue/queue.py
- [[._expire_stale()]] - code - gateway/approval_queue/queue.py
- [[._load_pending_store()]] - code - gateway/approval_queue/queue.py
- [[._persist_pending_store()]] - code - gateway/approval_queue/queue.py
- [[.broadcast()_1]] - code - gateway/approval_queue/queue.py
- [[.cleanup_decided()]] - code - gateway/approval_queue/queue.py
- [[.connect()_1]] - code - gateway/approval_queue/queue.py
- [[.decide()_1]] - code - gateway/approval_queue/queue.py
- [[.disconnect()_1]] - code - gateway/approval_queue/queue.py
- [[.get_item()_1]] - code - gateway/approval_queue/queue.py
- [[.get_pending()_1]] - code - gateway/approval_queue/queue.py
- [[.submit()_1]] - code - gateway/approval_queue/queue.py
- [[Accept a WebSocket connection and add to connected set          Args]] - rationale - gateway/approval_queue/queue.py
- [[Add an action to the approval queue          Args             request Approval]] - rationale - gateway/approval_queue/queue.py
- [[Any_2]] - code - gateway/approval_queue/queue.py
- [[ApprovalQueue]] - code - gateway/approval_queue/queue.py
- [[ApprovalQueueConfig_1]] - code - gateway/approval_queue/queue.py
- [[ApprovalQueueItem_1]] - code - gateway/approval_queue/queue.py
- [[ApprovalRequest_2]] - code - gateway/approval_queue/queue.py
- [[Best-effort JSONL persistence for queue lifecycle events.]] - rationale - gateway/approval_queue/queue.py
- [[Check all pending items and expire those past timeout          Returns]] - rationale - gateway/approval_queue/queue.py
- [[Create approval queue instance for testing]] - rationale - gateway/tests/test_approval_queue.py
- [[Fetch a single queue item by ID          Args             request_id Request U]] - rationale - gateway/approval_queue/queue.py
- [[Get all pending (not expired, not decided) items          First expires any stal]] - rationale - gateway/approval_queue/queue.py
- [[In-memory approval queue with WebSocket notifications      Actions requiring app]] - rationale - gateway/approval_queue/queue.py
- [[Initialize approval queue          Args             config Approval queue conf]] - rationale - gateway/approval_queue/queue.py
- [[Load queue items from store file when present.]] - rationale - gateway/approval_queue/queue.py
- [[MFAGuard_1]] - code - gateway/approval_queue/queue.py
- [[Persist queue items to disk for restart durability (best effort).          Uses]] - rationale - gateway/approval_queue/queue.py
- [[Process an approval decision          Args             request_id Request UUID]] - rationale - gateway/approval_queue/queue.py
- [[Queue should restore persisted items from store file on startup.]] - rationale - gateway/tests/test_approval_queue.py
- [[Remove a WebSocket connection from connected set          Args             webs]] - rationale - gateway/approval_queue/queue.py
- [[Remove decided (approvedrejectedexpired) items older than max_age_seconds.]] - rationale - gateway/approval_queue/queue.py
- [[Send a JSON message to all connected WebSocket clients          Silently removes]] - rationale - gateway/approval_queue/queue.py
- [[WebSocket_1]] - code - gateway/approval_queue/queue.py
- [[approval_queue()]] - code - gateway/tests/test_approval_queue.py
- [[approval_queue()_1]] - code - gateway/tests/test_security_integration.py
- [[queue()]] - code - gateway/tests/test_approval_stress.py
- [[test_store_restores_items_on_init()]] - code - gateway/tests/test_approval_queue.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_439
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Community 80]]
- 8 edges to [[_COMMUNITY_Community 50]]
- 7 edges to [[_COMMUNITY_Community 68]]
- 6 edges to [[_COMMUNITY_Community 108]]
- 4 edges to [[_COMMUNITY_Community 70]]
- 3 edges to [[_COMMUNITY_Community 30]]
- 2 edges to [[_COMMUNITY_Community 532]]
- 1 edge to [[_COMMUNITY_Community 7]]
- 1 edge to [[_COMMUNITY_Community 20]]

## Top bridge nodes
- [[ApprovalQueue]] - degree 51, connects to 8 communities
- [[queue()]] - degree 3, connects to 2 communities
- [[approval_queue()_1]] - degree 3, connects to 2 communities
- [[.decide()_1]] - degree 7, connects to 1 community
- [[approval_queue()]] - degree 3, connects to 1 community