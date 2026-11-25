---
source_file: "gateway/tests/test_forward_routing.py"
type: "code"
community: "AgentTarget"
location: "L338"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AgentTarget
---

# .test_blocked_outbound_replaced_with_policy_notice()

## Connections
- [[AgentTarget]] - `calls` [EXTRACTED]
- [[AsyncMock]] - `calls` [INFERRED]
- [[TestOutboundBlockedNotDelivered]] - `method` [EXTRACTED]
- [[_BlockedOutboundPipeline]] - `calls` [EXTRACTED]
- [[_passthrough_block_credentials()]] - `indirect_call` [INFERRED]
- [[app()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/AgentTarget
