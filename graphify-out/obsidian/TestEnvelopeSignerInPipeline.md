---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Key Vault & Audit Chain"
location: "L502"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Key_Vault__Audit_Chain
---

# TestEnvelopeSignerInPipeline

## Connections
- [[.test_envelope_metadata_in_audit_entry()]] - `method` [EXTRACTED]
- [[.test_no_signer_leaves_envelope_empty()]] - `method` [EXTRACTED]
- [[.test_outbound_response_is_signed_and_verifiable()]] - `method` [EXTRACTED]
- [[.test_signer_failure_never_blocks()]] - `method` [EXTRACTED]
- [[.test_tool_result_uses_wrap_tool_result()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CrossBotTrustLedger]] - `uses` [INFERRED]
- [[EnvelopeSigner]] - `uses` [INFERRED]
- [[EnvelopeSigner must attest outbound responses — C46 wiring.]] - `rationale_for` [EXTRACTED]
- [[InjectionAction]] - `uses` [INFERRED]
- [[InstructionEnvelope]] - `uses` [INFERRED]
- [[KeyLeakDetector]] - `uses` [INFERRED]
- [[KeyVault]] - `uses` [INFERRED]
- [[KeyVaultConfig]] - `uses` [INFERRED]
- [[OutboundInfoFilter]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[ScanResult_1]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[ThreatAction]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Key_Vault__Audit_Chain