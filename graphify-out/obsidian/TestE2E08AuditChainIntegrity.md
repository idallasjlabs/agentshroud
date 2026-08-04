---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "Security Pipeline & Audit Chain"
location: "L281"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Security_Pipeline__Audit_Chain
---

# TestE2E08AuditChainIntegrity

## Connections
- [[.test_audit_chain_hash_chained()]] - `method` [EXTRACTED]
- [[.test_blocked_message_has_audit_entry()]] - `method` [EXTRACTED]
- [[.test_forwarded_message_has_audit_entry()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CanaryTripwire]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[E2E-08 Every pipeline event — block or forward — produces an audit entry.]] - `rationale_for` [EXTRACTED]
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
