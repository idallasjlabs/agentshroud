---
source_file: "gateway/tests/test_approval_queue.py"
type: "code"
community: "test_approval_queue.py"
location: "L492"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_approval_queuepy
---

# _HangingWebSocket

## Connections
- [[.send_json()_1]] - `method` [EXTRACTED]
- [[A WebSocket stand-in whose send_json never returns — models a dead     client (c]] - `rationale_for` [EXTRACTED]
- [[ApprovalQueue_1]] - `uses` [INFERRED]
- [[ApprovalQueueConfig_2]] - `uses` [INFERRED]
- [[ApprovalRequest_2]] - `uses` [INFERRED]
- [[test_approval_queue.py]] - `contains` [EXTRACTED]
- [[test_broadcast_does_not_hang_forever_on_dead_client()_1]] - `calls` [EXTRACTED]
- [[test_submit_does_not_deadlock_on_hung_websocket_client()_1]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_approval_queuepy