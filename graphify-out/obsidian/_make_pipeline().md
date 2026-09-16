---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Signed Instruction Envelopes & Security Pipeline"
location: "L197"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Signed_Instruction_Envelopes__Security_Pipeline
---

# _make_pipeline()

## Connections
- [[dot-test_clean_message_passes()]] - `calls` [EXTRACTED]
- [[dot-test_context_guard_error_fails_closed()]] - `calls` [EXTRACTED]
- [[dot-test_critical_injection_blocks()]] - `calls` [EXTRACTED]
- [[dot-test_high_injection_blocks()]] - `calls` [EXTRACTED]
- [[dot-test_missing_trust_manager_does_not_raise()]] - `calls` [EXTRACTED]
- [[dot-test_no_context_guard_passes_through()]] - `calls` [EXTRACTED]
- [[dot-test_no_outbound_filter_does_not_unbind()]] - `calls` [EXTRACTED]
- [[dot-test_no_scorer_leaves_result_unscored()]] - `calls` [EXTRACTED]
- [[dot-test_no_signer_leaves_envelope_empty()]] - `calls` [EXTRACTED]
- [[dot-test_non_owner_block_does_not_emit_owner_bypass()]] - `calls` [EXTRACTED]
- [[dot-test_owner_bypass_is_recorded_in_audit_chain()]] - `calls` [EXTRACTED]
- [[dot-test_repetition_attack_does_not_block()]] - `calls` [EXTRACTED]
- [[dot-test_skip_context_guard_bypasses_step0()]] - `calls` [EXTRACTED]
- [[AsyncMock]] - `calls` [INFERRED]
- [[Minimal SecurityPipeline with a real PII sanitizer stub.]] - `rationale_for` [EXTRACTED]
- [[SecurityPipeline_1]] - `calls` [EXTRACTED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Signed_Instruction_Envelopes__Security_Pipeline