---
source_file: "gateway/security/instruction_envelope.py"
type: "code"
community: "Community 24"
location: "L42"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_24
---

# EnvelopeSigner

## Connections
- [[.__init__()_101]] - `method` [EXTRACTED]
- [[._compute_signature()]] - `method` [EXTRACTED]
- [[.sign()]] - `method` [EXTRACTED]
- [[.test_different_keys_fail_verification()]] - `calls` [EXTRACTED]
- [[.test_different_signers_same_key_verify()]] - `calls` [EXTRACTED]
- [[.test_outbound_response_is_signed_and_verifiable()]] - `calls` [EXTRACTED]
- [[.verify()]] - `method` [EXTRACTED]
- [[.wrap_system_prompt()]] - `method` [EXTRACTED]
- [[.wrap_tool_result()]] - `method` [EXTRACTED]
- [[Any_10]] - `uses` [INFERRED]
- [[Any_13]] - `uses` [INFERRED]
- [[C46 Signed Instruction Envelopes (HMAC-SHA256 tamper detection for system promptstool results)]] - `rationale_for` [EXTRACTED]
- [[EdgeService]] - `uses` [INFERRED]
- [[EdgeStore_3]] - `uses` [INFERRED]
- [[EnvelopeSigner]] - `uses` [INFERRED]
- [[HermesDelegate]] - `uses` [INFERRED]
- [[LabSearch]] - `uses` [INFERRED]
- [[PkeStatus]] - `uses` [INFERRED]
- [[Signs and verifies InstructionEnvelopes.      Usage          signer = Envelope]] - `rationale_for` [EXTRACTED]
- [[TestAuditChain]] - `uses` [INFERRED]
- [[TestAuditChainBounded]] - `uses` [INFERRED]
- [[TestContextGuardInPipeline]] - `uses` [INFERRED]
- [[TestContextIntegrityInPipeline]] - `uses` [INFERRED]
- [[TestEnvelopeSigner]] - `uses` [INFERRED]
- [[TestEnvelopeSignerInPipeline]] - `uses` [INFERRED]
- [[TestInboundPIIOwnerExemption]] - `uses` [INFERRED]
- [[TestKeyLeakDetection_1]] - `uses` [INFERRED]
- [[TestOutboundFilterResultBinding]] - `uses` [INFERRED]
- [[TestPIIBlockModeInPipeline]] - `uses` [INFERRED]
- [[TestPromptGuardToolResultTrustGate]] - `uses` [INFERRED]
- [[TestTrustViolationRecording]] - `uses` [INFERRED]
- [[VendorProfile_3]] - `uses` [INFERRED]
- [[_FakeAttack]] - `uses` [INFERRED]
- [[_FakeIntegrityScore]] - `uses` [INFERRED]
- [[build_edge_service()]] - `calls` [EXTRACTED]
- [[datetime_1]] - `uses` [INFERRED]
- [[facades.py]] - `imports` [EXTRACTED]
- [[instruction_envelope.py]] - `contains` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[service.py]] - `imports` [EXTRACTED]
- [[signer()]] - `calls` [EXTRACTED]
- [[test_delegate_wraps_task_as_untrusted_and_targets_restricted_profile()]] - `calls` [EXTRACTED]
- [[test_edge_facades.py]] - `imports` [EXTRACTED]
- [[test_edge_fuzz.py]] - `imports` [EXTRACTED]
- [[test_embedded_delimiters_are_neutralised()]] - `calls` [EXTRACTED]
- [[test_instruction_envelope.py]] - `imports` [EXTRACTED]
- [[test_pipeline_unit.py]] - `imports` [EXTRACTED]
- [[test_shellish_input_never_executes()]] - `calls` [EXTRACTED]
- [[test_signature_verifies_and_detects_tampering()]] - `calls` [EXTRACTED]
- [[test_source_is_sanitised()]] - `calls` [EXTRACTED]
- [[test_untrusted_envelope.py]] - `imports` [EXTRACTED]
- [[test_wrapped_content_is_delimited_and_labelled()]] - `calls` [EXTRACTED]
- [[unwrap_untrusted()]] - `references` [EXTRACTED]
- [[wrap_untrusted()]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_24