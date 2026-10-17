---
type: community
members: 66
---

# UserSessionManager (2)

**Members:** 66 nodes

## Members
- [[dot-__init__()_197]] - code - gateway/approval_queue/queue.py
- [[dot-_append_audit_event()]] - code - gateway/approval_queue/queue.py
- [[dot-_expire_stale()]] - code - gateway/approval_queue/queue.py
- [[dot-_load_pending_store()]] - code - gateway/approval_queue/queue.py
- [[dot-_persist_pending_store()]] - code - gateway/approval_queue/queue.py
- [[dot-broadcast()_1]] - code - gateway/approval_queue/queue.py
- [[dot-cleanup_decided()]] - code - gateway/approval_queue/queue.py
- [[dot-connect()_2]] - code - gateway/approval_queue/queue.py
- [[dot-decide()_1]] - code - gateway/approval_queue/queue.py
- [[dot-disconnect()_1]] - code - gateway/approval_queue/queue.py
- [[dot-get_item()_2]] - code - gateway/approval_queue/queue.py
- [[dot-get_pending()_1]] - code - gateway/approval_queue/queue.py
- [[dot-submit()_1]] - code - gateway/approval_queue/queue.py
- [[dot-test_100_concurrent_submissions()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_concurrent_submit_and_decide()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_double_decide_raises()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_expired_request_cannot_be_decided()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_get_pending_expires_stale()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_store_expires_old_items()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_store_save_and_load()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_store_update_status()]] - code - gateway/tests/test_approval_stress.py
- [[100 concurrent approval requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[Accept a WebSocket connection and add to connected set          Args]] - rationale - gateway/approval_queue/queue.py
- [[Add an action to the approval queue          Args             request Approval]] - rationale - gateway/approval_queue/queue.py
- [[Any_80]] - code - gateway/approval_queue/queue.py
- [[ApprovalQueue_1]] - code - gateway/approval_queue/queue.py
- [[ApprovalQueueConfig_2]] - code - gateway/approval_queue/queue.py
- [[ApprovalQueueItem_4]] - code - gateway/approval_queue/queue.py
- [[ApprovalRequest_5]] - code - gateway/approval_queue/queue.py
- [[Auto-expire old requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[Best-effort JSONL persistence for queue lifecycle events.]] - rationale - gateway/approval_queue/queue.py
- [[Check all pending items and expire those past timeout          Returns]] - rationale - gateway/approval_queue/queue.py
- [[Create approval queue instance for testing]] - rationale - gateway/tests/test_approval_queue.py
- [[Deciding on already-decided request raises ValueError.]] - rationale - gateway/tests/test_approval_stress.py
- [[Expired request raises ValueError on decide.]] - rationale - gateway/tests/test_approval_stress.py
- [[Fetch a single queue item by ID          Args             request_id Request U]] - rationale - gateway/approval_queue/queue.py
- [[Get all pending (not expired, not decided) items          First expires any stal]] - rationale - gateway/approval_queue/queue.py
- [[In-memory approval queue with WebSocket notifications      Actions requiring app]] - rationale - gateway/approval_queue/queue.py
- [[Initialize approval queue          Args             config Approval queue conf]] - rationale - gateway/approval_queue/queue.py
- [[Items saved to store can be reloaded.]] - rationale - gateway/tests/test_approval_stress.py
- [[Load queue items from store file when present.]] - rationale - gateway/approval_queue/queue.py
- [[MFAGuard_2]] - code - gateway/approval_queue/queue.py
- [[Persist queue items to disk for restart durability (best effort).          Uses]] - rationale - gateway/approval_queue/queue.py
- [[Process an approval decision          Args             request_id Request UUID]] - rationale - gateway/approval_queue/queue.py
- [[Queue persistence across restart.]] - rationale - gateway/tests/test_approval_stress.py
- [[Queue should restore persisted items from store file on startup.]] - rationale - gateway/tests/test_approval_queue.py
- [[Remove a WebSocket connection from connected set          Args             webs]] - rationale - gateway/approval_queue/queue.py
- [[Remove decided (approvedrejectedexpired) items older than max_age_seconds.]] - rationale - gateway/approval_queue/queue.py
- [[Send a JSON message to all connected WebSocket clients          Silently removes]] - rationale - gateway/approval_queue/queue.py
- [[Status updates persist.]] - rationale - gateway/tests/test_approval_stress.py
- [[Store marks expired items on load.]] - rationale - gateway/tests/test_approval_stress.py
- [[Submit 100 requests concurrently — all should succeed.]] - rationale - gateway/tests/test_approval_stress.py
- [[Submit and decide requests concurrently.]] - rationale - gateway/tests/test_approval_stress.py
- [[TestApprovalStorePersistence]] - code - gateway/tests/test_approval_stress.py
- [[TestApprovalTimeout]] - code - gateway/tests/test_approval_stress.py
- [[TestAutoExpire]] - code - gateway/tests/test_approval_stress.py
- [[TestConcurrentApprovalRequests]] - code - gateway/tests/test_approval_stress.py
- [[Timeout handling for approval requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[WebSocket_7]] - code - gateway/approval_queue/queue.py
- [[approval_queue()]] - code - gateway/tests/test_approval_queue.py
- [[approval_queue()_1]] - code - gateway/tests/test_security_integration.py
- [[get_pending should expire stale items.]] - rationale - gateway/tests/test_approval_stress.py
- [[queue()]] - code - gateway/tests/test_approval_stress.py
- [[store()_2]] - code - gateway/tests/test_approval_stress.py
- [[test_approval_stress.py]] - code - gateway/tests/test_approval_stress.py
- [[test_store_restores_items_on_init()]] - code - gateway/tests/test_approval_queue.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/UserSessionManager_2
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 16 edges to [[_COMMUNITY_ApprovalQueueConfig (3)_1]]
- 8 edges to [[_COMMUNITY_ApprovalQueueConfig (2)_1]]
- 7 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 5 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig (3)]]
- 1 edge to [[_COMMUNITY_ServiceManager]]

## Top bridge nodes
- [[ApprovalQueue_1]] - degree 51, connects to 6 communities
- [[test_approval_stress.py]] - degree 11, connects to 2 communities
- [[TestApprovalStorePersistence]] - degree 11, connects to 2 communities
- [[TestApprovalTimeout]] - degree 9, connects to 2 communities
- [[TestConcurrentApprovalRequests]] - degree 9, connects to 2 communities
