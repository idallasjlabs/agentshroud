---
source_file: "gateway/approval_queue/enhanced_queue.py"
type: "code"
community: "test_mfa_guard.py"
location: "L35"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_mfa_guardpy
---

# EnhancedApprovalQueue

## Connections
- [[dot-__init__()_62]] - `references` [EXTRACTED]
- [[dot-__init__()_148]] - `references` [EXTRACTED]
- [[dot-__init__()_114]] - `method` [EXTRACTED]
- [[dot-_notify_telegram()]] - `method` [EXTRACTED]
- [[dot-_schedule_timeout()]] - `method` [EXTRACTED]
- [[dot-_timeout_request()]] - `method` [EXTRACTED]
- [[dot-broadcast()_1]] - `method` [EXTRACTED]
- [[dot-close()_9]] - `method` [EXTRACTED]
- [[dot-connect()_1]] - `method` [EXTRACTED]
- [[dot-decide()_1]] - `method` [EXTRACTED]
- [[dot-disconnect()_1]] - `method` [EXTRACTED]
- [[dot-get_item()_2]] - `method` [EXTRACTED]
- [[dot-get_pending()_2]] - `method` [EXTRACTED]
- [[dot-get_policy_for_tier()]] - `method` [EXTRACTED]
- [[dot-get_tool_risk_tier()]] - `method` [EXTRACTED]
- [[dot-initialize()_1]] - `method` [EXTRACTED]
- [[dot-requires_approval()]] - `method` [EXTRACTED]
- [[dot-submit()_1]] - `method` [EXTRACTED]
- [[dot-submit_tool_request()_2]] - `method` [EXTRACTED]
- [[dot-test_enforce_mode_disabled()]] - `calls` [EXTRACTED]
- [[dot-test_restart_recovery_preserves_timeout_action()]] - `calls` [EXTRACTED]
- [[dot-test_restore_pending_items()]] - `calls` [EXTRACTED]
- [[dot-wait_for_decision()_2]] - `method` [EXTRACTED]
- [[AppState]] - `uses` [INFERRED]
- [[ApprovalQueueConfig]] - `uses` [INFERRED]
- [[ApprovalQueueItem]] - `uses` [INFERRED]
- [[ApprovalRequest]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[EdgeApprovals]] - `uses` [INFERRED]
- [[Enhanced approval queue with enforce mode and tool risk tiers. Features -…]] - `rationale_for` [EXTRACTED]
- [[MCPProxy]] - `uses` [INFERRED]
- [[MFAGuard]] - `uses` [INFERRED]
- [[TestPersistence_2]] - `uses` [INFERRED]
- [[TestToolRiskClassification]] - `uses` [INFERRED]
- [[ToolRiskConfig]] - `uses` [INFERRED]
- [[ToolRiskPolicy]] - `uses` [INFERRED]
- [[_real_queue()]] - `calls` [EXTRACTED]
- [[_submit_enhanced_high_risk()]] - `uses` [INFERRED]
- [[_submit_tool_call()]] - `uses` [INFERRED]
- [[approvals.py]] - `imports` [EXTRACTED]
- [[edge()_1]] - `uses` [INFERRED]
- [[enhanced_mfa_queue()]] - `uses` [INFERRED]
- [[enhanced_queue()]] - `uses` [INFERRED]
- [[enhanced_queue.py]] - `contains` [EXTRACTED]
- [[env()]] - `uses` [INFERRED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[mcp_proxy.py_2]] - `imports` [EXTRACTED]
- [[stack()]] - `uses` [INFERRED]
- [[state.py]] - `imports` [EXTRACTED]
- [[test_broadcast_does_not_hang_forever_on_dead_client()_1]] - `uses` [INFERRED]
- [[test_edge_approvals.py]] - `imports` [EXTRACTED]
- [[test_edge_e2e_sdk.py]] - `imports` [EXTRACTED]
- [[test_edge_pipeline.py]] - `imports` [EXTRACTED]
- [[test_enhanced_approval.py]] - `imports` [EXTRACTED]
- [[test_mcp_policy.py]] - `imports` [EXTRACTED]
- [[test_mfa_guard.py]] - `imports` [EXTRACTED]
- [[test_submit_does_not_deadlock_on_hung_websocket_client()_1]] - `uses` [INFERRED]
- [[test_websocket_notifications()]] - `uses` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_mfa_guardpy
