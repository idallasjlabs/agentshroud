---
source_file: "gateway/tests/test_redteam_probes.py"
type: "code"
community: "MiddlewareManager"
location: "L47"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/MiddlewareManager
---

# SecurityPipeline

## Connections
- [[ContextGuard]] - `uses` [INFERRED]
- [[EgressFilter_1]] - `uses` [INFERRED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[EncodingDetector]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer_1]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SecurityPipeline_2]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustLevel_2]] - `uses` [INFERRED]
- [[TrustManager_4]] - `uses` [INFERRED]
- [[_make_full_pipeline()]] - `references` [EXTRACTED]
- [[test_pipeline_fails_closed_without_pii()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/MiddlewareManager
