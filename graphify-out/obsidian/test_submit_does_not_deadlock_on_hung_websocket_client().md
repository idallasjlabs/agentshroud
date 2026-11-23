---
source_file: "gateway/tests/test_approval_queue.py"
type: "code"
community: "ApprovalRequest"
location: "L502"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ApprovalRequest
---

# test_submit_does_not_deadlock_on_hung_websocket_client()

## Connections
- [[ApprovalRequest]] - `uses` [INFERRED]
- [[SCRUM-154 a dead WebSocket client must never wedge the approval lock.…]] - `rationale_for` [EXTRACTED]
- [[_HangingWebSocket]] - `calls` [EXTRACTED]
- [[asyncio_10]] - `references` [EXTRACTED]
- [[test_approval_queue.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ApprovalRequest
