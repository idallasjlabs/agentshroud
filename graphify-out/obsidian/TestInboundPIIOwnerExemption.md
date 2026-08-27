---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Community 22"
location: "L724"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_22
---

# TestInboundPIIOwnerExemption

## Connections
- [[._redacting_pii()]] - `method` [EXTRACTED]
- [[.test_non_owner_inbound_query_still_redacted()]] - `method` [EXTRACTED]
- [[.test_owner_inbound_query_not_pii_redacted()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CrossBotTrustLedger]] - `uses` [INFERRED]
- [[EnvelopeSigner]] - `uses` [INFERRED]
- [[InjectionAction]] - `uses` [INFERRED]
- [[InstructionEnvelope]] - `uses` [INFERRED]
- [[KeyLeakDetector]] - `uses` [INFERRED]
- [[KeyVault]] - `uses` [INFERRED]
- [[KeyVaultConfig]] - `uses` [INFERRED]
- [[OutboundInfoFilter]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[ScanResult_1]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[Step 2 PII sanitisation must be skipped for the authenticated owner.      Non-ow]] - `rationale_for` [EXTRACTED]
- [[ThreatAction]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_22