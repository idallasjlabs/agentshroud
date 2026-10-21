---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "PipelineAction"
location: "L151"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PipelineAction
---

# TestE2E03OutboundPIIRedaction

## Connections
- [[dot-test_clean_response_passes_unchanged()]] - `method` [EXTRACTED]
- [[dot-test_credit_card_stripped_from_response()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CanaryTripwire]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[E2E-03 PII in agent responses is stripped before delivery.]] - `rationale_for` [EXTRACTED]
- [[EncodingDetector]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer_2]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[PromptGuard_1]] - `uses` [INFERRED]
- [[SecurityPipeline_1]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager_3]] - `uses` [INFERRED]
- [[test_e2e_watchtower.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PipelineAction
