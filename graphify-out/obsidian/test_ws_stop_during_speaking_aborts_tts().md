---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "Voice Gateway Routing Tests"
location: "L2325"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Voice_Gateway_Routing_Tests
---

# test_ws_stop_during_speaking_aborts_tts()

## Connections
- [[A device 'STOP' text frame during the TTS send phase must abort the remaining…]] - `rationale_for` [EXTRACTED]
- [[_mock_agent()_5]] - `contains` [EXTRACTED]
- [[_mock_agent()_2]] - `indirect_call` [INFERRED]
- [[_mock_ws()]] - `calls` [EXTRACTED]
- [[_pcm_bytes()]] - `calls` [EXTRACTED]
- [[_push_stop_on_first_pcm()]] - `indirect_call` [INFERRED]
- [[asyncio_1]] - `references` [EXTRACTED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Voice_Gateway_Routing_Tests