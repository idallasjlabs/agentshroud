---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "Canary Tripwire"
location: "L376"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Canary_Tripwire
---

# _BrokenSanitizer

## Connections
- [[dot-sanitize()_2]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CanaryTripwire]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[EncodingDetector]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[Sanitizer that always crashes — simulates module failure.]] - `rationale_for` [EXTRACTED]
- [[SecurityPipeline_1]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_e2e_watchtower.py]] - `contains` [EXTRACTED]
- [[test_pipeline_fails_closed_on_enhanced_sanitizer_error()]] - `calls` [EXTRACTED]
- [[test_pipeline_owner_exempt_from_fail_closed()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Canary_Tripwire