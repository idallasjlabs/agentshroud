---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "Voice Gateway Routing Tests"
location: "L2977"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Voice_Gateway_Routing_Tests
---

# test_ws_use_local_command_confirms_with_model_name()

## Connections
- [[_agent_must_not_be_called()_3]] - `contains` [EXTRACTED]
- [[_agent_must_not_be_called()_7]] - `indirect_call` [INFERRED]
- [[_capture_synth()_4]] - `contains` [EXTRACTED]
- [[_capture_synth()]] - `indirect_call` [INFERRED]
- [[_llm_must_not_be_called()_2]] - `contains` [EXTRACTED]
- [[_llm_must_not_be_called()_4]] - `indirect_call` [INFERRED]
- [[_mock_ws()]] - `calls` [EXTRACTED]
- [[_pcm_bytes()]] - `calls` [EXTRACTED]
- [[asyncio_1]] - `references` [EXTRACTED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]
- [[use qwen' sets agent='direct', model='qwen3-14b', and confirms with the actual…]] - `rationale_for` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Voice_Gateway_Routing_Tests