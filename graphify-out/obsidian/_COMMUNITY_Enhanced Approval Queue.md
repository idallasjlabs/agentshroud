---
type: community
cohesion: 0.03
members: 160
---

# Enhanced Approval Queue

**Cohesion:** 0.03 - loosely connected
**Members:** 160 nodes

## Members
- [[NOTE Called within _lock context]] - rationale - gateway/approval_queue/queue.py
- [[.__init__()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.__init__()_2]] - code - gateway/approval_queue/store.py
- [[._notify_telegram()]] - code - gateway/approval_queue/enhanced_queue.py
- [[._schedule_timeout()]] - code - gateway/approval_queue/enhanced_queue.py
- [[._timeout_request()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.broadcast()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.close()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.close()_1]] - code - gateway/approval_queue/store.py
- [[.connect()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.decide()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.disconnect()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.get_item()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.get_pending()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.get_policy_for_tier()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.get_tool_risk_tier()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.initialize()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.initialize()_1]] - code - gateway/approval_queue/store.py
- [[.load_all()]] - code - gateway/approval_queue/store.py
- [[.load_pending()]] - code - gateway/approval_queue/store.py
- [[.requires_approval()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.save()]] - code - gateway/approval_queue/store.py
- [[.submit()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.submit_tool_request()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.test_100_concurrent_submissions()]] - code - gateway/tests/test_approval_stress.py
- [[.test_concurrent_submit_and_decide()]] - code - gateway/tests/test_approval_stress.py
- [[.test_critical_tool_approval_flow()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_critical_tool_denial_flow()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_critical_tool_requires_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_double_decide_raises()]] - code - gateway/tests/test_approval_stress.py
- [[.test_enforce_mode_disabled()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_expired_request_cannot_be_decided()]] - code - gateway/tests/test_approval_stress.py
- [[.test_get_pending_expires_stale()]] - code - gateway/tests/test_approval_stress.py
- [[.test_get_tool_risk_tier()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_low_risk_tool_no_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_requires_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_restore_pending_items()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_store_expires_old_items()]] - code - gateway/tests/test_approval_stress.py
- [[.test_store_persists_across_reopen()]] - code - gateway/tests/test_approval_stress.py
- [[.test_store_save_and_load()]] - code - gateway/tests/test_approval_stress.py
- [[.test_store_update_status()]] - code - gateway/tests/test_approval_stress.py
- [[.test_timeout_auto_deny()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_wait_for_decision()]] - code - gateway/tests/test_enhanced_approval.py
- [[.update_status()]] - code - gateway/approval_queue/store.py
- [[.wait_for_decision()]] - code - gateway/approval_queue/enhanced_queue.py
- [[100 concurrent approval requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[A pending approval request in the queue]] - rationale - gateway/ingest_api/models.py
- [[Accept a WebSocket connection and add to connected set.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Add an action to the approval queue with policy-based timeout.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Any]] - code - gateway/approval_queue/enhanced_queue.py
- [[Approval queue configuration]] - rationale - gateway/ingest_api/config.py
- [[ApprovalQueueConfig]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalQueueConfig_2]] - code - gateway/ingest_api/config.py
- [[ApprovalQueueItem]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalQueueItem_2]] - code - gateway/approval_queue/store.py
- [[ApprovalQueueItem_4]] - code - gateway/tests/test_approval_store.py
- [[ApprovalQueueItem_3]] - code - gateway/ingest_api/models.py
- [[ApprovalRequest]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalRequest_2]] - code - gateway/ingest_api/models.py
- [[ApprovalStore_1]] - code - gateway/approval_queue/store.py
- [[ApprovalStore]] - code - gateway/approval_queue/enhanced_queue.py
- [[AuditStore same idempotency contract as ApprovalStore.]] - rationale - gateway/tests/test_approval_store.py
- [[Auto-expire old requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[Check if a tool requires approval based on risk tier and policy.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Close the database connection.]] - rationale - gateway/approval_queue/store.py
- [[Close the store and cancel timeout tasks.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Create a temporary SQLite store for testing.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Create a test tool risk configuration.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Create an enhanced approval queue for testing.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Deciding an item persists the new status.]] - rationale - gateway/tests/test_approval_store.py
- [[Deciding on already-decided request raises ValueError.]] - rationale - gateway/tests/test_approval_stress.py
- [[Enhanced approval queue with enforce mode and tool risk tiers.      Features]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[EnhancedApprovalQueue]] - code - gateway/approval_queue/enhanced_queue.py
- [[Expired items are marked expired during load_pending.]] - rationale - gateway/tests/test_approval_store.py
- [[Expired request raises ValueError on decide.]] - rationale - gateway/tests/test_approval_stress.py
- [[Fetch a single queue item by ID.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get all pending approval items.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get the policy for a risk tier.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get the risk tier for a tool.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Handle timeout for a pending request.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Initialize enhanced approval queue.          Args             config Basic app]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Initialize the store and restore pending items.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Insert or replace an approval item.]] - rationale - gateway/approval_queue/store.py
- [[Items saved by one store instance are visible to another.]] - rationale - gateway/tests/test_approval_store.py
- [[Items saved to store can be reloaded.]] - rationale - gateway/tests/test_approval_stress.py
- [[Items survive store closereopen cycle.]] - rationale - gateway/tests/test_approval_stress.py
- [[Load all items (for auditdebugging).]] - rationale - gateway/approval_queue/store.py
- [[Load all pending (non-expired, non-decided) items.          Items whose expires_]] - rationale - gateway/approval_queue/store.py
- [[Open the database and create the schema. Idempotent a second call         must]] - rationale - gateway/approval_queue/store.py
- [[Path]] - code - gateway/approval_queue/store.py
- [[Path_20]] - code - gateway/tests/test_approval_store.py
- [[Process an approval decision.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Queue persistence across restart.]] - rationale - gateway/tests/test_approval_stress.py
- [[Re-initializing must not orphan the first aiosqlite connection.      aiosqlite c]] - rationale - gateway/tests/test_approval_store.py
- [[Remove a WebSocket connection from connected set.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Request for human approval of a sensitive action      Submitted by an agent when]] - rationale - gateway/ingest_api/models.py
- [[Risk policy configuration for a tool tier]] - rationale - gateway/ingest_api/config.py
- [[SQLite-backed persistence for approval queue items.]] - rationale - gateway/approval_queue/store.py
- [[Schedule a timeout task for a request.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Send Telegram notification for approval requests.          Sends a formatted mes]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Send a JSON message to all connected WebSocket clients.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Simulates a full restart cycle save, close, reopen, verify.]] - rationale - gateway/tests/test_approval_store.py
- [[Status updates persist.]] - rationale - gateway/tests/test_approval_stress.py
- [[Store marks expired items on load.]] - rationale - gateway/tests/test_approval_stress.py
- [[Submit 100 requests concurrently — all should succeed.]] - rationale - gateway/tests/test_approval_stress.py
- [[Submit a tool call request for approval.          Returns             (request_]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Submit and decide requests concurrently.]] - rationale - gateway/tests/test_approval_stress.py
- [[Test MCP proxy integration with approval queue.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test SQLite persistence across restarts.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test approval requirement logic.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test denial flow for critical tool.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test full approval flow for critical tool.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test risk tier lookup.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that approval events are generated for WebSocket notification.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that approval is bypassed when enforce mode is disabled.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that critical tools are identified as requiring approval.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that low-risk tools don't require approval.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that pending items are restored after restart.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test the complete approval workflow.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test timeout with auto-deny.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test tool risk tier classification.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test waiting for approval decision.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[TestApprovalStorePersistence]] - code - gateway/tests/test_approval_stress.py
- [[TestApprovalTimeout]] - code - gateway/tests/test_approval_stress.py
- [[TestApprovalWorkflow]] - code - gateway/tests/test_enhanced_approval.py
- [[TestAutoExpire]] - code - gateway/tests/test_approval_stress.py
- [[TestConcurrentApprovalRequests]] - code - gateway/tests/test_approval_stress.py
- [[TestMCPProxyIntegration]] - code - gateway/tests/test_enhanced_approval.py
- [[TestPersistence]] - code - gateway/tests/test_enhanced_approval.py
- [[TestToolRiskClassification]] - code - gateway/tests/test_enhanced_approval.py
- [[Timeout handling for approval requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[Tool risk tier configuration]] - rationale - gateway/ingest_api/config.py
- [[ToolRiskConfig_1]] - code - gateway/ingest_api/config.py
- [[ToolRiskConfig]] - code - gateway/approval_queue/enhanced_queue.py
- [[ToolRiskPolicy_1]] - code - gateway/ingest_api/config.py
- [[ToolRiskPolicy]] - code - gateway/approval_queue/enhanced_queue.py
- [[Update the status of an existing item.]] - rationale - gateway/approval_queue/store.py
- [[Wait for an approval decision.          Returns             True if approved, F]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[WebSocket]] - code - gateway/approval_queue/enhanced_queue.py
- [[_make_item()]] - code - gateway/tests/test_approval_store.py
- [[enhanced_queue()]] - code - gateway/tests/test_enhanced_approval.py
- [[enhanced_queue.py]] - code - gateway/approval_queue/enhanced_queue.py
- [[get_pending should expire stale items.]] - rationale - gateway/tests/test_approval_stress.py
- [[queue()]] - code - gateway/tests/test_approval_stress.py
- [[queue.py]] - code - gateway/approval_queue/queue.py
- [[store()]] - code - gateway/tests/test_approval_store.py
- [[store()_1]] - code - gateway/tests/test_approval_stress.py
- [[store.py]] - code - gateway/approval_queue/store.py
- [[temp_store()]] - code - gateway/tests/test_enhanced_approval.py
- [[test_approval_store.py]] - code - gateway/tests/test_approval_store.py
- [[test_approval_stress.py]] - code - gateway/tests/test_approval_stress.py
- [[test_audit_store_initialize_is_idempotent()]] - code - gateway/tests/test_approval_store.py
- [[test_decide_persists()]] - code - gateway/tests/test_approval_store.py
- [[test_enhanced_approval.py]] - code - gateway/tests/test_enhanced_approval.py
- [[test_expired_items_on_reload()]] - code - gateway/tests/test_approval_store.py
- [[test_initialize_is_idempotent()]] - code - gateway/tests/test_approval_store.py
- [[test_persist_and_reload()]] - code - gateway/tests/test_approval_store.py
- [[test_store_survives_restart()]] - code - gateway/tests/test_approval_store.py
- [[test_websocket_notifications()]] - code - gateway/tests/test_enhanced_approval.py
- [[tool_risk_config()]] - code - gateway/tests/test_enhanced_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Enhanced_Approval_Queue
SORT file.name ASC
```

## Connections to other communities
- 26 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 25 edges to [[_COMMUNITY_Approval Queue Core]]
- 17 edges to [[_COMMUNITY_SSH Proxy & Gateway Config]]
- 13 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 13 edges to [[_COMMUNITY_Module Group 78]]
- 5 edges to [[_COMMUNITY_Module Group 83]]
- 4 edges to [[_COMMUNITY_Ledger Config & Test Infra]]
- 4 edges to [[_COMMUNITY_Audit Store & Ledger]]
- 3 edges to [[_COMMUNITY_Module Group 127]]
- 2 edges to [[_COMMUNITY_MCP Inspector & Audit]]
- 2 edges to [[_COMMUNITY_Module Group 195]]
- 2 edges to [[_COMMUNITY_Module Group 135]]
- 1 edge to [[_COMMUNITY_Module Group 189]]
- 1 edge to [[_COMMUNITY_Module Group 255]]
- 1 edge to [[_COMMUNITY_Module Group 216]]

## Top bridge nodes
- [[ApprovalQueueConfig_2]] - degree 55, connects to 8 communities
- [[ApprovalRequest_2]] - degree 60, connects to 5 communities
- [[ToolRiskConfig_1]] - degree 23, connects to 4 communities
- [[ToolRiskPolicy_1]] - degree 21, connects to 4 communities
- [[queue.py]] - degree 7, connects to 3 communities