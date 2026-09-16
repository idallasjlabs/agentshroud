---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "Voice Gateway Routing Tests"
location: "L3200"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Voice_Gateway_Routing_Tests
---

# test_ws_tell_agent_command_with_chained_instruction()

## Connections
- [[Tell Hermes to check my email.' must switch the agent AND route the remaining…]] - `rationale_for` [EXTRACTED]
- [[_capture_synth()_3]] - `contains` [EXTRACTED]
- [[_capture_synth()]] - `indirect_call` [INFERRED]
- [[_llm_must_not_be_called()_1]] - `contains` [EXTRACTED]
- [[_llm_must_not_be_called()_4]] - `indirect_call` [INFERRED]
- [[_mock_agent()_6]] - `contains` [EXTRACTED]
- [[_mock_agent()_2]] - `indirect_call` [INFERRED]
- [[_mock_ws()]] - `calls` [EXTRACTED]
- [[_pcm_bytes()]] - `calls` [EXTRACTED]
- [[asyncio_1]] - `references` [EXTRACTED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Voice_Gateway_Routing_Tests