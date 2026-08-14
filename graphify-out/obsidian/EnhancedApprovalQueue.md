---
source_file: "gateway/approval_queue/enhanced_queue.py"
type: "code"
community: "Collaborator Prompt Classifiers"
location: "L35"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Collaborator_Prompt_Classifiers
---

# EnhancedApprovalQueue

## Connections
- [[.__init__()_2]] - `method` [EXTRACTED]
- [[._notify_telegram()]] - `method` [EXTRACTED]
- [[._schedule_timeout()]] - `method` [EXTRACTED]
- [[._timeout_request()]] - `method` [EXTRACTED]
- [[.broadcast()]] - `method` [EXTRACTED]
- [[.close()_2]] - `method` [EXTRACTED]
- [[.connect()]] - `method` [EXTRACTED]
- [[.decide()]] - `method` [EXTRACTED]
- [[.disconnect()]] - `method` [EXTRACTED]
- [[.get_item()]] - `method` [EXTRACTED]
- [[.get_pending()]] - `method` [EXTRACTED]
- [[.get_policy_for_tier()]] - `method` [EXTRACTED]
- [[.get_tool_risk_tier()]] - `method` [EXTRACTED]
- [[.initialize()]] - `method` [EXTRACTED]
- [[.requires_approval()]] - `method` [EXTRACTED]
- [[.submit()]] - `method` [EXTRACTED]
- [[.submit_tool_request()]] - `method` [EXTRACTED]
- [[.test_enforce_mode_disabled()]] - `calls` [EXTRACTED]
- [[.test_restart_recovery_preserves_timeout_action()]] - `calls` [EXTRACTED]
- [[.test_restore_pending_items()]] - `calls` [EXTRACTED]
- [[.wait_for_decision()]] - `method` [EXTRACTED]
- [[ApprovalQueue_1]] - `uses` [INFERRED]
- [[ApprovalQueueConfig_2]] - `uses` [INFERRED]
- [[ApprovalQueueItem_3]] - `uses` [INFERRED]
- [[ApprovalRequest_3]] - `uses` [INFERRED]
- [[ApprovalStore_1]] - `uses` [INFERRED]
- [[Enhanced approval queue with enforce mode and tool risk tiers.      Features]] - `rationale_for` [EXTRACTED]
- [[EnhancedApprovalQueue_2]] - `uses` [INFERRED]
- [[MCPPolicyConfig_1]] - `uses` [INFERRED]
- [[MCPPolicyEngine_1]] - `uses` [INFERRED]
- [[MCPProxy]] - `calls` [INFERRED]
- [[MFAGuard_2]] - `uses` [INFERRED]
- [[MonkeyPatch]] - `uses` [INFERRED]
- [[TestApprovalWorkflow]] - `uses` [INFERRED]
- [[TestMCPProxyIntegration]] - `uses` [INFERRED]
- [[TestPersistence]] - `uses` [INFERRED]
- [[TestToolRiskClassification]] - `uses` [INFERRED]
- [[ToolRiskConfig_1]] - `uses` [INFERRED]
- [[ToolRiskPolicy_1]] - `uses` [INFERRED]
- [[_FakeApprovalQueue]] - `uses` [INFERRED]
- [[_real_queue()]] - `calls` [EXTRACTED]
- [[enhanced_queue()]] - `calls` [EXTRACTED]
- [[enhanced_queue.py]] - `contains` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[mcp_proxy.py]] - `imports` [EXTRACTED]
- [[state.py]] - `imports` [EXTRACTED]
- [[test_enhanced_approval.py]] - `imports` [EXTRACTED]
- [[test_mcp_policy.py]] - `imports` [EXTRACTED]
- [[test_mfa_guard.py]] - `imports` [EXTRACTED]
- [[test_websocket_notifications()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Collaborator_Prompt_Classifiers