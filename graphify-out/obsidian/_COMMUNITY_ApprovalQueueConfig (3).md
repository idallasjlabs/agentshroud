---
type: community
members: 91
---

# ApprovalQueueConfig (3)

**Members:** 91 nodes

## Members
- [[dot-__init__()_140]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-__init__()_141]] - code - gateway/approval_queue/store.py
- [[dot-close()_10]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-close()_11]] - code - gateway/approval_queue/store.py
- [[dot-connect()_2]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-disconnect()_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-initialize()_2]] - code - gateway/approval_queue/store.py
- [[dot-mcp_proxy_with_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-send_json()_1]] - code - gateway/tests/test_enhanced_approval.py
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
- [[dot-test_wait_for_decision()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-update_status()]] - code - gateway/approval_queue/store.py
- [[dot-wait_for_decision()_3]] - code - gateway/approval_queue/enhanced_queue.py
- [[A WebSocket stand-in whose send_json never returns.      Models a real-world dea]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Accept a WebSocket connection and add to connected set.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Approval queue configuration]] - rationale - gateway/ingest_api/config.py
- [[ApprovalQueue_1]] - code - gateway/tests/test_mfa_guard.py
- [[ApprovalQueueConfig_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalQueueConfig_2]] - code - gateway/ingest_api/config.py
- [[ApprovalStore]] - code - gateway/approval_queue/store.py
- [[ApprovalStore_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[Build a REAL EnhancedApprovalQueue with a default ToolRiskConfig.      The defau]] - rationale - gateway/tests/test_mcp_policy.py
- [[Close the database connection._1]] - rationale - gateway/approval_queue/store.py
- [[Close the store and cancel timeout tasks.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Create a temporary SQLite store for testing.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Create a test tool risk configuration.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Create an MCP proxy with approval queue.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Create an enhanced approval queue for testing.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Enhanced approval queue with enforce mode and tool risk tiers.      Features]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[EnhancedApprovalQueue_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[EnhancedApprovalQueue_2]] - code - gateway/tests/test_mfa_guard.py
- [[Initialize enhanced approval queue.          Args             config Basic app]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[MCPProxy.check_approval_required]] - code - gateway/proxy/mcp_proxy.py
- [[MFAGuard_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[MonkeyPatch]] - code - gateway/tests/test_mcp_policy.py
- [[Open the database and create the schema. Idempotent a second call         must]] - rationale - gateway/approval_queue/store.py
- [[Path_39]] - code - gateway/approval_queue/store.py
- [[Remove a WebSocket connection from connected set.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Risk policy configuration for a tool tier]] - rationale - gateway/ingest_api/config.py
- [[SCRUM-110 restart recovery must reschedule the timeout with the         item's]] - rationale - gateway/tests/test_enhanced_approval.py
- [[SCRUM-154 a dead WebSocket client must never wedge the approval lock.      subm_1]] - rationale - gateway/tests/test_enhanced_approval.py
- [[SQLite-backed persistence for approval queue items.]] - rationale - gateway/approval_queue/store.py
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
- [[Update the status of an existing item.]] - rationale - gateway/approval_queue/store.py
- [[Wait for an approval decision.          Returns             True if approved, F]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[WebSocket_3]] - code - gateway/approval_queue/enhanced_queue.py
- [[_HangingWebSocket_1]] - code - gateway/tests/test_enhanced_approval.py
- [[_real_queue()]] - code - gateway/tests/test_mcp_policy.py
- [[broadcast() itself must bound its wait per-client, not just rely on     callers]] - rationale - gateway/tests/test_enhanced_approval.py
- [[enhanced_mfa_queue()]] - code - gateway/tests/test_mfa_guard.py
- [[enhanced_queue()]] - code - gateway/tests/test_enhanced_approval.py
- [[enhanced_queue.py]] - code - gateway/approval_queue/enhanced_queue.py
- [[temp_store()]] - code - gateway/tests/test_enhanced_approval.py
- [[test_broadcast_does_not_hang_forever_on_dead_client()_1]] - code - gateway/tests/test_enhanced_approval.py
- [[test_enhanced_approval.py]] - code - gateway/tests/test_enhanced_approval.py
- [[test_submit_does_not_deadlock_on_hung_websocket_client()_1]] - code - gateway/tests/test_enhanced_approval.py
- [[test_websocket_notifications()]] - code - gateway/tests/test_enhanced_approval.py
- [[tool_risk_config()]] - code - gateway/tests/test_enhanced_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalQueueConfig_3
SORT file.name ASC
```

## Connections to other communities
- 66 edges to [[_COMMUNITY_ApprovalQueueConfig (4)]]
- 30 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 24 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 22 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 17 edges to [[_COMMUNITY_MCPPermissionManager]]
- 9 edges to [[_COMMUNITY_Mac App Discovery Skill (2)]]
- 7 edges to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 6 edges to [[_COMMUNITY_PIIConfig]]
- 3 edges to [[_COMMUNITY_TestSSRFDetection (4)]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig (5)]]
- 3 edges to [[_COMMUNITY_BotConfig]]
- 3 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager (3)]]
- 2 edges to [[_COMMUNITY_MiddlewareManager (2)]]
- 1 edge to [[_COMMUNITY_GroupApprovalRouter]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager (4)]]
- 1 edge to [[_COMMUNITY_MCPInspector]]
- 1 edge to [[_COMMUNITY_main.py.md (2)]]
- 1 edge to [[_COMMUNITY_TestMCPResultEndpoint]]

## Top bridge nodes
- [[ApprovalQueueConfig_2]] - degree 80, connects to 10 communities
- [[EnhancedApprovalQueue_1]] - degree 57, connects to 8 communities
- [[ToolRiskConfig]] - degree 38, connects to 7 communities
- [[enhanced_queue.py]] - degree 14, connects to 6 communities
- [[ApprovalStore]] - degree 58, connects to 5 communities
