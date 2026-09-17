---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "Canary Tripwire"
location: "L383"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Canary_Tripwire
---

# _BrokenOutputCanary

## Connections
- [[dot-check_response()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CanaryTripwire]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[EncodingDetector]] - `uses` [INFERRED]
- [[OutputCanary that always crashes.]] - `rationale_for` [EXTRACTED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SecurityPipeline_1]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_e2e_watchtower.py]] - `contains` [EXTRACTED]
- [[test_pipeline_fails_closed_on_output_canary_error()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Canary_Tripwire