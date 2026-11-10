---
type: community
members: 75
---

# Community 108

**Members:** 75 nodes

## Members
- [[.__init__()_6]] - code - gateway/approval_queue/store.py
- [[._notify_telegram()]] - code - gateway/approval_queue/enhanced_queue.py
- [[._timeout_request()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.broadcast()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.close()_4]] - code - gateway/approval_queue/store.py
- [[.decide()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.get_item()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.get_pending()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.initialize()_1]] - code - gateway/approval_queue/store.py
- [[.load_all()]] - code - gateway/approval_queue/store.py
- [[.load_pending()]] - code - gateway/approval_queue/store.py
- [[.save()]] - code - gateway/approval_queue/store.py
- [[.submit()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.submit_tool_request()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.test_100_concurrent_submissions()]] - code - gateway/tests/test_approval_stress.py
- [[.test_store_expires_old_items()]] - code - gateway/tests/test_approval_stress.py
- [[.test_store_persists_across_reopen()]] - code - gateway/tests/test_approval_stress.py
- [[.test_store_save_and_load()]] - code - gateway/tests/test_approval_stress.py
- [[.test_store_update_status()]] - code - gateway/tests/test_approval_stress.py
- [[.update_status()]] - code - gateway/approval_queue/store.py
- [[100 concurrent approval requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[A pending approval request in the queue]] - rationale - gateway/ingest_api/models.py
- [[Add an action to the approval queue with policy-based timeout.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Any]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalQueueItem]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalQueueItem_2]] - code - gateway/approval_queue/store.py
- [[ApprovalQueueItem_3]] - code - gateway/ingest_api/models.py
- [[ApprovalQueueItem_4]] - code - gateway/tests/test_approval_store.py
- [[ApprovalRequest]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalStore_1]] - code - gateway/approval_queue/store.py
- [[AuditStore same idempotency contract as ApprovalStore.]] - rationale - gateway/tests/test_approval_store.py
- [[Auto-expire old requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[Close the database connection.]] - rationale - gateway/approval_queue/store.py
- [[Deciding an item persists the new status.]] - rationale - gateway/tests/test_approval_store.py
- [[Expired items are marked expired during load_pending.]] - rationale - gateway/tests/test_approval_store.py
- [[Fetch a single queue item by ID.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get all pending approval items.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Handle timeout for a pending request.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Insert or replace an approval item.]] - rationale - gateway/approval_queue/store.py
- [[Items saved by one store instance are visible to another.]] - rationale - gateway/tests/test_approval_store.py
- [[Items saved to store can be reloaded.]] - rationale - gateway/tests/test_approval_stress.py
- [[Items survive store closereopen cycle.]] - rationale - gateway/tests/test_approval_stress.py
- [[Load all items (for auditdebugging).]] - rationale - gateway/approval_queue/store.py
- [[Load all pending (non-expired, non-decided) items.          Items whose expires_]] - rationale - gateway/approval_queue/store.py
- [[Open the database and create the schema. Idempotent a second call         must]] - rationale - gateway/approval_queue/store.py
- [[Path]] - code - gateway/approval_queue/store.py
- [[Path_24]] - code - gateway/tests/test_approval_store.py
- [[Process an approval decision.          IEC 62443 FR1 approving a high-risk acti]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Queue persistence across restart.]] - rationale - gateway/tests/test_approval_stress.py
- [[Re-initializing must not orphan the first aiosqlite connection.      aiosqlite c]] - rationale - gateway/tests/test_approval_store.py
- [[SQLite-backed persistence for approval queue items.]] - rationale - gateway/approval_queue/store.py
- [[Send Telegram notification for approval requests.          Sends a formatted mes]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Send a JSON message to all connected WebSocket clients.          SCRUM-154 boun]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Simulates a full restart cycle save, close, reopen, verify.]] - rationale - gateway/tests/test_approval_store.py
- [[Status updates persist.]] - rationale - gateway/tests/test_approval_stress.py
- [[Store marks expired items on load.]] - rationale - gateway/tests/test_approval_stress.py
- [[Submit 100 requests concurrently — all should succeed.]] - rationale - gateway/tests/test_approval_stress.py
- [[Submit a tool call request for approval.          Args             tool_name T]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[TestApprovalStorePersistence]] - code - gateway/tests/test_approval_stress.py
- [[TestApprovalTimeout]] - code - gateway/tests/test_approval_stress.py
- [[TestAutoExpire]] - code - gateway/tests/test_approval_stress.py
- [[TestConcurrentApprovalRequests]] - code - gateway/tests/test_approval_stress.py
- [[Timeout handling for approval requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[Update the status of an existing item.]] - rationale - gateway/approval_queue/store.py
- [[_make_item()]] - code - gateway/tests/test_approval_store.py
- [[store()]] - code - gateway/tests/test_approval_store.py
- [[store()_1]] - code - gateway/tests/test_approval_stress.py
- [[test_approval_store.py]] - code - gateway/tests/test_approval_store.py
- [[test_approval_stress.py]] - code - gateway/tests/test_approval_stress.py
- [[test_audit_store_initialize_is_idempotent()]] - code - gateway/tests/test_approval_store.py
- [[test_decide_persists()]] - code - gateway/tests/test_approval_store.py
- [[test_expired_items_on_reload()]] - code - gateway/tests/test_approval_store.py
- [[test_initialize_is_idempotent()]] - code - gateway/tests/test_approval_store.py
- [[test_persist_and_reload()]] - code - gateway/tests/test_approval_store.py
- [[test_store_survives_restart()]] - code - gateway/tests/test_approval_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_108
SORT file.name ASC
```

## Connections to other communities
- 58 edges to [[_COMMUNITY_Community 30]]
- 12 edges to [[_COMMUNITY_Community 68]]
- 6 edges to [[_COMMUNITY_Community 70]]
- 6 edges to [[_COMMUNITY_Community 439]]
- 4 edges to [[_COMMUNITY_Community 35]]
- 4 edges to [[_COMMUNITY_Community 254]]
- 2 edges to [[_COMMUNITY_Community 1014]]
- 2 edges to [[_COMMUNITY_Community 72]]
- 2 edges to [[_COMMUNITY_Community 707]]
- 1 edge to [[_COMMUNITY_Community 10]]
- 1 edge to [[_COMMUNITY_Community 20]]
- 1 edge to [[_COMMUNITY_Community 329]]

## Top bridge nodes
- [[ApprovalStore_1]] - degree 60, connects to 6 communities
- [[ApprovalQueueItem_3]] - degree 30, connects to 5 communities
- [[ApprovalQueueItem]] - degree 12, connects to 3 communities
- [[test_approval_stress.py]] - degree 11, connects to 3 communities
- [[TestApprovalStorePersistence]] - degree 11, connects to 3 communities