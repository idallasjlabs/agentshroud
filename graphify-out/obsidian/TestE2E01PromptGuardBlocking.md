---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "PII Sanitizer Pipeline"
location: "L82"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PII_Sanitizer_Pipeline
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
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_e2e_watchtower.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PII_Sanitizer_Pipeline