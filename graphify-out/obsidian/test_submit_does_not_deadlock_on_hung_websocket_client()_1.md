---
source_file: "gateway/tests/test_enhanced_approval.py"
type: "code"
community: "test_mfa_guard.py"
location: "L491"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_mfa_guardpy
---

# test_submit_does_not_deadlock_on_hung_websocket_client()

## Connections
- [[ApprovalQueueConfig]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[EnhancedApprovalQueue]] - `uses` [INFERRED]
- [[SCRUM-154 a dead WebSocket client must never wedge the approval lock.…_1]] - `rationale_for` [EXTRACTED]
- [[ToolRiskConfig]] - `uses` [INFERRED]
- [[_HangingWebSocket_1]] - `calls` [EXTRACTED]
- [[asyncio_49]] - `references` [EXTRACTED]
- [[test_enhanced_approval.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_mfa_guardpy
