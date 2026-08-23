---
type: community
cohesion: 0.04
members: 74
---

# Queue (approval_queue)

**Cohesion:** 0.04 - loosely connected
**Members:** 74 nodes

## Members
- [[NOTE Called within _lock context]] - rationale - gateway/approval_queue/queue.py
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
- [[.test_100_concurrent_submissions()]] - code - gateway/tests/test_approval_stress.py
- [[.test_concurrent_submit_and_decide()]] - code - gateway/tests/test_approval_stress.py
- [[.test_double_decide_raises()]] - code - gateway/tests/test_approval_stress.py
- [[.test_expired_request_cannot_be_decided()]] - code - gateway/tests/test_approval_stress.py
- [[.test_get_pending_expires_stale()]] - code - gateway/tests/test_approval_stress.py
- [[.test_store_expires_old_items()]] - code - gateway/tests/test_approval_stress.py
- [[.test_store_persists_across_reopen()]] - code - gateway/tests/test_approval_stress.py
- [[.test_store_save_and_load()]] - code - gateway/tests/test_approval_stress.py
- [[.test_store_update_status()]] - code - gateway/tests/test_approval_stress.py
- [[100 concurrent approval requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[A pending approval request in the queue]] - rationale - gateway/ingest_api/models.py
- [[Accept a WebSocket connection and add to connected set          Args]] - rationale - gateway/approval_queue/queue.py
- [[Add an action to the approval queue          Args             request Approval]] - rationale - gateway/approval_queue/queue.py
- [[AgentShroud Security Dashboard (index.html)]] - code - gateway/dashboard/index.html
- [[Any_2]] - code - gateway/approval_queue/queue.py
- [[ApprovalQueue]] - code - gateway/approval_queue/queue.py
- [[ApprovalQueueConfig_1]] - code - gateway/approval_queue/queue.py
- [[ApprovalQueueItem_1]] - code - gateway/approval_queue/queue.py
- [[ApprovalQueueItem_3]] - code - gateway/ingest_api/models.py
- [[ApprovalRequest_2]] - code - gateway/approval_queue/queue.py
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
- [[Items survive store closereopen cycle.]] - rationale - gateway/tests/test_approval_stress.py
- [[Load queue items from store file when present.]] - rationale - gateway/approval_queue/queue.py
- [[MFAGuard_1]] - code - gateway/approval_queue/queue.py
- [[MFAGuard.verify()]] - code - gateway/security/mfa_guard.py
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
- [[WebSocket_1]] - code - gateway/approval_queue/queue.py
- [[approval_queue()]] - code - gateway/tests/test_approval_queue.py
- [[approval_queue()_1]] - code - gateway/tests/test_security_integration.py
- [[get_pending should expire stale items.]] - rationale - gateway/tests/test_approval_stress.py
- [[queue()]] - code - gateway/tests/test_approval_stress.py
- [[queue.py]] - code - gateway/approval_queue/queue.py
- [[store()_1]] - code - gateway/tests/test_approval_stress.py
- [[test_approval_stress.py]] - code - gateway/tests/test_approval_stress.py
- [[test_store_restores_items_on_init()]] - code - gateway/tests/test_approval_queue.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Queue_approval_queue
SORT file.name ASC
```

## Connections to other communities
- 26 edges to [[_COMMUNITY_Enhanced Approval]]
- 17 edges to [[_COMMUNITY_Approval Queue]]
- 13 edges to [[_COMMUNITY_Security Fixes & SSH Write Endpoint]]
- 7 edges to [[_COMMUNITY_Mfa Guard]]
- 4 edges to [[_COMMUNITY_Aiosqlite (05 - Dependencies)]]
- 4 edges to [[_COMMUNITY_Approval Store]]
- 3 edges to [[_COMMUNITY_Ssh Write File Endpoint]]
- 2 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 1 edge to [[_COMMUNITY_Router (soc)]]
- 1 edge to [[_COMMUNITY_Daily Cve Report (security)]]
- 1 edge to [[_COMMUNITY_SOC Router Coverage]]
- 1 edge to [[_COMMUNITY_Config]]
- 1 edge to [[_COMMUNITY_Icon 64x64 (app)]]
- 1 edge to [[_COMMUNITY_Ssh Proxy]]
- 1 edge to [[_COMMUNITY_Soc Services Coverage]]
- 1 edge to [[_COMMUNITY_Soc Egress Endpoints]]

## Top bridge nodes
- [[queue.py]] - degree 16, connects to 8 communities
- [[ApprovalQueue]] - degree 51, connects to 6 communities
- [[ApprovalQueueItem_3]] - degree 30, connects to 5 communities
- [[test_approval_stress.py]] - degree 11, connects to 2 communities
- [[TestApprovalStorePersistence]] - degree 11, connects to 2 communities