---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Signed Instruction Envelopes & Security Pipeline"
location: "L211"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Signed_Instruction_Envelopes__Security_Pipeline
---

# TestContextGuardInPipeline

## Connections
- [[dot-test_clean_message_passes()]] - `method` [EXTRACTED]
- [[dot-test_context_guard_error_fails_closed()]] - `method` [EXTRACTED]
- [[dot-test_critical_injection_blocks()]] - `method` [EXTRACTED]
- [[dot-test_high_injection_blocks()]] - `method` [EXTRACTED]
- [[dot-test_no_context_guard_passes_through()]] - `method` [EXTRACTED]
- [[dot-test_non_owner_block_does_not_emit_owner_bypass()]] - `method` [EXTRACTED]
- [[dot-test_owner_bypass_audited_at_every_guard()]] - `method` [EXTRACTED]
- [[dot-test_owner_bypass_is_recorded_in_audit_chain()]] - `method` [EXTRACTED]
- [[dot-test_repetition_attack_does_not_block()]] - `method` [EXTRACTED]
- [[dot-test_skip_context_guard_bypasses_step0()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[ContextGuard must run in SecurityPipeline.process_inbound() — A2.]] - `rationale_for` [EXTRACTED]
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