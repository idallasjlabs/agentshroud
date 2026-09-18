---
source_file: "gateway/approval_queue/enhanced_queue.py"
type: "code"
community: "ApprovalRequest"
location: "L35"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ApprovalRequest
---

# EnhancedApprovalQueue

## Connections
- [[.__init__()_104]] - `method` [EXTRACTED]
- [[._notify_telegram()]] - `method` [EXTRACTED]
- [[._schedule_timeout()]] - `method` [EXTRACTED]
- [[._timeout_request()]] - `method` [EXTRACTED]
- [[.broadcast()]] - `method` [EXTRACTED]
- [[.close()_11]] - `method` [EXTRACTED]
- [[.connect()]] - `method` [EXTRACTED]
- [[.decide()]] - `method` [EXTRACTED]
- [[.disconnect()]] - `method` [EXTRACTED]
- [[.get_item()_1]] - `method` [EXTRACTED]
- [[.get_pending()]] - `method` [EXTRACTED]
- [[.get_policy_for_tier()]] - `method` [EXTRACTED]
- [[.get_tool_risk_tier()]] - `method` [EXTRACTED]
- [[.initialize()_2]] - `method` [EXTRACTED]
- [[.requires_approval()]] - `method` [EXTRACTED]
- [[.submit()]] - `method` [EXTRACTED]
- [[.submit_tool_request()_1]] - `method` [EXTRACTED]
- [[.test_enforce_mode_disabled()]] - `calls` [EXTRACTED]
- [[.test_restart_recovery_preserves_timeout_action()]] - `calls` [EXTRACTED]
- [[.test_restore_pending_items()]] - `calls` [EXTRACTED]
- [[.wait_for_decision()_1]] - `method` [EXTRACTED]
- [[ApprovalQueue]] - `uses` [INFERRED]
- [[ApprovalQueueConfig_2]] - `uses` [INFERRED]
- [[ApprovalQueueItem_2]] - `uses` [INFERRED]
- [[ApprovalRequest_2]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[Data Flow]] - `references` [EXTRACTED]
- [[Enhanced approval queue with enforce mode and tool risk tiers.      Features]] - `rationale_for` [EXTRACTED]
- [[EnhancedApprovalQueue_2]] - `uses` [INFERRED]
- [[Human-in-the-loop approval queue]] - `conceptually_related_to` [INFERRED]
- [[MCPPolicyConfig]] - `uses` [INFERRED]
- [[MCPPolicyEngine]] - `uses` [INFERRED]
- [[MCPProxy.check_approval_required]] - `calls` [EXTRACTED]
- [[MCPProxy.process_tool_call]] - `calls` [EXTRACTED]
- [[MFAGuard_2]] - `uses` [INFERRED]
- [[MonkeyPatch]] - `uses` [INFERRED]
- [[Startup Sequence]] - `references` [EXTRACTED]
- [[TestApprovalWorkflow]] - `uses` [INFERRED]
- [[TestMCPProxyIntegration]] - `uses` [INFERRED]
- [[TestPersistence]] - `uses` [INFERRED]
- [[TestToolRiskClassification]] - `uses` [INFERRED]
- [[ToolRiskConfig]] - `uses` [INFERRED]
- [[ToolRiskPolicy]] - `uses` [INFERRED]
- [[_FakeApprovalQueue]] - `uses` [INFERRED]
- [[_HangingWebSocket]] - `uses` [INFERRED]
- [[_real_queue()]] - `calls` [EXTRACTED]
- [[enhanced_queue()]] - `calls` [EXTRACTED]
- [[enhanced_queue.py]] - `contains` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[main.py]] - `references` [EXTRACTED]
- [[mcp_proxy.py]] - `imports` [EXTRACTED]
- [[state.py]] - `imports` [EXTRACTED]
- [[test_broadcast_does_not_hang_forever_on_dead_client()]] - `calls` [EXTRACTED]
- [[test_enhanced_approval.py]] - `imports` [EXTRACTED]
- [[test_mcp_policy.py]] - `imports` [EXTRACTED]
- [[test_mfa_guard.py]] - `imports` [EXTRACTED]
- [[test_submit_does_not_deadlock_on_hung_websocket_client()]] - `calls` [EXTRACTED]
- [[test_websocket_notifications()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ApprovalRequest