---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "Security Pipeline & Audit Chain"
location: "L357"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Security_Pipeline__Audit_Chain
---

# TestE2E10FailClosed

## Connections
- [[.test_pipeline_raises_with_only_prompt_guard()]] - `method` [EXTRACTED]
- [[.test_pipeline_raises_without_pii_sanitizer()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CanaryTripwire]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[E2E-10 SecurityPipeline refuses to operate without PII sanitizer.]] - `rationale_for` [EXTRACTED]
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