---
type: community
cohesion: 0.03
members: 75
---

# Approval Queue Core

**Cohesion:** 0.03 - loosely connected
**Members:** 75 nodes

## Members
- [[.__init__()_1]] - code - gateway/approval_queue/queue.py
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
- [[Any_1]] - code - gateway/approval_queue/queue.py
- [[ApprovalQueue]] - code - gateway/approval_queue/queue.py
- [[ApprovalQueueConfig_1]] - code - gateway/approval_queue/queue.py
- [[ApprovalQueueItem_1]] - code - gateway/approval_queue/queue.py
- [[ApprovalRequest_1]] - code - gateway/approval_queue/queue.py
- [[Best-effort JSONL persistence for queue lifecycle events.]] - rationale - gateway/approval_queue/queue.py
- [[Check all pending items and expire those past timeout          Returns]] - rationale - gateway/approval_queue/queue.py
- [[Create approval queue configuration for testing]] - rationale - gateway/tests/test_approval_queue.py
- [[Create approval queue instance for testing]] - rationale - gateway/tests/test_approval_queue.py
- [[Fetch a single queue item by ID          Args             request_id Request U]] - rationale - gateway/approval_queue/queue.py
- [[Get all pending (not expired, not decided) items          First expires any stal]] - rationale - gateway/approval_queue/queue.py
- [[In-memory approval queue with WebSocket notifications      Actions requiring app]] - rationale - gateway/approval_queue/queue.py
- [[Initialize approval queue          Args             config Approval queue conf]] - rationale - gateway/approval_queue/queue.py
- [[Load queue items from store file when present.]] - rationale - gateway/approval_queue/queue.py
- [[Persist queue items to disk for restart durability (best effort).]] - rationale - gateway/approval_queue/queue.py
- [[Process an approval decision          Args             request_id Request UUID]] - rationale - gateway/approval_queue/queue.py
- [[Queue should restore persisted items from store file on startup.]] - rationale - gateway/tests/test_approval_queue.py
- [[Queue store file should persist items and status transitions.]] - rationale - gateway/tests/test_approval_queue.py
- [[Remove a WebSocket connection from connected set          Args             webs]] - rationale - gateway/approval_queue/queue.py
- [[Remove decided (approvedrejectedexpired) items older than max_age_seconds.]] - rationale - gateway/approval_queue/queue.py
- [[Send a JSON message to all connected WebSocket clients          Silently removes]] - rationale - gateway/approval_queue/queue.py
- [[Test WebSocket client disconnection]] - rationale - gateway/tests/test_approval_queue.py
- [[Test approving a pending request]] - rationale - gateway/tests/test_approval_queue.py
- [[Test deciding on already-decided request raises ValueError]] - rationale - gateway/tests/test_approval_queue.py
- [[Test deciding on an expired request raises ValueError]] - rationale - gateway/tests/test_approval_queue.py
- [[Test deciding on nonexistent request raises KeyError]] - rationale - gateway/tests/test_approval_queue.py
- [[Test getting a specific item by ID]] - rationale - gateway/tests/test_approval_queue.py
- [[Test getting all pending requests]] - rationale - gateway/tests/test_approval_queue.py
- [[Test getting nonexistent item returns None]] - rationale - gateway/tests/test_approval_queue.py
- [[Test rejecting a pending request]] - rationale - gateway/tests/test_approval_queue.py
- [[Test submitting an approval request]] - rationale - gateway/tests/test_approval_queue.py
- [[Test that concurrent decision attempts are handled correctly]] - rationale - gateway/tests/test_approval_queue.py
- [[Test that get_pending excludes decided requests]] - rationale - gateway/tests/test_approval_queue.py
- [[Test that requests expire after timeout]] - rationale - gateway/tests/test_approval_queue.py
- [[WebSocket_1]] - code - gateway/approval_queue/queue.py
- [[approval_queue()]] - code - gateway/tests/test_approval_queue.py
- [[approval_queue()_1]] - code - gateway/tests/test_security_integration.py
- [[cleanup_decided() must not remove pending items regardless of age.]] - rationale - gateway/tests/test_approval_queue.py
- [[cleanup_decided() should not remove decided items newer than threshold.]] - rationale - gateway/tests/test_approval_queue.py
- [[cleanup_decided() should remove approvedrejected items older than threshold.]] - rationale - gateway/tests/test_approval_queue.py
- [[queue_config()]] - code - gateway/tests/test_approval_queue.py
- [[test_approval_queue.py]] - code - gateway/tests/test_approval_queue.py
- [[test_cleanup_decided_keeps_pending_items()]] - code - gateway/tests/test_approval_queue.py
- [[test_cleanup_decided_keeps_recent_decided_items()]] - code - gateway/tests/test_approval_queue.py
- [[test_cleanup_decided_removes_old_decided_items()]] - code - gateway/tests/test_approval_queue.py
- [[test_concurrent_decisions()]] - code - gateway/tests/test_approval_queue.py
- [[test_decide_already_decided()]] - code - gateway/tests/test_approval_queue.py
- [[test_decide_approval_approve()]] - code - gateway/tests/test_approval_queue.py
- [[test_decide_approval_reject()]] - code - gateway/tests/test_approval_queue.py
- [[test_decide_expired_request()]] - code - gateway/tests/test_approval_queue.py
- [[test_decide_nonexistent_request()]] - code - gateway/tests/test_approval_queue.py
- [[test_get_item()]] - code - gateway/tests/test_approval_queue.py
- [[test_get_item_nonexistent()]] - code - gateway/tests/test_approval_queue.py
- [[test_get_pending()]] - code - gateway/tests/test_approval_queue.py
- [[test_get_pending_excludes_decided()]] - code - gateway/tests/test_approval_queue.py
- [[test_request_expiration()]] - code - gateway/tests/test_approval_queue.py
- [[test_store_persists_submit_and_decision()]] - code - gateway/tests/test_approval_queue.py
- [[test_store_restores_items_on_init()]] - code - gateway/tests/test_approval_queue.py
- [[test_submit_approval_request()]] - code - gateway/tests/test_approval_queue.py
- [[test_websocket_disconnect()]] - code - gateway/tests/test_approval_queue.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Approval_Queue_Core
SORT file.name ASC
```

## Connections to other communities
- 25 edges to [[_COMMUNITY_Enhanced Approval Queue]]
- 9 edges to [[_COMMUNITY_SSH Proxy & Gateway Config]]
- 2 edges to [[_COMMUNITY_Module Group 216]]
- 2 edges to [[_COMMUNITY_Module Group 74]]
- 1 edge to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 1 edge to [[_COMMUNITY_Module Group 189]]

## Top bridge nodes
- [[ApprovalQueue]] - degree 37, connects to 4 communities
- [[test_approval_queue.py]] - degree 25, connects to 2 communities
- [[approval_queue()_1]] - degree 3, connects to 2 communities
- [[.decide()_1]] - degree 7, connects to 1 community
- [[test_store_persists_submit_and_decision()]] - degree 4, connects to 1 community