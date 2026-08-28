---
source_file: "gateway/tests/test_enhanced_approval.py"
type: "code"
community: "Community 23"
location: "L544"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_23
---

# test_broadcast_does_not_hang_forever_on_dead_client()

## Connections
- [[ApprovalQueueConfig_2]] - `calls` [EXTRACTED]
- [[ApprovalStore]] - `calls` [INFERRED]
- [[ApprovalStore_1]] - `calls` [EXTRACTED]
- [[EnhancedApprovalQueue]] - `calls` [EXTRACTED]
- [[ToolRiskConfig_1]] - `calls` [EXTRACTED]
- [[_HangingWebSocket_1]] - `calls` [EXTRACTED]
- [[broadcast() itself must bound its wait per-client, not just rely on     callers]] - `rationale_for` [EXTRACTED]
- [[test_enhanced_approval.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_23