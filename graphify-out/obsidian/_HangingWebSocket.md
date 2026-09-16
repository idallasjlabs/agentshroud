---
source_file: "gateway/tests/test_enhanced_approval.py"
type: "code"
community: "Enhanced Approval Queue"
location: "L478"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Enhanced_Approval_Queue
---

# _HangingWebSocket

## Connections
- [[dot-send_json()]] - `method` [EXTRACTED]
- [[A WebSocket stand-in whose send_json never returns.      Models a real-world dea]] - `rationale_for` [EXTRACTED]
- [[ApprovalQueueConfig_2]] - `uses` [INFERRED]
- [[ApprovalRequest_2]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[EnhancedApprovalQueue_1]] - `uses` [INFERRED]
- [[MCPProxy_1]] - `uses` [INFERRED]
- [[MCPToolCall_1]] - `uses` [INFERRED]
- [[ToolRiskConfig]] - `uses` [INFERRED]
- [[ToolRiskPolicy]] - `uses` [INFERRED]
- [[test_broadcast_does_not_hang_forever_on_dead_client()]] - `calls` [EXTRACTED]
- [[test_enhanced_approval.py]] - `contains` [EXTRACTED]
- [[test_submit_does_not_deadlock_on_hung_websocket_client()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Enhanced_Approval_Queue