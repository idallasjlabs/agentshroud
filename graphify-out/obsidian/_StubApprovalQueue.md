---
source_file: "gateway/tests/test_a2a_policy.py"
type: "code"
community: "Community 75"
location: "L322"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_75
---

# _StubApprovalQueue

## Connections
- [[dot-__init__()_180]] - `method` [EXTRACTED]
- [[dot-submit_tool_request()_4]] - `method` [EXTRACTED]
- [[dot-wait_for_decision()_4]] - `method` [EXTRACTED]
- [[A2AMethod]] - `uses` [INFERRED]
- [[A2APolicyAction]] - `uses` [INFERRED]
- [[A2APolicyConfig]] - `uses` [INFERRED]
- [[A2APolicyDecision]] - `uses` [INFERRED]
- [[A2APolicyEngine_1]] - `uses` [INFERRED]
- [[test_a2a_policy.py]] - `contains` [EXTRACTED]
- [[test_enforce_denies_when_queue_downgrades_requires_wait_to_false()]] - `calls` [EXTRACTED]
- [[test_enforce_high_risk_method_approved_resolves_to_allow()]] - `calls` [EXTRACTED]
- [[test_enforce_high_risk_method_rejected_resolves_to_deny()]] - `calls` [EXTRACTED]
- [[test_enforce_task_ownership_violation_never_reaches_approval_queue()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_75