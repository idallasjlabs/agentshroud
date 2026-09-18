---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "TrustManager"
location: "L82"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/TrustManager
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
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SecurityPipeline_1]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_e2e_watchtower.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/TrustManager