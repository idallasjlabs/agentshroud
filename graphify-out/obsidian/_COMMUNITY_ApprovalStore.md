---
type: community
members: 96
---

# ApprovalStore

**Members:** 96 nodes

## Members
- [[dot-__init__()_157]] - code - gateway/approval_queue/store.py
- [[dot-_append_audit_event()]] - code - gateway/approval_queue/queue.py
- [[dot-_expire_stale()]] - code - gateway/approval_queue/queue.py
- [[dot-_persist_pending_store()]] - code - gateway/approval_queue/queue.py
- [[dot-broadcast()_1]] - code - gateway/approval_queue/queue.py
- [[dot-cleanup_decided()]] - code - gateway/approval_queue/queue.py
- [[dot-close()_13]] - code - gateway/approval_queue/store.py
- [[dot-decide()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-decide()_1]] - code - gateway/approval_queue/queue.py
- [[dot-get_item()_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-get_item()_2]] - code - gateway/approval_queue/queue.py
- [[dot-get_pending()_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-get_pending()_2]] - code - gateway/approval_queue/queue.py
- [[dot-initialize()_2]] - code - gateway/approval_queue/store.py
- [[dot-load_all()]] - code - gateway/approval_queue/store.py
- [[dot-load_pending()]] - code - gateway/approval_queue/store.py
- [[dot-save()_1]] - code - gateway/approval_queue/store.py
- [[dot-submit()_1]] - code - gateway/approval_queue/queue.py
- [[dot-test_100_concurrent_submissions()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_concurrent_submit_and_decide()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_double_decide_raises()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_expired_request_cannot_be_decided()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_get_pending_expires_stale()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_store_expires_old_items()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_store_persists_across_reopen()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_store_save_and_load()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_store_update_status()]] - code - gateway/tests/test_approval_stress.py
- [[dot-update_status()]] - code - gateway/approval_queue/store.py
- [[100 concurrent approval requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[A pending approval request in the queue]] - rationale - gateway/ingest_api/models.py
- [[Add an action to the approval queue Args request Approval request from agent…]] - rationale - gateway/approval_queue/queue.py
- [[Any_59]] - code
- [[Approval Queue Stress Tests — concurrent requests and timeouts.]] - rationale - gateway/tests/test_approval_stress.py
- [[ApprovalQueueItem]] - code - gateway/ingest_api/models.py
- [[ApprovalStore]] - code - gateway/approval_queue/store.py
- [[AuditStore same idempotency contract as ApprovalStore.]] - rationale - gateway/tests/test_approval_store.py
- [[Auto-expire old requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[Best-effort JSONL persistence for queue lifecycle events.]] - rationale - gateway/approval_queue/queue.py
- [[Check all pending items and expire those past timeout Returns List of expired…]] - rationale - gateway/approval_queue/queue.py
- [[Close the database connection.]] - rationale - gateway/approval_queue/store.py
- [[Deciding an item persists the new status.]] - rationale - gateway/tests/test_approval_store.py
- [[Deciding on already-decided request raises ValueError.]] - rationale - gateway/tests/test_approval_stress.py
- [[Expired items are marked expired during load_pending.]] - rationale - gateway/tests/test_approval_store.py
- [[Expired request raises ValueError on decide.]] - rationale - gateway/tests/test_approval_stress.py
- [[Fetch a single queue item by ID Args request_id Request UUID Returns…]] - rationale - gateway/approval_queue/queue.py
- [[Fetch a single queue item by ID.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get all pending (not expired, not decided) items First expires any stale items.…]] - rationale - gateway/approval_queue/queue.py
- [[Get all pending approval items.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Insert or replace an approval item.]] - rationale - gateway/approval_queue/store.py
- [[Items saved by one store instance are visible to another.]] - rationale - gateway/tests/test_approval_store.py
- [[Items saved to store can be reloaded.]] - rationale - gateway/tests/test_approval_stress.py
- [[Items survive store closereopen cycle.]] - rationale - gateway/tests/test_approval_stress.py
- [[Load all items (for auditdebugging).]] - rationale - gateway/approval_queue/store.py
- [[Load all pending (non-expired, non-decided) items. Items whose expires_at is in…]] - rationale - gateway/approval_queue/store.py
- [[Open the database and create the schema. Idempotent a second call must not…]] - rationale - gateway/approval_queue/store.py
- [[Path_52]] - code
- [[Path_53]] - code
- [[Persist queue items to disk for restart durability (best effort). Uses atomic…]] - rationale - gateway/approval_queue/queue.py
- [[Process an approval decision Args request_id Request UUID approved Whether…]] - rationale - gateway/approval_queue/queue.py
- [[Process an approval decision. IEC 62443 FR1 approving a high-risk action…]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Queue persistence across restart.]] - rationale - gateway/tests/test_approval_stress.py
- [[Re-initializing must not orphan the first aiosqlite connection. aiosqlite…_1]] - rationale - gateway/tests/test_approval_store.py
- [[Remove decided (approvedrejectedexpired) items older than max_age_seconds.…]] - rationale - gateway/approval_queue/queue.py
- [[SQLite-backed persistence for approval queue items.]] - rationale - gateway/approval_queue/store.py
- [[Send a JSON message to all connected WebSocket clients Silently removes clients…]] - rationale - gateway/approval_queue/queue.py
- [[Simulates a full restart cycle save, close, reopen, verify.]] - rationale - gateway/tests/test_approval_store.py
- [[Status updates persist.]] - rationale - gateway/tests/test_approval_stress.py
- [[Store marks expired items on load.]] - rationale - gateway/tests/test_approval_stress.py
- [[Submit 100 requests concurrently — all should succeed.]] - rationale - gateway/tests/test_approval_stress.py
- [[Submit and decide requests concurrently.]] - rationale - gateway/tests/test_approval_stress.py
- [[TestApprovalStorePersistence]] - code - gateway/tests/test_approval_stress.py
- [[TestApprovalTimeout]] - code - gateway/tests/test_approval_stress.py
- [[TestAutoExpire]] - code - gateway/tests/test_approval_stress.py
- [[TestConcurrentApprovalRequests]] - code - gateway/tests/test_approval_stress.py
- [[Tests for SQLite-backed approval queue persistence.]] - rationale - gateway/tests/test_approval_store.py
- [[Timeout handling for approval requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[Update the status of an existing item.]] - rationale - gateway/approval_queue/store.py
- [[_make_item()]] - code - gateway/tests/test_approval_store.py
- [[asyncio_56]] - code
- [[asyncio_57]] - code
- [[decide()]] - code - gateway/tests/test_approval_stress.py
- [[fixture_102]] - code
- [[fixture_103]] - code
- [[get_pending should expire stale items.]] - rationale - gateway/tests/test_approval_stress.py
- [[queue()]] - code - gateway/tests/test_approval_stress.py
- [[store()_2]] - code - gateway/tests/test_approval_store.py
- [[store()_3]] - code - gateway/tests/test_approval_stress.py
- [[submit_one()]] - code - gateway/tests/test_approval_stress.py
- [[test_approval_store.py]] - code - gateway/tests/test_approval_store.py
- [[test_approval_stress.py]] - code - gateway/tests/test_approval_stress.py
- [[test_audit_store_initialize_is_idempotent()]] - code - gateway/tests/test_approval_store.py
- [[test_decide_persists()]] - code - gateway/tests/test_approval_store.py
- [[test_expired_items_on_reload()]] - code - gateway/tests/test_approval_store.py
- [[test_initialize_is_idempotent()_1]] - code - gateway/tests/test_approval_store.py
- [[test_persist_and_reload()]] - code - gateway/tests/test_approval_store.py
- [[test_store_survives_restart()]] - code - gateway/tests/test_approval_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalStore
SORT file.name ASC
```

## Connections to other communities
- 33 edges to [[_COMMUNITY_EnhancedApprovalQueue]]
- 15 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 10 edges to [[_COMMUNITY_ApprovalRequest]]
- 4 edges to [[_COMMUNITY_ingest_apimodels.py]]
- 2 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 2 edges to [[_COMMUNITY_test_soc_router_coverage.py]]
- 2 edges to [[_COMMUNITY_AuditStore]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_load_config]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[ApprovalStore]] - degree 44, connects to 5 communities
- [[ApprovalQueueItem]] - degree 32, connects to 5 communities
- [[test_approval_stress.py]] - degree 17, connects to 4 communities
- [[test_approval_store.py]] - degree 14, connects to 3 communities
- [[dot-submit()_1]] - degree 7, connects to 2 communities
