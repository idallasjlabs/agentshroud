---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "Community 870"
location: "L383"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_870
---

# _BrokenOutputCanary

## Connections
- [[.check_response()_1]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CanaryTripwire]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[EncodingDetector]] - `uses` [INFERRED]
- [[OutputCanary that always crashes.]] - `rationale_for` [EXTRACTED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_e2e_watchtower.py]] - `contains` [EXTRACTED]
- [[test_pipeline_fails_closed_on_output_canary_error()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_870