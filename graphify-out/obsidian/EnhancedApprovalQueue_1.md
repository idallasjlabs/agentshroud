---
source_file: "gateway/approval_queue/enhanced_queue.py"
type: "code"
community: "ContextSegment"
location: "L35"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ContextSegment
---

# EnhancedApprovalQueue

## Connections
- [[dot-__init__()_189]] - `method` [EXTRACTED]
- [[dot-_notify_telegram()]] - `method` [EXTRACTED]
- [[dot-_schedule_timeout()]] - `method` [EXTRACTED]
- [[dot-_timeout_request()]] - `method` [EXTRACTED]
- [[dot-broadcast()_1]] - `method` [EXTRACTED]
- [[dot-close()_16]] - `method` [EXTRACTED]
- [[dot-connect()_2]] - `method` [EXTRACTED]
- [[dot-decide()_1]] - `method` [EXTRACTED]
- [[dot-disconnect()_1]] - `method` [EXTRACTED]
- [[dot-get_item()_2]] - `method` [EXTRACTED]
- [[dot-get_pending()_1]] - `method` [EXTRACTED]
- [[dot-get_policy_for_tier()]] - `method` [EXTRACTED]
- [[dot-get_tool_risk_tier()]] - `method` [EXTRACTED]
- [[dot-initialize()_2]] - `method` [EXTRACTED]
- [[dot-requires_approval()]] - `method` [EXTRACTED]
- [[dot-submit()_1]] - `method` [EXTRACTED]
- [[dot-submit_tool_request()_4]] - `method` [EXTRACTED]
- [[dot-test_enforce_mode_disabled()]] - `calls` [EXTRACTED]
- [[dot-test_restart_recovery_preserves_timeout_action()]] - `calls` [EXTRACTED]
- [[dot-test_restore_pending_items()]] - `calls` [EXTRACTED]
- [[dot-wait_for_decision()_4]] - `method` [EXTRACTED]
- [[ApprovalQueue_1]] - `uses` [INFERRED]
- [[ApprovalQueueConfig_1]] - `uses` [INFERRED]
- [[ApprovalQueueItem_4]] - `uses` [INFERRED]
- [[ApprovalRequest_5]] - `uses` [INFERRED]
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
- [[TestPersistence_2]] - `uses` [INFERRED]
- [[TestToolRiskClassification]] - `uses` [INFERRED]
- [[ToolRiskConfig]] - `uses` [INFERRED]
- [[ToolRiskPolicy]] - `uses` [INFERRED]
- [[_FakeApprovalQueue]] - `uses` [INFERRED]
- [[_HangingWebSocket_1]] - `uses` [INFERRED]
- [[_real_queue()]] - `calls` [EXTRACTED]
- [[enhanced_queue()]] - `calls` [EXTRACTED]
- [[enhanced_queue.py]] - `contains` [EXTRACTED]
- [[main.py]] - `references` [EXTRACTED]
- [[mcp_proxy.py]] - `imports` [EXTRACTED]
- [[state.py]] - `imports` [EXTRACTED]
- [[test_broadcast_does_not_hang_forever_on_dead_client()_1]] - `calls` [EXTRACTED]
- [[test_enhanced_approval.py]] - `imports` [EXTRACTED]
- [[test_mcp_policy.py]] - `imports` [EXTRACTED]
- [[test_mfa_guard.py]] - `imports` [EXTRACTED]
- [[test_submit_does_not_deadlock_on_hung_websocket_client()_1]] - `calls` [EXTRACTED]
- [[test_websocket_notifications()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ContextSegment
