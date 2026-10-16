---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "PIIConfig"
location: "L227"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PIIConfig
---

# TestE2E06EncodingBypassDetection

## Connections
- [[dot-test_base64_content_decoded()]] - `method` [EXTRACTED]
- [[dot-test_encoding_detector_is_wired()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CanaryTripwire]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[E2E-06 Base64 and Unicode encoding bypasses are decoded and processed.]] - `rationale_for` [EXTRACTED]
- [[EncodingDetector]] - `uses` [INFERRED]
- [[PIIConfig_1]] - `uses` [INFERRED]
- [[PIISanitizer_2]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SecurityPipeline_2]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_e2e_watchtower.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PIIConfig
