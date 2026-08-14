---
source_file: "gateway/approval_queue/store.py"
type: "code"
community: "Collaborator Prompt Classifiers"
location: "L40"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Collaborator_Prompt_Classifiers
---

# ApprovalStore

## Connections
- [[.__init__()_5]] - `method` [EXTRACTED]
- [[.close()_3]] - `method` [EXTRACTED]
- [[.initialize()_1]] - `method` [EXTRACTED]
- [[.load_all()]] - `method` [EXTRACTED]
- [[.load_pending()]] - `method` [EXTRACTED]
- [[.save()]] - `method` [EXTRACTED]
- [[.test_restart_recovery_preserves_timeout_action()]] - `calls` [EXTRACTED]
- [[.test_restore_pending_items()]] - `calls` [EXTRACTED]
- [[.test_store_persists_across_reopen()]] - `calls` [EXTRACTED]
- [[.update_status()]] - `method` [EXTRACTED]
- [[Any]] - `uses` [INFERRED]
- [[ApprovalQueue_1]] - `uses` [INFERRED]
- [[ApprovalQueueConfig]] - `uses` [INFERRED]
- [[ApprovalQueueItem]] - `uses` [INFERRED]
- [[ApprovalQueueItem_4]] - `uses` [INFERRED]
- [[ApprovalRequest]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[EnhancedApprovalQueue]] - `uses` [INFERRED]
- [[EnhancedApprovalQueue_2]] - `uses` [INFERRED]
- [[MCPPolicyConfig_1]] - `uses` [INFERRED]
- [[MCPPolicyEngine_1]] - `uses` [INFERRED]
- [[MFAGuard]] - `uses` [INFERRED]
- [[MonkeyPatch]] - `uses` [INFERRED]
- [[Path_24]] - `uses` [INFERRED]
- [[SQLite-backed persistence for approval queue items.]] - `rationale_for` [EXTRACTED]
- [[TestApprovalStorePersistence]] - `uses` [INFERRED]
- [[TestApprovalTimeout]] - `uses` [INFERRED]
- [[TestApprovalWorkflow]] - `uses` [INFERRED]
- [[TestAutoExpire]] - `uses` [INFERRED]
- [[TestConcurrentApprovalRequests]] - `uses` [INFERRED]
- [[TestMCPProxyIntegration]] - `uses` [INFERRED]
- [[TestPersistence]] - `uses` [INFERRED]
- [[TestToolRiskClassification]] - `uses` [INFERRED]
- [[ToolRiskConfig]] - `uses` [INFERRED]
- [[ToolRiskPolicy]] - `uses` [INFERRED]
- [[WebSocket]] - `uses` [INFERRED]
- [[_FakeApprovalQueue]] - `uses` [INFERRED]
- [[_real_queue()]] - `calls` [EXTRACTED]
- [[enhanced_mfa_queue()]] - `calls` [EXTRACTED]
- [[enhanced_queue.py]] - `imports` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[store()]] - `calls` [EXTRACTED]
- [[store()_1]] - `calls` [EXTRACTED]
- [[store.py]] - `contains` [EXTRACTED]
- [[temp_store()]] - `calls` [EXTRACTED]
- [[test_approval_store.py]] - `imports` [EXTRACTED]
- [[test_approval_stress.py]] - `imports` [EXTRACTED]
- [[test_decide_persists()]] - `calls` [EXTRACTED]
- [[test_enhanced_approval.py]] - `references` [EXTRACTED]
- [[test_expired_items_on_reload()]] - `calls` [EXTRACTED]
- [[test_initialize_is_idempotent()]] - `calls` [EXTRACTED]
- [[test_mcp_policy.py]] - `imports` [EXTRACTED]
- [[test_mfa_guard.py]] - `imports` [EXTRACTED]
- [[test_persist_and_reload()]] - `calls` [EXTRACTED]
- [[test_store_survives_restart()]] - `calls` [EXTRACTED]
- [[test_websocket_notifications()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Collaborator_Prompt_Classifiers