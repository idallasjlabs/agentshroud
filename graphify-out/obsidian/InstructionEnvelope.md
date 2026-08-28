---
source_file: "gateway/security/instruction_envelope.py"
type: "code"
community: "Key Vault & Audit Chain"
location: "L30"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Key_Vault__Audit_Chain
---

# InstructionEnvelope

## Connections
- [[.sign()]] - `references` [EXTRACTED]
- [[.test_outbound_response_is_signed_and_verifiable()]] - `calls` [EXTRACTED]
- [[.verify()]] - `references` [EXTRACTED]
- [[.wrap_system_prompt()]] - `references` [EXTRACTED]
- [[.wrap_tool_result()]] - `references` [EXTRACTED]
- [[A signed instruction or tool result.]] - `rationale_for` [EXTRACTED]
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
- [[test_instruction_envelope.py]] - `imports` [EXTRACTED]
- [[test_pipeline_unit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Key_Vault__Audit_Chain