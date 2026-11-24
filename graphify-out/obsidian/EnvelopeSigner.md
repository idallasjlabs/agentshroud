---
source_file: "gateway/security/instruction_envelope.py"
type: "code"
community: "EnvelopeSigner"
location: "L42"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/EnvelopeSigner
---

# EnvelopeSigner

## Connections
- [[dot-__init__()_203]] - `references` [EXTRACTED]
- [[dot-__init__()_205]] - `method` [EXTRACTED]
- [[dot-_compute_signature()]] - `method` [EXTRACTED]
- [[dot-sign()]] - `method` [EXTRACTED]
- [[dot-test_different_keys_fail_verification()]] - `calls` [EXTRACTED]
- [[dot-test_different_signers_same_key_verify()]] - `calls` [EXTRACTED]
- [[dot-test_outbound_response_is_signed_and_verifiable()]] - `calls` [EXTRACTED]
- [[dot-verify()_1]] - `method` [EXTRACTED]
- [[dot-wrap_system_prompt()]] - `method` [EXTRACTED]
- [[dot-wrap_tool_result()]] - `method` [EXTRACTED]
- [[HermesDelegate]] - `uses` [INFERRED]
- [[Signs and verifies InstructionEnvelopes. Usage signer = EnvelopeSigner() env…]] - `rationale_for` [EXTRACTED]
- [[TestEnvelopeSigner]] - `uses` [INFERRED]
- [[TestEnvelopeSignerInPipeline]] - `uses` [INFERRED]
- [[build_edge_service()]] - `calls` [EXTRACTED]
- [[facades.py]] - `imports` [EXTRACTED]
- [[instruction_envelope.py]] - `contains` [EXTRACTED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[service.py]] - `imports` [EXTRACTED]
- [[signer()]] - `uses` [INFERRED]
- [[test_delegate_wraps_task_as_untrusted_and_targets_restricted_profile()]] - `calls` [EXTRACTED]
- [[test_edge_facades.py]] - `imports` [EXTRACTED]
- [[test_edge_fuzz.py]] - `imports` [EXTRACTED]
- [[test_embedded_delimiters_are_neutralised()]] - `calls` [EXTRACTED]
- [[test_instruction_envelope.py]] - `imports` [EXTRACTED]
- [[test_pipeline_unit.py]] - `imports` [EXTRACTED]
- [[test_shellish_input_never_executes()]] - `uses` [INFERRED]
- [[test_signature_verifies_and_detects_tampering()]] - `calls` [EXTRACTED]
- [[test_source_is_sanitised()]] - `calls` [EXTRACTED]
- [[test_untrusted_envelope.py]] - `imports` [EXTRACTED]
- [[test_wrapped_content_is_delimited_and_labelled()]] - `calls` [EXTRACTED]
- [[unwrap_untrusted()]] - `references` [EXTRACTED]
- [[wrap_untrusted()]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/EnvelopeSigner
