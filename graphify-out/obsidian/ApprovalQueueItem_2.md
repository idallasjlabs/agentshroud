---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "ApprovalRequest"
location: "L181"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ApprovalRequest
---

# ApprovalQueueItem

## Connections
- [[.test_store_expires_old_items()]] - `calls` [EXTRACTED]
- [[.test_store_persists_across_reopen()]] - `calls` [EXTRACTED]
- [[.test_store_save_and_load()]] - `calls` [EXTRACTED]
- [[.test_store_update_status()]] - `calls` [EXTRACTED]
- [[A pending approval request in the queue]] - `rationale_for` [EXTRACTED]
- [[Any_39]] - `uses` [INFERRED]
- [[ApprovalQueueConfig_1]] - `uses` [INFERRED]
- [[ApprovalQueueItem_1]] - `uses` [INFERRED]
- [[ApprovalQueueItem_4]] - `uses` [INFERRED]
- [[ApprovalRequest_1]] - `uses` [INFERRED]
- [[ApprovalStore_1]] - `uses` [INFERRED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[EnhancedApprovalQueue_1]] - `uses` [INFERRED]
- [[MFAGuard_1]] - `uses` [INFERRED]
- [[Path_36]] - `uses` [INFERRED]
- [[TestApprovalStorePersistence]] - `uses` [INFERRED]
- [[TestApprovalTimeout]] - `uses` [INFERRED]
- [[TestAutoExpire]] - `uses` [INFERRED]
- [[TestConcurrentApprovalRequests]] - `uses` [INFERRED]
- [[ToolRiskConfig_1]] - `uses` [INFERRED]
- [[ToolRiskPolicy_1]] - `uses` [INFERRED]
- [[WebSocket_3]] - `uses` [INFERRED]
- [[_make_item()]] - `calls` [EXTRACTED]
- [[approval.py]] - `imports` [EXTRACTED]
- [[enhanced_queue.py]] - `imports` [EXTRACTED]
- [[ingest_apimodels.py]] - `contains` [EXTRACTED]
- [[queue.py]] - `imports` [EXTRACTED]
- [[store.py]] - `imports` [EXTRACTED]
- [[test_approval_store.py]] - `imports` [EXTRACTED]
- [[test_approval_stress.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/ApprovalRequest