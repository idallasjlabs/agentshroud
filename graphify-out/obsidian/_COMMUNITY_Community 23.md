---
type: community
cohesion: 0.04
members: 119
---

# Community 23

**Cohesion:** 0.04 - loosely connected
**Members:** 119 nodes

## Members
- [[.__init__()_3]] - code - gateway/approval_queue/enhanced_queue.py
- [[.__init__()_6]] - code - gateway/approval_queue/store.py
- [[._notify_telegram()]] - code - gateway/approval_queue/enhanced_queue.py
- [[._schedule_timeout()]] - code - gateway/approval_queue/enhanced_queue.py
- [[._timeout_request()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.broadcast()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.close()_3]] - code - gateway/approval_queue/enhanced_queue.py
- [[.close()_4]] - code - gateway/approval_queue/store.py
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
- [[.send_json()_1]] - code - gateway/tests/test_enhanced_approval.py
- [[.submit()]] - code - gateway/approval_queue/enhanced_queue.py
- [[.submit_tool_request()]] - code - gateway/approval_queue/enhanced_queue.py
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
- [[.test_wait_for_decision()]] - code - gateway/tests/test_enhanced_approval.py
- [[.update_status()]] - code - gateway/approval_queue/store.py
- [[.wait_for_decision()]] - code - gateway/approval_queue/enhanced_queue.py
- [[A WebSocket stand-in whose send_json never returns.      Models a real-world dea]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Accept a WebSocket connection and add to connected set.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Add an action to the approval queue with policy-based timeout.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Any]] - code - gateway/approval_queue/enhanced_queue.py
- [[Approval queue configuration]] - rationale - gateway/ingest_api/config.py
- [[ApprovalQueueConfig]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalQueueConfig_2]] - code - gateway/ingest_api/config.py
- [[ApprovalQueueItem]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalRequest]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalStore_1]] - code - gateway/approval_queue/store.py
- [[ApprovalStore]] - code - gateway/approval_queue/enhanced_queue.py
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
- [[Fetch a single queue item by ID.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get all pending approval items.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get the policy for a risk tier.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get the risk tier for a tool.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Handle timeout for a pending request.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Initialize enhanced approval queue.          Args             config Basic app]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Initialize the store and restore pending items.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[MCPProxy.check_approval_required]] - code - gateway/proxy/mcp_proxy.py
- [[MFAGuard]] - code - gateway/approval_queue/enhanced_queue.py
- [[MonkeyPatch]] - code - gateway/tests/test_mcp_policy.py
- [[Open the database and create the schema. Idempotent a second call         must]] - rationale - gateway/approval_queue/store.py
- [[Path]] - code - gateway/approval_queue/store.py
- [[Process an approval decision.          IEC 62443 FR1 approving a high-risk acti]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Remove a WebSocket connection from connected set.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Risk policy configuration for a tool tier]] - rationale - gateway/ingest_api/config.py
- [[SCRUM-110 restart recovery must reschedule the timeout with the         item's]] - rationale - gateway/tests/test_enhanced_approval.py
- [[SCRUM-154 a dead WebSocket client must never wedge the approval lock.      subm_1]] - rationale - gateway/tests/test_enhanced_approval.py
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
- [[TestPersistence]] - code - gateway/tests/test_enhanced_approval.py
- [[TestToolRiskClassification]] - code - gateway/tests/test_enhanced_approval.py
- [[Tool risk tier configuration]] - rationale - gateway/ingest_api/config.py
- [[ToolRiskConfig_1]] - code - gateway/ingest_api/config.py
- [[ToolRiskConfig]] - code - gateway/approval_queue/enhanced_queue.py
- [[ToolRiskPolicy_1]] - code - gateway/ingest_api/config.py
- [[ToolRiskPolicy]] - code - gateway/approval_queue/enhanced_queue.py
- [[Update the status of an existing item.]] - rationale - gateway/approval_queue/store.py
- [[Wait for an approval decision.          Returns             True if approved, F]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[WebSocket_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[_HangingWebSocket_1]] - code - gateway/tests/test_enhanced_approval.py
- [[_real_queue()]] - code - gateway/tests/test_mcp_policy.py
- [[approval_queue()_1]] - code - gateway/tests/test_security_integration.py
- [[broadcast() itself must bound its wait per-client, not just rely on     callers]] - rationale - gateway/tests/test_enhanced_approval.py
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
TABLE source_file, type FROM #community/Community_23
SORT file.name ASC
```

## Connections to other communities
- 33 edges to [[_COMMUNITY_Community 125]]
- 29 edges to [[_COMMUNITY_Community 63]]
- 22 edges to [[_COMMUNITY_Community 33]]
- 21 edges to [[_COMMUNITY_Community 56]]
- 17 edges to [[_COMMUNITY_Community 44]]
- 16 edges to [[_COMMUNITY_Community 15]]
- 11 edges to [[_COMMUNITY_Community 26]]
- 6 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 6 edges to [[_COMMUNITY_Community 43]]
- 4 edges to [[_COMMUNITY_Community 85]]
- 4 edges to [[_COMMUNITY_Community 64]]
- 3 edges to [[_COMMUNITY_Community 14]]
- 3 edges to [[_COMMUNITY_Community 1013]]
- 3 edges to [[_COMMUNITY_Community 91]]
- 2 edges to [[_COMMUNITY_Community 46]]
- 2 edges to [[_COMMUNITY_Community 39]]
- 2 edges to [[_COMMUNITY_PII Sanitizer & E2E Tests]]
- 1 edge to [[_COMMUNITY_Community 123]]
- 1 edge to [[_COMMUNITY_Ingest API & Approval Routes]]
- 1 edge to [[_COMMUNITY_Community 206]]
- 1 edge to [[_COMMUNITY_Community 77]]
- 1 edge to [[_COMMUNITY_Community 289]]
- 1 edge to [[_COMMUNITY_Community 508]]
- 1 edge to [[_COMMUNITY_Community 261]]
- 1 edge to [[_COMMUNITY_RBAC & SOC Realtime]]

## Top bridge nodes
- [[ApprovalQueueConfig_2]] - degree 80, connects to 12 communities
- [[EnhancedApprovalQueue]] - degree 60, connects to 10 communities
- [[enhanced_queue.py]] - degree 15, connects to 8 communities
- [[ApprovalStore_1]] - degree 60, connects to 6 communities
- [[ToolRiskConfig_1]] - degree 38, connects to 6 communities