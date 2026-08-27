---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "Community 870"
location: "L116"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_870
---

# TestE2E02InboundPIIRedaction

## Connections
- [[.test_email_redacted()]] - `method` [EXTRACTED]
- [[.test_phone_redacted()]] - `method` [EXTRACTED]
- [[.test_ssn_redacted()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CanaryTripwire]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[E2E-02 Social security numbers and email are redacted before forwarding.]] - `rationale_for` [EXTRACTED]
- [[EncodingDetector]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_e2e_watchtower.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_870