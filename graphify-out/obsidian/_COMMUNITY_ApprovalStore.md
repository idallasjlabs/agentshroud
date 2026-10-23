---
type: community
cohesion: 0.08
members: 37
---

# ApprovalStore

**Cohesion:** 0.08 - loosely connected
**Members:** 37 nodes

## Members
- [[dot-__init__()_92]] - code - gateway/approval_queue/store.py
- [[dot-close()_9]] - code - gateway/approval_queue/store.py
- [[dot-initialize()]] - code - gateway/approval_queue/store.py
- [[dot-load_all()]] - code - gateway/approval_queue/store.py
- [[dot-load_pending()]] - code - gateway/approval_queue/store.py
- [[dot-save()_1]] - code - gateway/approval_queue/store.py
- [[dot-test_store_persists_across_reopen()]] - code - gateway/tests/test_approval_stress.py
- [[dot-update_status()]] - code - gateway/approval_queue/store.py
- [[ApprovalQueueItem]] - code - gateway/approval_queue/store.py
- [[ApprovalQueueItem_1]] - code - gateway/tests/test_approval_store.py
- [[ApprovalStore]] - code - gateway/approval_queue/store.py
- [[AuditStore same idempotency contract as ApprovalStore.]] - rationale - gateway/tests/test_approval_store.py
- [[Close the database connection.]] - rationale - gateway/approval_queue/store.py
- [[Deciding an item persists the new status.]] - rationale - gateway/tests/test_approval_store.py
- [[Expired items are marked expired during load_pending.]] - rationale - gateway/tests/test_approval_store.py
- [[Insert or replace an approval item.]] - rationale - gateway/approval_queue/store.py
- [[Items saved by one store instance are visible to another.]] - rationale - gateway/tests/test_approval_store.py
- [[Items survive store closereopen cycle.]] - rationale - gateway/tests/test_approval_stress.py
- [[Load all items (for auditdebugging).]] - rationale - gateway/approval_queue/store.py
- [[Load all pending (non-expired, non-decided) items.          Items whose expires_]] - rationale - gateway/approval_queue/store.py
- [[Open the database and create the schema. Idempotent a second call         must]] - rationale - gateway/approval_queue/store.py
- [[Path_23]] - code - gateway/approval_queue/store.py
- [[Path_24]] - code - gateway/tests/test_approval_store.py
- [[Re-initializing must not orphan the first aiosqlite connection.      aiosqlite c]] - rationale - gateway/tests/test_approval_store.py
- [[SQLite-backed persistence for approval queue items.]] - rationale - gateway/approval_queue/store.py
- [[Simulates a full restart cycle save, close, reopen, verify.]] - rationale - gateway/tests/test_approval_store.py
- [[Update the status of an existing item.]] - rationale - gateway/approval_queue/store.py
- [[_make_item()]] - code - gateway/tests/test_approval_store.py
- [[store()_1]] - code - gateway/tests/test_approval_store.py
- [[store()_2]] - code - gateway/tests/test_approval_stress.py
- [[test_approval_store.py]] - code - gateway/tests/test_approval_store.py
- [[test_audit_store_initialize_is_idempotent()]] - code - gateway/tests/test_approval_store.py
- [[test_decide_persists()]] - code - gateway/tests/test_approval_store.py
- [[test_expired_items_on_reload()]] - code - gateway/tests/test_approval_store.py
- [[test_initialize_is_idempotent()]] - code - gateway/tests/test_approval_store.py
- [[test_persist_and_reload()]] - code - gateway/tests/test_approval_store.py
- [[test_store_survives_restart()]] - code - gateway/tests/test_approval_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalStore
SORT file.name ASC
```

## Connections to other communities
- 29 edges to [[_COMMUNITY_ContextSegment]]
- 7 edges to [[_COMMUNITY_MiddlewareManager (3)]]
- 5 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 4 edges to [[_COMMUNITY_test_voice_latency_guard.py]]
- 4 edges to [[_COMMUNITY_AlertDispatcher (5)]]
- 1 edge to [[_COMMUNITY_Phase 2 — Security Core (HMAC Auth + PII Sanitizer, HTTP CONNECT Proxy, Approval Queue)]]

## Top bridge nodes
- [[ApprovalStore]] - degree 58, connects to 5 communities
- [[test_approval_store.py]] - degree 11, connects to 2 communities
- [[Path_24]] - degree 10, connects to 2 communities
- [[ApprovalQueueItem_1]] - degree 4, connects to 2 communities
- [[dot-test_store_persists_across_reopen()]] - degree 4, connects to 2 communities
