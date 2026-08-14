---
source_file: "gateway/tests/test_forward_routing.py"
type: "code"
community: "SOC Dashboard"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SOC_Dashboard
---

# test_forward_routing.py

## Connections
- [[AgentTarget]] - `references` [EXTRACTED]
- [[ForwardRequest]] - `imports` [EXTRACTED]
- [[TestAgentIdPropagatedFromTarget]] - `contains` [EXTRACTED]
- [[TestOutboundBlockedNotDelivered]] - `contains` [EXTRACTED]
- [[TestOwnerSpoofingViaForwardBody]] - `contains` [EXTRACTED]
- [[TestOwnerTrustElevation]] - `contains` [EXTRACTED]
- [[_BlockedOutboundPipeline]] - `contains` [EXTRACTED]
- [[_PipelineCaptor]] - `contains` [EXTRACTED]
- [[_TrustCaptor]] - `contains` [EXTRACTED]
- [[_make_mock_app_state()]] - `contains` [EXTRACTED]
- [[_make_trust_app_state()]] - `contains` [EXTRACTED]
- [[forward-routing agent_id propagation into security pipeline]] - `implements` [EXTRACTED]
- [[forward.py]] - `imports_from` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SOC_Dashboard