---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "SecurityPipeline (2)"
location: "L356"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/SecurityPipeline_2
---

# TestE2E10FailClosed

## Connections
- [[dot-test_pipeline_raises_with_only_prompt_guard()]] - `method` [EXTRACTED]
- [[dot-test_pipeline_raises_without_pii_sanitizer()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CanaryTripwire]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[E2E-10 SecurityPipeline refuses to operate without PII sanitizer.]] - `rationale_for` [EXTRACTED]
- [[EncodingDetector]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer_3]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[PromptGuard_1]] - `uses` [INFERRED]
- [[SecurityPipeline_1]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_e2e_watchtower.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/SecurityPipeline_2
