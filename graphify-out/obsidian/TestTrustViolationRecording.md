---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Signed Instruction Envelopes & Security Pipeline"
location: "L833"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Signed_Instruction_Envelopes__Security_Pipeline
---

# TestTrustViolationRecording

## Connections
- [[dot-_pipeline_with_trust()]] - `method` [EXTRACTED]
- [[dot-test_blocked_request_decays_trust_score()]] - `method` [EXTRACTED]
- [[dot-test_blocked_request_propagates_to_cross_bot_peer()]] - `method` [EXTRACTED]
- [[dot-test_clean_request_does_not_touch_trust_score()]] - `method` [EXTRACTED]
- [[dot-test_missing_trust_manager_does_not_raise()]] - `method` [EXTRACTED]
- [[dot-test_owner_exempted_block_does_not_decay_trust()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CrossBotTrustLedger_1]] - `uses` [INFERRED]
- [[EnvelopeSigner]] - `uses` [INFERRED]
- [[InjectionAction]] - `uses` [INFERRED]
- [[InstructionEnvelope]] - `uses` [INFERRED]
- [[KeyLeakDetector]] - `uses` [INFERRED]
- [[KeyVault]] - `uses` [INFERRED]
- [[KeyVaultConfig]] - `uses` [INFERRED]
- [[OutboundInfoFilter]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[ScanResult_1]] - `uses` [INFERRED]
- [[SecurityPipeline_1]] - `uses` [INFERRED]
- [[SecurityPipeline._maybe_record_trust_violation — centralized hook that     fires]] - `rationale_for` [EXTRACTED]
- [[ThreatAction]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Signed_Instruction_Envelopes__Security_Pipeline