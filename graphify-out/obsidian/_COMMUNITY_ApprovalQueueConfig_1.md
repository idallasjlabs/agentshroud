---
type: community
cohesion: 0.03
members: 142
---

# ApprovalQueueConfig

**Cohesion:** 0.03 - loosely connected
**Members:** 142 nodes

## Members
- [[dot-__init__()_44]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-__init__()_45]] - code - gateway/approval_queue/store.py
- [[dot-_notify_telegram()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-_schedule_timeout()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-_timeout_request()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-broadcast()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-close()_2]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-close()_3]] - code - gateway/approval_queue/store.py
- [[dot-connect()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-decide()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-disconnect()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-get_item()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-get_pending()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-get_policy_for_tier()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-get_tool_risk_tier()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-initialize()_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-initialize()_2]] - code - gateway/approval_queue/store.py
- [[dot-mcp_proxy_with_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-requires_approval()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-send_json()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-submit()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-submit_tool_request()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-test_100_concurrent_submissions()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_critical_tool_approval_flow()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_critical_tool_denial_flow()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_critical_tool_requires_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_enforce_mode_disabled()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_get_tool_risk_tier()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_low_risk_tool_allowed()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_low_risk_tool_no_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_owner_bypass()_1]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_requires_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_restart_recovery_preserves_timeout_action()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_restore_pending_items()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_store_expires_old_items()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_store_persists_across_reopen()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_store_save_and_load()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_store_update_status()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_wait_for_decision()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-update_status()]] - code - gateway/approval_queue/store.py
- [[dot-wait_for_decision()]] - code - gateway/approval_queue/enhanced_queue.py
- [[100 concurrent approval requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[A WebSocket stand-in whose send_json never returns.      Models a real-world dea]] - rationale - gateway/tests/test_enhanced_approval.py
- [[A pending approval request in the queue]] - rationale - gateway/ingest_api/models.py
- [[Accept a WebSocket connection and add to connected set.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Add an action to the approval queue with policy-based timeout.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Any_12]] - code - gateway/approval_queue/enhanced_queue.py
- [[Approval queue configuration]] - rationale - gateway/ingest_api/config.py
- [[ApprovalQueueConfig_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalQueueConfig_2]] - code - gateway/ingest_api/config.py
- [[ApprovalQueueItem_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalQueueItem_2]] - code - gateway/ingest_api/models.py
- [[ApprovalRequest]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalStore]] - code - gateway/approval_queue/store.py
- [[ApprovalStore_1]] - code - gateway/approval_queue/enhanced_queue.py
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
- [[EnhancedApprovalQueue_1]] - code - gateway/tests/test_mfa_guard.py
- [[Fetch a single queue item by ID.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get all pending approval items.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get the policy for a risk tier.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get the risk tier for a tool.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Handle timeout for a pending request.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Initialize enhanced approval queue.          Args             config Basic app]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Initialize the store and restore pending items.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Items saved to store can be reloaded.]] - rationale - gateway/tests/test_approval_stress.py
- [[Items survive store closereopen cycle.]] - rationale - gateway/tests/test_approval_stress.py
- [[MCPProxy.check_approval_required]] - code - gateway/proxy/mcp_proxy.py
- [[MFAGuard_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[Open the database and create the schema. Idempotent a second call         must]] - rationale - gateway/approval_queue/store.py
- [[Path_15]] - code - gateway/approval_queue/store.py
- [[Process an approval decision.          IEC 62443 FR1 approving a high-risk acti]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Queue persistence across restart.]] - rationale - gateway/tests/test_approval_stress.py
- [[Remove a WebSocket connection from connected set.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Risk policy configuration for a tool tier]] - rationale - gateway/ingest_api/config.py
- [[SCRUM-110 restart recovery must reschedule the timeout with the         item's]] - rationale - gateway/tests/test_enhanced_approval.py
- [[SCRUM-154 a dead WebSocket client must never wedge the approval lock.      subm]] - rationale - gateway/tests/test_enhanced_approval.py
- [[SQLite-backed persistence for approval queue items.]] - rationale - gateway/approval_queue/store.py
- [[Schedule a timeout task for a request.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Send Telegram notification for approval requests.          Sends a formatted mes]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Send a JSON message to all connected WebSocket clients.          SCRUM-154 boun]] - rationale - gateway/approval_queue/enhanced_queue.py
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
- [[ToolRiskConfig]] - code - gateway/ingest_api/config.py
- [[ToolRiskConfig_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[ToolRiskPolicy]] - code - gateway/ingest_api/config.py
- [[ToolRiskPolicy_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[Update the status of an existing item.]] - rationale - gateway/approval_queue/store.py
- [[Wait for an approval decision.          Returns             True if approved, F]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[WebSocket_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[_HangingWebSocket]] - code - gateway/tests/test_enhanced_approval.py
- [[_real_queue()]] - code - gateway/tests/test_mcp_policy.py
- [[broadcast() itself must bound its wait per-client, not just rely on     callers]] - rationale - gateway/tests/test_enhanced_approval.py
- [[enhanced_mfa_queue()]] - code - gateway/tests/test_mfa_guard.py
- [[enhanced_queue()]] - code - gateway/tests/test_enhanced_approval.py
- [[enhanced_queue.py]] - code - gateway/approval_queue/enhanced_queue.py
- [[queue()]] - code - gateway/tests/test_approval_stress.py
- [[store()]] - code - gateway/tests/test_approval_stress.py
- [[temp_store()]] - code - gateway/tests/test_enhanced_approval.py
- [[test_approval_stress.py]] - code - gateway/tests/test_approval_stress.py
- [[test_broadcast_does_not_hang_forever_on_dead_client()]] - code - gateway/tests/test_enhanced_approval.py
- [[test_enhanced_approval.py]] - code - gateway/tests/test_enhanced_approval.py
- [[test_submit_does_not_deadlock_on_hung_websocket_client()]] - code - gateway/tests/test_enhanced_approval.py
- [[test_websocket_notifications()]] - code - gateway/tests/test_enhanced_approval.py
- [[tool_risk_config()]] - code - gateway/tests/test_enhanced_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalQueueConfig
SORT file.name ASC
```

## Connections to other communities
- 31 edges to [[_COMMUNITY_ApprovalQueueConfig_2]]
- 29 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 26 edges to [[_COMMUNITY_ApprovalQueueConfig_3]]
- 21 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 15 edges to [[_COMMUNITY_MCPPermissionManager]]
- 13 edges to [[_COMMUNITY_Mac App Discovery Skill_1]]
- 11 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 10 edges to [[_COMMUNITY_PIIConfig]]
- 4 edges to [[_COMMUNITY_create_auth_dependency]]
- 4 edges to [[_COMMUNITY_main.py]]
- 4 edges to [[_COMMUNITY__FakeRBAC]]
- 3 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 3 edges to [[_COMMUNITY_TestSSRFDetection_6]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager_1]]
- 2 edges to [[_COMMUNITY_InjectionAction_1]]
- 2 edges to [[_COMMUNITY_Restart Procedure]]
- 2 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_GroupApprovalRouter]]
- 1 edge to [[_COMMUNITY_MCPInspector]]
- 1 edge to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_TestMCPResultEndpoint]]

## Top bridge nodes
- [[ApprovalQueueConfig_2]] - degree 80, connects to 9 communities
- [[EnhancedApprovalQueue]] - degree 59, connects to 9 communities
- [[ApprovalStore]] - degree 60, connects to 7 communities
- [[enhanced_queue.py]] - degree 15, connects to 7 communities
- [[ToolRiskConfig]] - degree 38, connects to 5 communities
