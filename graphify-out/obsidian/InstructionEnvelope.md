---
source_file: "gateway/security/instruction_envelope.py"
type: "code"
community: "InstructionEnvelope"
location: "L31"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/InstructionEnvelope
---

# InstructionEnvelope

## Connections
- [[dot-sign()]] - `calls` [EXTRACTED]
- [[dot-test_outbound_response_is_signed_and_verifiable()]] - `calls` [EXTRACTED]
- [[dot-verify()_1]] - `references` [EXTRACTED]
- [[dot-wrap_system_prompt()]] - `references` [EXTRACTED]
- [[dot-wrap_tool_result()]] - `references` [EXTRACTED]
- [[A signed instruction or tool result.]] - `rationale_for` [EXTRACTED]
- [[TestEnvelopeSigner]] - `uses` [INFERRED]
- [[TestEnvelopeSignerInPipeline]] - `uses` [INFERRED]
- [[instruction_envelope.py]] - `contains` [EXTRACTED]
- [[test_instruction_envelope.py]] - `imports` [EXTRACTED]
- [[test_pipeline_unit.py]] - `imports` [EXTRACTED]
- [[unwrap_untrusted()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/InstructionEnvelope
