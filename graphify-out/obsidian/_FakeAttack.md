---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Signed Instruction Envelopes & Security Pipeline"
location: "L191"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Signed_Instruction_Envelopes__Security_Pipeline
---

# _FakeAttack

## Connections
- [[dot-test_blocked_request_decays_trust_score()]] - `calls` [EXTRACTED]
- [[dot-test_blocked_request_propagates_to_cross_bot_peer()]] - `calls` [EXTRACTED]
- [[dot-test_critical_injection_blocks()]] - `calls` [EXTRACTED]
- [[dot-test_high_injection_blocks()]] - `calls` [EXTRACTED]
- [[dot-test_missing_trust_manager_does_not_raise()]] - `calls` [EXTRACTED]
- [[dot-test_non_owner_block_does_not_emit_owner_bypass()]] - `calls` [EXTRACTED]
- [[dot-test_owner_bypass_audited_at_every_guard()]] - `calls` [EXTRACTED]
- [[dot-test_owner_bypass_is_recorded_in_audit_chain()]] - `calls` [EXTRACTED]
- [[dot-test_owner_exempted_block_does_not_decay_trust()]] - `calls` [EXTRACTED]
- [[dot-test_repetition_attack_does_not_block()]] - `calls` [EXTRACTED]
- [[dot-test_skip_context_guard_bypasses_step0()]] - `calls` [EXTRACTED]
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
- [[ThreatAction]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Signed_Instruction_Envelopes__Security_Pipeline