---
source_file: "gateway/tests/test_a2a_trust_scoring.py"
type: "code"
community: "A2a Integration"
location: "L93"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/A2a_Integration
---

# TrustManager

## Connections
- [[A2APolicyConfig]] - `uses` [INFERRED]
- [[A2APolicyEngine_1]] - `uses` [INFERRED]
- [[A2AProxy]] - `uses` [INFERRED]
- [[ProgressiveTrustConfig]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[ViolationType]] - `uses` [INFERRED]
- [[test_generic_denial_does_not_record_a2a_specific_violation_types()]] - `references` [EXTRACTED]
- [[test_ssrf_callback_rejection_triggers_severe_demotion()]] - `references` [EXTRACTED]
- [[test_task_ownership_violation_records_a2a_violation_type()]] - `references` [EXTRACTED]
- [[trust_manager()_1]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/A2a_Integration