---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "Enhanced Approval Queue"
location: "L181"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Enhanced_Approval_Queue
---

# ApprovalQueueItem

## Connections
- [[.test_store_expires_old_items()]] - `calls` [EXTRACTED]
- [[.test_store_persists_across_reopen()]] - `calls` [EXTRACTED]
- [[.test_store_save_and_load()]] - `calls` [EXTRACTED]
- [[.test_store_update_status()]] - `calls` [EXTRACTED]
- [[A pending approval request in the queue]] - `rationale_for` [EXTRACTED]
- [[Any_2]] - `uses` [INFERRED]
- [[ApprovalQueueConfig]] - `uses` [INFERRED]
- [[ApprovalQueueItem_1]] - `uses` [INFERRED]
- [[ApprovalQueueItem_4]] - `uses` [INFERRED]
- [[ApprovalRequest_1]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[EnhancedApprovalQueue]] - `uses` [INFERRED]
- [[MCPProxyRequest]] - `uses` [INFERRED]
- [[MCPResultRequest]] - `uses` [INFERRED]
- [[MFAGuard]] - `uses` [INFERRED]
- [[OpProxyRequest]] - `uses` [INFERRED]
- [[Path_23]] - `uses` [INFERRED]
- [[SSHExecRequest_1]] - `uses` [INFERRED]
- [[TestApprovalStorePersistence]] - `uses` [INFERRED]
- [[TestApprovalTimeout]] - `uses` [INFERRED]
- [[TestAutoExpire]] - `uses` [INFERRED]
- [[TestConcurrentApprovalRequests]] - `uses` [INFERRED]
- [[ToolRiskConfig]] - `uses` [INFERRED]
- [[ToolRiskPolicy]] - `uses` [INFERRED]
- [[WebSocket_1]] - `uses` [INFERRED]
- [[_make_item()]] - `calls` [EXTRACTED]
- [[approval.py]] - `imports` [EXTRACTED]
- [[enhanced_queue.py]] - `imports` [EXTRACTED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[models.py]] - `contains` [EXTRACTED]
- [[queue.py]] - `imports` [EXTRACTED]
- [[store.py]] - `imports` [EXTRACTED]
- [[test_approval_store.py]] - `imports` [EXTRACTED]
- [[test_approval_stress.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Enhanced_Approval_Queue