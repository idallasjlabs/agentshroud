---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "PII Sanitizer Pipeline"
location: "L151"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PII_Sanitizer_Pipeline
---

# TestE2E03OutboundPIIRedaction

## Connections
- [[.test_clean_response_passes_unchanged()]] - `method` [EXTRACTED]
- [[.test_credit_card_stripped_from_response()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CanaryTripwire]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[E2E-03 PII in agent responses is stripped before delivery.]] - `rationale_for` [EXTRACTED]
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