---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Pipeline Action & Instruction Envelope"
location: "L193"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Pipeline_Action__Instruction_Envelope
---

# TestContextGuardInPipeline

## Connections
- [[.test_clean_message_passes()]] - `method` [EXTRACTED]
- [[.test_context_guard_error_fails_closed()]] - `method` [EXTRACTED]
- [[.test_critical_injection_blocks()]] - `method` [EXTRACTED]
- [[.test_high_injection_blocks()]] - `method` [EXTRACTED]
- [[.test_no_context_guard_passes_through()]] - `method` [EXTRACTED]
- [[.test_repetition_attack_does_not_block()]] - `method` [EXTRACTED]
- [[.test_skip_context_guard_bypasses_step0()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[ContextGuard must run in SecurityPipeline.process_inbound() — A2.]] - `rationale_for` [EXTRACTED]
- [[EnvelopeSigner]] - `uses` [INFERRED]
- [[InstructionEnvelope]] - `uses` [INFERRED]
- [[KeyLeakDetector]] - `uses` [INFERRED]
- [[KeyVault]] - `uses` [INFERRED]
- [[KeyVaultConfig]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Pipeline_Action__Instruction_Envelope
