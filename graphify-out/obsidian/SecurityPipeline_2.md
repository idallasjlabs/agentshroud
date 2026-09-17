---
source_file: "gateway/tests/test_redteam_probes.py"
type: "code"
community: "TrustManager"
location: "L47"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/TrustManager
---

# SecurityPipeline

## Connections
- [[ContextGuard]] - `uses` [INFERRED]
- [[EgressFilter]] - `uses` [INFERRED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[EncodingDetector]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SecurityPipeline_1]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustLevel]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[_make_full_pipeline()]] - `references` [EXTRACTED]
- [[test_pipeline_fails_closed_without_pii()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/TrustManager