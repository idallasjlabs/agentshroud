---
source_file: "gateway/approval_queue/store.py"
type: "code"
community: "test_mfa_guard.py"
location: "L40"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_mfa_guardpy
---

# ApprovalStore

## Connections
- [[dot-__init__()_114]] - `references` [EXTRACTED]
- [[dot-__init__()_116]] - `method` [EXTRACTED]
- [[dot-close()_10]] - `method` [EXTRACTED]
- [[dot-initialize()_2]] - `method` [EXTRACTED]
- [[dot-load_all()]] - `method` [EXTRACTED]
- [[dot-load_pending()]] - `method` [EXTRACTED]
- [[dot-save()_2]] - `method` [EXTRACTED]
- [[dot-test_restart_recovery_preserves_timeout_action()]] - `calls` [EXTRACTED]
- [[dot-test_restore_pending_items()]] - `calls` [EXTRACTED]
- [[dot-test_store_persists_across_reopen()]] - `calls` [EXTRACTED]
- [[dot-update_status()]] - `method` [EXTRACTED]
- [[ApprovalQueueItem]] - `uses` [INFERRED]
- [[EnhancedApprovalQueue]] - `uses` [INFERRED]
- [[SQLite-backed persistence for approval queue items.]] - `rationale_for` [EXTRACTED]
- [[TestApprovalStorePersistence]] - `uses` [INFERRED]
- [[TestPersistence_2]] - `uses` [INFERRED]
- [[_real_queue()]] - `calls` [EXTRACTED]
- [[approval_queuestore.py]] - `contains` [EXTRACTED]
- [[edge()_1]] - `uses` [INFERRED]
- [[enhanced_mfa_queue()]] - `uses` [INFERRED]
- [[enhanced_queue.py]] - `imports` [EXTRACTED]
- [[env()]] - `uses` [INFERRED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[stack()]] - `uses` [INFERRED]
- [[store()_1]] - `uses` [INFERRED]
- [[store()_2]] - `uses` [INFERRED]
- [[temp_store()]] - `uses` [INFERRED]
- [[test_approval_store.py]] - `imports` [EXTRACTED]
- [[test_approval_stress.py]] - `imports` [EXTRACTED]
- [[test_broadcast_does_not_hang_forever_on_dead_client()_1]] - `uses` [INFERRED]
- [[test_decide_persists()]] - `uses` [INFERRED]
- [[test_edge_approvals.py]] - `imports` [EXTRACTED]
- [[test_edge_e2e_sdk.py]] - `imports` [EXTRACTED]
- [[test_edge_pipeline.py]] - `imports` [EXTRACTED]
- [[test_enhanced_approval.py]] - `imports` [EXTRACTED]
- [[test_expired_items_on_reload()]] - `uses` [INFERRED]
- [[test_initialize_is_idempotent()_1]] - `uses` [INFERRED]
- [[test_mcp_policy.py]] - `imports` [EXTRACTED]
- [[test_mfa_guard.py]] - `imports` [EXTRACTED]
- [[test_persist_and_reload()]] - `uses` [INFERRED]
- [[test_store_survives_restart()]] - `uses` [INFERRED]
- [[test_submit_does_not_deadlock_on_hung_websocket_client()_1]] - `uses` [INFERRED]
- [[test_websocket_notifications()]] - `uses` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_mfa_guardpy
