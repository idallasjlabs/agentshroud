---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Pipeline Action & Instruction Envelope"
location: "L179"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Pipeline_Action__Instruction_Envelope
---

# _make_pipeline()

## Connections
- [[.test_clean_message_passes()]] - `calls` [EXTRACTED]
- [[.test_context_guard_error_fails_closed()]] - `calls` [EXTRACTED]
- [[.test_critical_injection_blocks()]] - `calls` [EXTRACTED]
- [[.test_high_injection_blocks()]] - `calls` [EXTRACTED]
- [[.test_no_context_guard_passes_through()]] - `calls` [EXTRACTED]
- [[.test_no_scorer_leaves_result_unscored()]] - `calls` [EXTRACTED]
- [[.test_no_signer_leaves_envelope_empty()]] - `calls` [EXTRACTED]
- [[.test_repetition_attack_does_not_block()]] - `calls` [EXTRACTED]
- [[.test_skip_context_guard_bypasses_step0()]] - `calls` [EXTRACTED]
- [[AsyncMock]] - `calls` [INFERRED]
- [[Minimal SecurityPipeline with a real PII sanitizer stub.]] - `rationale_for` [EXTRACTED]
- [[SecurityPipeline]] - `calls` [EXTRACTED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Pipeline_Action__Instruction_Envelope