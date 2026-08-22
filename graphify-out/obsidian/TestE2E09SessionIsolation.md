---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "Security Audit & Watchtower Tests"
location: "L317"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Security_Audit__Watchtower_Tests
---

# TestE2E09SessionIsolation

## Connections
- [[.test_agents_process_independently()]] - `method` [EXTRACTED]
- [[.test_pii_from_agent_a_not_in_agent_b_audit()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CanaryTripwire]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[E2E-09 Two agents process independently with no cross-contamination.]] - `rationale_for` [EXTRACTED]
- [[EncodingDetector]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_e2e_watchtower.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Security_Audit__Watchtower_Tests