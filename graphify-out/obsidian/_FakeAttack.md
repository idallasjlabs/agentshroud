---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Pipeline Action & Instruction Envelope"
location: "L173"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Pipeline_Action__Instruction_Envelope
---

# _FakeAttack

## Connections
- [[.test_critical_injection_blocks()]] - `calls` [EXTRACTED]
- [[.test_high_injection_blocks()]] - `calls` [EXTRACTED]
- [[.test_repetition_attack_does_not_block()]] - `calls` [EXTRACTED]
- [[.test_skip_context_guard_bypasses_step0()]] - `calls` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[EnvelopeSigner]] - `uses` [INFERRED]
- [[InstructionEnvelope]] - `uses` [INFERRED]
- [[KeyLeakDetector]] - `uses` [INFERRED]
- [[KeyVault]] - `uses` [INFERRED]
- [[KeyVaultConfig]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Pipeline_Action__Instruction_Envelope
