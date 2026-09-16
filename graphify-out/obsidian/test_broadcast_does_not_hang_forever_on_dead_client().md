---
source_file: "gateway/tests/test_enhanced_approval.py"
type: "code"
community: "Enhanced Approval Queue"
location: "L544"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Enhanced_Approval_Queue
---

# test_broadcast_does_not_hang_forever_on_dead_client()

## Connections
- [[ApprovalQueueConfig_2]] - `calls` [EXTRACTED]
- [[ApprovalStore]] - `calls` [EXTRACTED]
- [[ApprovalStore_1]] - `calls` [INFERRED]
- [[EnhancedApprovalQueue_1]] - `calls` [EXTRACTED]
- [[ToolRiskConfig]] - `calls` [EXTRACTED]
- [[_HangingWebSocket]] - `calls` [EXTRACTED]
- [[broadcast() itself must bound its wait per-client, not just rely on     callers]] - `rationale_for` [EXTRACTED]
- [[test_enhanced_approval.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Enhanced_Approval_Queue