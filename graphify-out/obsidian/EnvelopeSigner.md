---
source_file: "gateway/security/instruction_envelope.py"
type: "code"
community: "Pipeline Unit"
location: "L41"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Pipeline_Unit
---

# EnvelopeSigner

## Connections
- [[.__init__()_86]] - `method` [EXTRACTED]
- [[._compute_signature()]] - `method` [EXTRACTED]
- [[.sign()]] - `method` [EXTRACTED]
- [[.test_different_keys_fail_verification()]] - `calls` [EXTRACTED]
- [[.test_different_signers_same_key_verify()]] - `calls` [EXTRACTED]
- [[.test_outbound_response_is_signed_and_verifiable()]] - `calls` [EXTRACTED]
- [[.verify()]] - `method` [EXTRACTED]
- [[.wrap_system_prompt()]] - `method` [EXTRACTED]
- [[.wrap_tool_result()]] - `method` [EXTRACTED]
- [[C46 Signed Instruction Envelopes (HMAC-SHA256 tamper detection for system promptstool results)]] - `rationale_for` [EXTRACTED]
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
- [[TestPromptGuardToolResultTrustGate]] - `uses` [INFERRED]
- [[TestTrustViolationRecording]] - `uses` [INFERRED]
- [[_FakeAttack]] - `uses` [INFERRED]
- [[_FakeIntegrityScore]] - `uses` [INFERRED]
- [[instruction_envelope.py]] - `contains` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[signer()]] - `calls` [EXTRACTED]
- [[test_instruction_envelope.py]] - `imports` [EXTRACTED]
- [[test_pipeline_unit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Pipeline_Unit