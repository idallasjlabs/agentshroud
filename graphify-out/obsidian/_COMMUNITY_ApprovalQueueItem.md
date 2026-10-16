---
type: community
cohesion: 0.07
members: 43
---

# ApprovalQueueItem

**Cohesion:** 0.07 - loosely connected
**Members:** 43 nodes

## Members
- [[dot-test_100_concurrent_submissions()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_concurrent_submit_and_decide()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_double_decide_raises()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_store_expires_old_items()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_store_persists_across_reopen()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_store_save_and_load()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_store_update_status()]] - code - gateway/tests/test_approval_stress.py
- [[100 concurrent approval requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[A pending approval request in the queue]] - rationale - gateway/ingest_api/models.py
- [[ApprovalQueueItem_1]] - code - gateway/tests/test_approval_store.py
- [[ApprovalQueueItem_2]] - code - gateway/ingest_api/models.py
- [[AuditStore same idempotency contract as ApprovalStore.]] - rationale - gateway/tests/test_approval_store.py
- [[Auto-expire old requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[Deciding an item persists the new status.]] - rationale - gateway/tests/test_approval_store.py
- [[Deciding on already-decided request raises ValueError.]] - rationale - gateway/tests/test_approval_stress.py
- [[Expired items are marked expired during load_pending.]] - rationale - gateway/tests/test_approval_store.py
- [[Items saved by one store instance are visible to another.]] - rationale - gateway/tests/test_approval_store.py
- [[Items saved to store can be reloaded.]] - rationale - gateway/tests/test_approval_stress.py
- [[Items survive store closereopen cycle.]] - rationale - gateway/tests/test_approval_stress.py
- [[Path_13]] - code - gateway/tests/test_approval_store.py
- [[Queue persistence across restart.]] - rationale - gateway/tests/test_approval_stress.py
- [[Re-initializing must not orphan the first aiosqlite connection.      aiosqlite c]] - rationale - gateway/tests/test_approval_store.py
- [[Simulates a full restart cycle save, close, reopen, verify.]] - rationale - gateway/tests/test_approval_store.py
- [[Status updates persist.]] - rationale - gateway/tests/test_approval_stress.py
- [[Store marks expired items on load.]] - rationale - gateway/tests/test_approval_stress.py
- [[Submit 100 requests concurrently — all should succeed.]] - rationale - gateway/tests/test_approval_stress.py
- [[Submit and decide requests concurrently.]] - rationale - gateway/tests/test_approval_stress.py
- [[TestApprovalStorePersistence]] - code - gateway/tests/test_approval_stress.py
- [[TestAutoExpire]] - code - gateway/tests/test_approval_stress.py
- [[TestConcurrentApprovalRequests]] - code - gateway/tests/test_approval_stress.py
- [[_make_item()]] - code - gateway/tests/test_approval_store.py
- [[queue()]] - code - gateway/tests/test_approval_stress.py
- [[store()_1]] - code - gateway/tests/test_approval_store.py
- [[store()_2]] - code - gateway/tests/test_approval_stress.py
- [[store.py]] - code - gateway/approval_queue/store.py
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
TABLE source_file, type FROM #community/ApprovalQueueItem
SORT file.name ASC
```

## Connections to other communities
- 32 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 8 edges to [[_COMMUNITY_ApprovalRequest]]
- 5 edges to [[_COMMUNITY_DataLedger]]
- 4 edges to [[_COMMUNITY_AuditStore]]
- 2 edges to [[_COMMUNITY_ingest_apimodels.py]]
- 2 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 2 edges to [[_COMMUNITY_First Time Setup]]
- 1 edge to [[_COMMUNITY_All Dependencies]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]
- 1 edge to [[_COMMUNITY_socrouter.py]]

## Top bridge nodes
- [[ApprovalQueueItem_2]] - degree 30, connects to 6 communities
- [[store.py]] - degree 7, connects to 5 communities
- [[test_approval_stress.py]] - degree 11, connects to 3 communities
- [[TestApprovalStorePersistence]] - degree 11, connects to 3 communities
- [[TestConcurrentApprovalRequests]] - degree 9, connects to 3 communities
