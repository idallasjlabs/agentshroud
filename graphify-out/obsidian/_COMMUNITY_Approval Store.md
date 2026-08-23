---
type: community
cohesion: 0.19
members: 17
---

# Approval Store

**Cohesion:** 0.19 - loosely connected
**Members:** 17 nodes

## Members
- [[ApprovalQueueItem_4]] - code - gateway/tests/test_approval_store.py
- [[AuditStore same idempotency contract as ApprovalStore.]] - rationale - gateway/tests/test_approval_store.py
- [[Deciding an item persists the new status.]] - rationale - gateway/tests/test_approval_store.py
- [[Expired items are marked expired during load_pending.]] - rationale - gateway/tests/test_approval_store.py
- [[Items saved by one store instance are visible to another.]] - rationale - gateway/tests/test_approval_store.py
- [[Path_24]] - code - gateway/tests/test_approval_store.py
- [[Re-initializing must not orphan the first aiosqlite connection.      aiosqlite c]] - rationale - gateway/tests/test_approval_store.py
- [[Simulates a full restart cycle save, close, reopen, verify.]] - rationale - gateway/tests/test_approval_store.py
- [[_make_item()]] - code - gateway/tests/test_approval_store.py
- [[store()]] - code - gateway/tests/test_approval_store.py
- [[test_approval_store.py]] - code - gateway/tests/test_approval_store.py
- [[test_audit_store_initialize_is_idempotent()]] - code - gateway/tests/test_approval_store.py
- [[test_decide_persists()]] - code - gateway/tests/test_approval_store.py
- [[test_expired_items_on_reload()]] - code - gateway/tests/test_approval_store.py
- [[test_initialize_is_idempotent()]] - code - gateway/tests/test_approval_store.py
- [[test_persist_and_reload()]] - code - gateway/tests/test_approval_store.py
- [[test_store_survives_restart()]] - code - gateway/tests/test_approval_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Approval_Store
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Enhanced Approval]]
- 4 edges to [[_COMMUNITY_Queue (approval_queue)]]
- 4 edges to [[_COMMUNITY_Audit Export]]

## Top bridge nodes
- [[test_approval_store.py]] - degree 11, connects to 3 communities
- [[Path_24]] - degree 10, connects to 3 communities
- [[ApprovalQueueItem_4]] - degree 4, connects to 3 communities
- [[_make_item()]] - degree 7, connects to 1 community
- [[test_decide_persists()]] - degree 5, connects to 1 community