---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "Voice Gateway Routing Tests"
location: "L3030"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Voice_Gateway_Routing_Tests
---

# test_ws_use_local_command_reflects_live_voice_model()

## Connections
- [[_agent_must_not_be_called()_4]] - `contains` [EXTRACTED]
- [[_agent_must_not_be_called()_7]] - `indirect_call` [INFERRED]
- [[_capture_synth()_5]] - `contains` [EXTRACTED]
- [[_capture_synth()]] - `indirect_call` [INFERRED]
- [[_llm_must_not_be_called()_3]] - `contains` [EXTRACTED]
- [[_llm_must_not_be_called()_4]] - `indirect_call` [INFERRED]
- [[_mock_ws()]] - `calls` [EXTRACTED]
- [[_pcm_bytes()]] - `calls` [EXTRACTED]
- [[asyncio_1]] - `references` [EXTRACTED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]
- [[use local' must confirm with and display whatever _VOICE_MODEL currently is,…]] - `rationale_for` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Voice_Gateway_Routing_Tests