---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "PIIConfig"
location: "L82"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PIIConfig
---

# TestE2E01PromptGuardBlocking

## Connections
- [[dot-test_benign_message_passes()]] - `method` [EXTRACTED]
- [[dot-test_classic_injection_blocked()]] - `method` [EXTRACTED]
- [[dot-test_jailbreak_blocked()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CanaryTripwire]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[E2E-01 PromptGuard blocks high-confidence injection payloads.]] - `rationale_for` [EXTRACTED]
- [[EncodingDetector]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer_2]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SecurityPipeline_2]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_e2e_watchtower.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PIIConfig
