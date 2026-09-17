---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "TrustManager"
location: "L151"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/TrustManager
---

# TestE2E03OutboundPIIRedaction

## Connections
- [[.test_clean_response_passes_unchanged()_1]] - `method` [EXTRACTED]
- [[.test_credit_card_stripped_from_response()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CanaryTripwire]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[E2E-03 PII in agent responses is stripped before delivery.]] - `rationale_for` [EXTRACTED]
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