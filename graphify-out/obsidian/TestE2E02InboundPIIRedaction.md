---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "Canary Tripwire"
location: "L116"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Canary_Tripwire
---

# TestE2E02InboundPIIRedaction

## Connections
- [[dot-test_email_redacted()]] - `method` [EXTRACTED]
- [[dot-test_phone_redacted()]] - `method` [EXTRACTED]
- [[dot-test_ssn_redacted()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CanaryTripwire]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[E2E-02 Social security numbers and email are redacted before forwarding.]] - `rationale_for` [EXTRACTED]
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