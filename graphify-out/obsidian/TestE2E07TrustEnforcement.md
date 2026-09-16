---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "Canary Tripwire"
location: "L253"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Canary_Tripwire
---

# TestE2E07TrustEnforcement

## Connections
- [[dot-test_low_trust_cannot_delete_file()]] - `method` [EXTRACTED]
- [[dot-test_trusted_agent_can_send_message()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CanaryTripwire]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[E2E-07 Low-trust agent cannot perform high-risk actions.]] - `rationale_for` [EXTRACTED]
- [[EncodingDetector]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SecurityPipeline_1]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_e2e_watchtower.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Canary_Tripwire