---
source_file: "gateway/security/instruction_envelope.py"
type: "code"
community: "Signed Instruction Envelopes & Security Pipeline"
location: "L41"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Signed_Instruction_Envelopes__Security_Pipeline
---

# EnvelopeSigner

## Connections
- [[dot-__init__()_60]] - `method` [EXTRACTED]
- [[dot-_compute_signature()]] - `method` [EXTRACTED]
- [[dot-sign()]] - `method` [EXTRACTED]
- [[dot-test_different_keys_fail_verification()]] - `calls` [EXTRACTED]
- [[dot-test_different_signers_same_key_verify()]] - `calls` [EXTRACTED]
- [[dot-test_outbound_response_is_signed_and_verifiable()]] - `calls` [EXTRACTED]
- [[dot-verify()]] - `method` [EXTRACTED]
- [[dot-wrap_system_prompt()]] - `method` [EXTRACTED]
- [[dot-wrap_tool_result()]] - `method` [EXTRACTED]
- [[C46 Signed Instruction Envelopes (HMAC-SHA256 tamper detection for system promptstool results)]] - `rationale_for` [EXTRACTED]
- [[Signs and verifies InstructionEnvelopes.      Usage          signer = Envelope]] - `rationale_for` [EXTRACTED]
- [[TestAuditChain]] - `uses` [INFERRED]
- [[TestAuditChainBounded]] - `uses` [INFERRED]
- [[TestContextGuardInPipeline]] - `uses` [INFERRED]
- [[TestContextIntegrityInPipeline]] - `uses` [INFERRED]
- [[TestEnvelopeSigner]] - `uses` [INFERRED]
- [[TestEnvelopeSignerInPipeline]] - `uses` [INFERRED]
- [[TestInboundPIIOwnerExemption]] - `uses` [INFERRED]
- [[TestKeyLeakDetection]] - `uses` [INFERRED]
- [[TestOutboundFilterResultBinding]] - `uses` [INFERRED]
- [[TestPromptGuardToolResultTrustGate]] - `uses` [INFERRED]
- [[TestTrustViolationRecording]] - `uses` [INFERRED]
- [[_FakeAttack]] - `uses` [INFERRED]
- [[_FakeIntegrityScore]] - `uses` [INFERRED]
- [[instruction_envelope.py]] - `contains` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[signer()]] - `calls` [EXTRACTED]
- [[test_instruction_envelope.py]] - `imports` [EXTRACTED]
- [[test_pipeline_unit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Signed_Instruction_Envelopes__Security_Pipeline