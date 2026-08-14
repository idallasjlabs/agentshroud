---
source_file: "gateway/security/a2a_policy.py"
type: "code"
community: "SOC Dashboard"
location: "L143"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SOC_Dashboard
---

# A2APolicyDecision

## Connections
- [[._decide()]] - `references` [EXTRACTED]
- [[.allowed()]] - `method` [EXTRACTED]
- [[.enforce()]] - `references` [EXTRACTED]
- [[.evaluate()]] - `references` [EXTRACTED]
- [[A2AMethod_1]] - `uses` [INFERRED]
- [[A2APolicyConfig_1]] - `uses` [INFERRED]
- [[A2APolicyEngine_2]] - `uses` [INFERRED]
- [[The result of evaluating a single A2A request against the policy.]] - `rationale_for` [EXTRACTED]
- [[_LegacyStubApprovalQueue]] - `uses` [INFERRED]
- [[_StubApprovalQueue]] - `uses` [INFERRED]
- [[a2a_policy.py]] - `contains` [EXTRACTED]
- [[test_a2a_policy.py]] - `imports` [EXTRACTED]
- [[test_decision_allowed_property_only_true_for_terminal_allow()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SOC_Dashboard