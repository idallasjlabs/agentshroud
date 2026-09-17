---
source_file: "gateway/approval_queue/enhanced_queue.py"
type: "code"
community: "ApprovalRequest"
location: "L47"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ApprovalRequest
---

# ApprovalStore

## Connections
- [[.__init__()_104]] - `references` [EXTRACTED]
- [[.test_restart_recovery_preserves_timeout_action()]] - `calls` [INFERRED]
- [[.test_restore_pending_items()]] - `calls` [INFERRED]
- [[ApprovalQueueConfig_2]] - `uses` [INFERRED]
- [[ApprovalQueueItem_2]] - `uses` [INFERRED]
- [[ApprovalRequest_2]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[MFAGuard_2]] - `uses` [INFERRED]
- [[ToolRiskConfig]] - `uses` [INFERRED]
- [[ToolRiskPolicy]] - `uses` [INFERRED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[temp_store()]] - `calls` [INFERRED]
- [[test_broadcast_does_not_hang_forever_on_dead_client()]] - `calls` [INFERRED]
- [[test_submit_does_not_deadlock_on_hung_websocket_client()]] - `calls` [INFERRED]
- [[test_websocket_notifications()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/ApprovalRequest