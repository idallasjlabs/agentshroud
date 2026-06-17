---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "Security Pipeline & Audit Chain"
location: "L83"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Security_Pipeline__Audit_Chain
---

# TestE2E01PromptGuardBlocking

## Connections
- [[.test_benign_message_passes()]] - `method` [EXTRACTED]
- [[.test_classic_injection_blocked()]] - `method` [EXTRACTED]
- [[.test_jailbreak_blocked()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CanaryTripwire]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[E2E-01 PromptGuard blocks high-confidence injection payloads.]] - `rationale_for` [EXTRACTED]
- [[EncodingDetector]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_e2e_watchtower.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Security_Pipeline__Audit_Chain