---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "Voice Gateway Routing Tests"
location: "L3454"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Voice_Gateway_Routing_Tests
---

# test_tts_resume_after_mid_stream_disconnect()

## Connections
- [[If the socket dies during the TTS downlink, the NEXT connection must receive…]] - `rationale_for` [EXTRACTED]
- [[_mock_agent()]] - `contains` [EXTRACTED]
- [[_mock_agent()_2]] - `indirect_call` [INFERRED]
- [[_mock_ws()]] - `calls` [EXTRACTED]
- [[_pcm_bytes()]] - `calls` [EXTRACTED]
- [[_send_bytes_then_die()]] - `indirect_call` [INFERRED]
- [[asyncio_1]] - `references` [EXTRACTED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Voice_Gateway_Routing_Tests