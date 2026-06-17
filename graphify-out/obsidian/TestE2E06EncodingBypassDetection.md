---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "Security Pipeline & Audit Chain"
location: "L228"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Security_Pipeline__Audit_Chain
---

# TestE2E06EncodingBypassDetection

## Connections
- [[.test_base64_content_decoded()]] - `method` [EXTRACTED]
- [[.test_encoding_detector_is_wired()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CanaryTripwire]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[E2E-06 Base64 and Unicode encoding bypasses are decoded and processed.]] - `rationale_for` [EXTRACTED]
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