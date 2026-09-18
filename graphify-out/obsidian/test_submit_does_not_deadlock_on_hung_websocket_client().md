---
source_file: "gateway/tests/test_enhanced_approval.py"
type: "code"
community: "ApprovalRequest"
location: "L491"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ApprovalRequest
---

# test_submit_does_not_deadlock_on_hung_websocket_client()

## Connections
- [[ApprovalQueueConfig_2]] - `calls` [EXTRACTED]
- [[ApprovalStore]] - `calls` [EXTRACTED]
- [[ApprovalStore_1]] - `calls` [INFERRED]
- [[EnhancedApprovalQueue_1]] - `calls` [EXTRACTED]
- [[SCRUM-154 a dead WebSocket client must never wedge the approval lock.      subm]] - `rationale_for` [EXTRACTED]
- [[ToolRiskConfig]] - `calls` [EXTRACTED]
- [[_HangingWebSocket]] - `calls` [EXTRACTED]
- [[test_enhanced_approval.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ApprovalRequest