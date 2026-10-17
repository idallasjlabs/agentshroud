---
type: community
members: 121
---

# ApprovalQueueConfig (2)

**Members:** 121 nodes

## Members
- [[dot-__init__()_91]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-__init__()_92]] - code - gateway/approval_queue/store.py
- [[dot-_notify_telegram()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-_schedule_timeout()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-_timeout_request()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-broadcast()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-close()_9]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-close()_10]] - code - gateway/approval_queue/store.py
- [[dot-connect()_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-decide()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-disconnect()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-get_item()_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-get_pending()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-get_policy_for_tier()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-get_tool_risk_tier()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-initialize()_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-initialize()_2]] - code - gateway/approval_queue/store.py
- [[dot-mcp_proxy_with_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-requires_approval()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-send_json()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-submit()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-submit_tool_request()_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-test_critical_tool_approval_flow()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_critical_tool_denial_flow()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_critical_tool_requires_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_enforce_mode_disabled()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_get_tool_risk_tier()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_low_risk_tool_allowed()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_low_risk_tool_no_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_owner_bypass()_3]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_requires_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_restart_recovery_preserves_timeout_action()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_restore_pending_items()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_store_persists_across_reopen()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_wait_for_decision()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-update_status()]] - code - gateway/approval_queue/store.py
- [[dot-wait_for_decision()_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[A WebSocket stand-in whose send_json never returns.      Models a real-world dea]] - rationale - gateway/tests/test_enhanced_approval.py
- [[A pending approval request in the queue]] - rationale - gateway/ingest_api/models.py
- [[Accept a WebSocket connection and add to connected set.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Add an action to the approval queue with policy-based timeout.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Any_29]] - code - gateway/approval_queue/enhanced_queue.py
- [[Approval queue configuration]] - rationale - gateway/ingest_api/config.py
- [[ApprovalQueueConfig]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalQueueConfig_1]] - code - gateway/ingest_api/config.py
- [[ApprovalQueueItem_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalQueueItem_2]] - code - gateway/ingest_api/models.py
- [[ApprovalRequest_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalStore]] - code - gateway/approval_queue/store.py
- [[ApprovalStore_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[Build a REAL EnhancedApprovalQueue with a default ToolRiskConfig.      The defau]] - rationale - gateway/tests/test_mcp_policy.py
- [[Check if a tool requires approval based on risk tier and policy.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Close the database connection.]] - rationale - gateway/approval_queue/store.py
- [[Close the store and cancel timeout tasks.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Create a temporary SQLite store for testing.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Create a test tool risk configuration.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Create an MCP proxy with approval queue.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Create an enhanced approval queue for testing.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Enhanced approval queue with enforce mode and tool risk tiers.      Features]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[EnhancedApprovalQueue_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[Fetch a single queue item by ID.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get all pending approval items.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get the policy for a risk tier.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get the risk tier for a tool.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Handle timeout for a pending request.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Initialize enhanced approval queue.          Args             config Basic app]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Initialize the store and restore pending items.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Items survive store closereopen cycle.]] - rationale - gateway/tests/test_approval_stress.py
- [[MCPProxy.check_approval_required]] - code - gateway/proxy/mcp_proxy.py
- [[MFAGuard]] - code - gateway/approval_queue/enhanced_queue.py
- [[Open the database and create the schema. Idempotent a second call         must]] - rationale - gateway/approval_queue/store.py
- [[Path_21]] - code - gateway/approval_queue/store.py
- [[Process an approval decision.          IEC 62443 FR1 approving a high-risk acti]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Remove a WebSocket connection from connected set.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Risk policy configuration for a tool tier]] - rationale - gateway/ingest_api/config.py
- [[SCRUM-110 restart recovery must reschedule the timeout with the         item's]] - rationale - gateway/tests/test_enhanced_approval.py
- [[SCRUM-154 a dead WebSocket client must never wedge the approval lock.      subm]] - rationale - gateway/tests/test_enhanced_approval.py
- [[SQLite-backed persistence for approval queue items.]] - rationale - gateway/approval_queue/store.py
- [[Schedule a timeout task for a request.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Send Telegram notification for approval requests.          Sends a formatted mes]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Send a JSON message to all connected WebSocket clients.          SCRUM-154 boun]] - rationale - gateway/approval_queue/enhanced_queue.py
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
- [[TestApprovalWorkflow]] - code - gateway/tests/test_enhanced_approval.py
- [[TestMCPProxyIntegration]] - code - gateway/tests/test_enhanced_approval.py
- [[TestPersistence_1]] - code - gateway/tests/test_enhanced_approval.py
- [[TestToolRiskClassification]] - code - gateway/tests/test_enhanced_approval.py
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
- [[enhanced_queue()]] - code - gateway/tests/test_enhanced_approval.py
- [[enhanced_queue.py]] - code - gateway/approval_queue/enhanced_queue.py
- [[temp_store()]] - code - gateway/tests/test_enhanced_approval.py
- [[test_broadcast_does_not_hang_forever_on_dead_client()]] - code - gateway/tests/test_enhanced_approval.py
- [[test_enhanced_approval.py]] - code - gateway/tests/test_enhanced_approval.py
- [[test_submit_does_not_deadlock_on_hung_websocket_client()]] - code - gateway/tests/test_enhanced_approval.py
- [[test_websocket_notifications()]] - code - gateway/tests/test_enhanced_approval.py
- [[tool_risk_config()]] - code - gateway/tests/test_enhanced_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalQueueConfig_2
SORT file.name ASC
```

## Connections to other communities
- 30 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 22 edges to [[_COMMUNITY_UserSessionManager (2)_1]]
- 21 edges to [[_COMMUNITY_ApprovalQueueConfig (3)_1]]
- 21 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 15 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 15 edges to [[_COMMUNITY_ApprovalQueueConfig (5)]]
- 15 edges to [[_COMMUNITY_MCPPermissionManager]]
- 13 edges to [[_COMMUNITY_ApprovalQueueConfig (4)_1]]
- 8 edges to [[_COMMUNITY_ApprovalQueueConfig (2)_1]]
- 6 edges to [[_COMMUNITY_agentshroud-blueteamSKILL.md (3)]]
- 4 edges to [[_COMMUNITY_main.py_1]]
- 4 edges to [[_COMMUNITY_socrouter.py]]
- 3 edges to [[_COMMUNITY_TestSSRFDetection (6)]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager (2)]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 2 edges to [[_COMMUNITY_02-infrastructure.md (2)]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig (3)]]
- 1 edge to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_GroupApprovalRouter]]
- 1 edge to [[_COMMUNITY_MCPInspector]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_TestMCPResultEndpoint]]
- 1 edge to [[_COMMUNITY_create_auth_dependency (3)]]

## Top bridge nodes
- [[ApprovalQueueConfig_1]] - degree 80, connects to 11 communities
- [[EnhancedApprovalQueue_1]] - degree 59, connects to 8 communities
- [[ApprovalStore]] - degree 60, connects to 7 communities
- [[ApprovalQueueItem_2]] - degree 30, connects to 7 communities
- [[enhanced_queue.py]] - degree 15, connects to 7 communities
