---
type: community
cohesion: 0.03
members: 134
---

# Enhanced Approval Queue

**Cohesion:** 0.03 - loosely connected
**Members:** 134 nodes

## Members
- [[.__init__()_7]] - code - gateway/approval_queue/enhanced_queue.py
- [[.__init__()_10]] - code - gateway/approval_queue/store.py
- [[._notify_telegram()]] - code - gateway/approval_queue/enhanced_queue.py
- [[._schedule_timeout()]] - code - gateway/approval_queue/enhanced_queue.py
- [[._timeout_request()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.broadcast()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.close()_2]] - code - gateway/approval_queue/enhanced_queue.py
- [[.close()_3]] - code - gateway/approval_queue/store.py
- [[.connect()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.decide()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.disconnect()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.get_item()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.get_pending()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.get_policy_for_tier()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.get_tool_risk_tier()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.initialize()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.initialize()_1]] - code - gateway/approval_queue/store.py
- [[.mcp_proxy_with_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[.requires_approval()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.submit()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.submit_tool_request()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.test_100_concurrent_submissions()]] - code - gateway/tests/test_approval_stress.py
- [[.test_critical_tool_approval_flow()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_critical_tool_denial_flow()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_critical_tool_requires_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_enforce_mode_disabled()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_get_tool_risk_tier()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_low_risk_tool_allowed()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_low_risk_tool_no_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_owner_bypass()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_requires_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_restart_recovery_preserves_timeout_action()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_restore_pending_items()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_store_expires_old_items()]] - code - gateway/tests/test_approval_stress.py
- [[.test_store_persists_across_reopen()]] - code - gateway/tests/test_approval_stress.py
- [[.test_store_save_and_load()]] - code - gateway/tests/test_approval_stress.py
- [[.test_store_update_status()]] - code - gateway/tests/test_approval_stress.py
- [[.test_wait_for_decision()]] - code - gateway/tests/test_enhanced_approval.py
- [[.update_status()]] - code - gateway/approval_queue/store.py
- [[.wait_for_decision()]] - code - gateway/approval_queue/enhanced_queue.py
- [[100 concurrent approval requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[A pending approval request in the queue]] - rationale - gateway/ingest_api/models.py
- [[Accept a WebSocket connection and add to connected set.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Add an action to the approval queue with policy-based timeout.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Any_2]] - code - gateway/approval_queue/enhanced_queue.py
- [[Approval queue configuration]] - rationale - gateway/ingest_api/config.py
- [[ApprovalQueueConfig]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalQueueConfig_2]] - code - gateway/ingest_api/config.py
- [[ApprovalQueueItem_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalQueueItem]] - code - gateway/ingest_api/models.py
- [[ApprovalRequest_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalStore_1]] - code - gateway/approval_queue/store.py
- [[ApprovalStore]] - code - gateway/approval_queue/enhanced_queue.py
- [[Auto-expire old requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[Build a REAL EnhancedApprovalQueue with a default ToolRiskConfig.      The defau]] - rationale - gateway/tests/test_mcp_policy.py
- [[Check if a tool requires approval based on risk tier and policy.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Close the database connection.]] - rationale - gateway/approval_queue/store.py
- [[Close the store and cancel timeout tasks.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Create a temporary SQLite store for testing.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Create a test tool risk configuration.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Create an MCP proxy with approval queue.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Create an enhanced approval queue for testing.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Enhanced approval queue with enforce mode and tool risk tiers.      Features]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[EnhancedApprovalQueue]] - code - gateway/approval_queue/enhanced_queue.py
- [[EnhancedApprovalQueue_2]] - code - gateway/tests/test_mfa_guard.py
- [[Fetch a single queue item by ID.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get all pending approval items.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get the policy for a risk tier.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get the risk tier for a tool.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Handle timeout for a pending request.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Initialize enhanced approval queue.          Args             config Basic app]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Initialize the store and restore pending items.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Items saved to store can be reloaded.]] - rationale - gateway/tests/test_approval_stress.py
- [[Items survive store closereopen cycle.]] - rationale - gateway/tests/test_approval_stress.py
- [[MFAGuard]] - code - gateway/approval_queue/enhanced_queue.py
- [[Open the database and create the schema. Idempotent a second call         must]] - rationale - gateway/approval_queue/store.py
- [[Path]] - code - gateway/approval_queue/store.py
- [[Process an approval decision.          IEC 62443 FR1 approving a high-risk acti]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Queue persistence across restart.]] - rationale - gateway/tests/test_approval_stress.py
- [[Remove a WebSocket connection from connected set.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Risk policy configuration for a tool tier]] - rationale - gateway/ingest_api/config.py
- [[SCRUM-110 restart recovery must reschedule the timeout with the         item's]] - rationale - gateway/tests/test_enhanced_approval.py
- [[SQLite-backed persistence for approval queue items.]] - rationale - gateway/approval_queue/store.py
- [[Schedule a timeout task for a request.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Send Telegram notification for approval requests.          Sends a formatted mes]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Send a JSON message to all connected WebSocket clients.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Status updates persist.]] - rationale - gateway/tests/test_approval_stress.py
- [[Store marks expired items on load.]] - rationale - gateway/tests/test_approval_stress.py
- [[Submit 100 requests concurrently — all should succeed.]] - rationale - gateway/tests/test_approval_stress.py
- [[Submit a tool call request for approval.          Args             tool_name T]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Test MCP proxy integration with approval queue.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test SQLite persistence across restarts.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test approval requirement logic.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test denial flow for critical tool.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test full approval flow for critical tool.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test owner bypass for high-tier tools.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test risk tier lookup.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that approval events are generated for WebSocket notification.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that approval is bypassed when enforce mode is disabled.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that critical tools are identified as requiring approval.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that low-risk tools are allowed without approval.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that low-risk tools don't require approval.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that pending items are restored after restart.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test the complete approval workflow.]] - rationale - gateway/tests/test_enhanced_approval.py
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
- [[WebSocket_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[_real_queue()]] - code - gateway/tests/test_mcp_policy.py
- [[enhanced_mfa_queue()]] - code - gateway/tests/test_mfa_guard.py
- [[enhanced_queue()]] - code - gateway/tests/test_enhanced_approval.py
- [[queue()]] - code - gateway/tests/test_approval_stress.py
- [[store()_1]] - code - gateway/tests/test_approval_stress.py
- [[store.py]] - code - gateway/approval_queue/store.py
- [[temp_store()]] - code - gateway/tests/test_enhanced_approval.py
- [[test_approval_stress.py]] - code - gateway/tests/test_approval_stress.py
- [[test_enhanced_approval.py]] - code - gateway/tests/test_enhanced_approval.py
- [[test_websocket_notifications()]] - code - gateway/tests/test_enhanced_approval.py
- [[tool_risk_config()]] - code - gateway/tests/test_enhanced_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Enhanced_Approval_Queue
SORT file.name ASC
```

## Connections to other communities
- 36 edges to [[_COMMUNITY_Gateway Test Suite]]
- 26 edges to [[_COMMUNITY_Gateway Test Suite]]
- 23 edges to [[_COMMUNITY_Forward Routing & Approval]]
- 21 edges to [[_COMMUNITY_MCP Policy Engine]]
- 21 edges to [[_COMMUNITY_Approval Queue Tests]]
- 14 edges to [[_COMMUNITY_Gateway Test Suite]]
- 13 edges to [[_COMMUNITY_Gateway Test Suite]]
- 7 edges to [[_COMMUNITY_Approval & FastAPI Ingest]]
- 6 edges to [[_COMMUNITY_Auth & Exception Types]]
- 4 edges to [[_COMMUNITY_SOC Dashboard]]
- 3 edges to [[_COMMUNITY_Approval Queue]]
- 2 edges to [[_COMMUNITY_PII Sanitizer Pipeline]]
- 2 edges to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_MCP Proxy Config]]
- 1 edge to [[_COMMUNITY_SOC Service Manager]]
- 1 edge to [[_COMMUNITY_URLDomain Validation Tests]]

## Top bridge nodes
- [[ApprovalQueueConfig_2]] - degree 76, connects to 8 communities
- [[EnhancedApprovalQueue]] - degree 51, connects to 7 communities
- [[ApprovalStore_1]] - degree 57, connects to 6 communities
- [[ToolRiskConfig_1]] - degree 35, connects to 6 communities
- [[ApprovalQueueItem]] - degree 35, connects to 5 communities