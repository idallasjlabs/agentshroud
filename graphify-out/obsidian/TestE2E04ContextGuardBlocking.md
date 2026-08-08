---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "PII Sanitizer Pipeline"
location: "L177"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PII_Sanitizer_Pipeline
---

# TestE2E04ContextGuardBlocking

## Connections
- [[.test_cross_context_injection_blocked()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CanaryTripwire]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[E2E-04 ContextGuard detects session-level injection in multi-turn context.]] - `rationale_for` [EXTRACTED]
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