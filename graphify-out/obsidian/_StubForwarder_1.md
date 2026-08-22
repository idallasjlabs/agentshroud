---
source_file: "gateway/tests/test_a2a_trust_scoring.py"
type: "code"
community: "A2a Integration"
location: "L26"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/A2a_Integration
---

# _StubForwarder

## Connections
- [[.forward()_3]] - `method` [EXTRACTED]
- [[A2APolicyConfig]] - `uses` [INFERRED]
- [[A2APolicyEngine_1]] - `uses` [INFERRED]
- [[A2AProxy]] - `uses` [INFERRED]
- [[ProgressiveTrustConfig]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[ViolationType]] - `uses` [INFERRED]
- [[test_a2a_trust_scoring.py]] - `contains` [EXTRACTED]
- [[test_generic_denial_does_not_record_a2a_specific_violation_types()]] - `calls` [EXTRACTED]
- [[test_proxy_without_trust_manager_does_not_raise()]] - `calls` [EXTRACTED]
- [[test_ssrf_callback_rejection_triggers_severe_demotion()]] - `calls` [EXTRACTED]
- [[test_task_ownership_violation_records_a2a_violation_type()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/A2a_Integration