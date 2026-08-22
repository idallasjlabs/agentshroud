---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Pipeline Unit"
location: "L786"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Pipeline_Unit
---

# TestOutboundFilterResultBinding

## Connections
- [[.test_no_outbound_filter_does_not_unbind()]] - `method` [EXTRACTED]
- [[.test_outbound_filter_still_escalates_fabricated_notice()]] - `method` [EXTRACTED]
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
- [[Regression filter_result was possibly-unbound in process_outbound when no     o]] - `rationale_for` [EXTRACTED]
- [[ScanResult_1]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[ThreatAction]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Pipeline_Unit