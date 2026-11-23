---
source_file: "gateway/tests/test_enhanced_approval.py"
type: "code"
community: "EnhancedApprovalQueue"
location: "L544"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/EnhancedApprovalQueue
---

# test_broadcast_does_not_hang_forever_on_dead_client()

## Connections
- [[ApprovalQueueConfig]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[EnhancedApprovalQueue]] - `uses` [INFERRED]
- [[ToolRiskConfig]] - `uses` [INFERRED]
- [[_HangingWebSocket_1]] - `calls` [EXTRACTED]
- [[asyncio_48]] - `references` [EXTRACTED]
- [[broadcast() itself must bound its wait per-client, not just rely on callers…]] - `rationale_for` [EXTRACTED]
- [[test_enhanced_approval.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/EnhancedApprovalQueue
