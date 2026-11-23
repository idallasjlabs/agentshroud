---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "mock_stream"
location: "L924"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/mock_stream
---

# test_ws_full_utterance_state_sequence()

## Connections
- [[LISTEN → binary PCM → END → STT → forwardstream → TTS → PCM + END → idle.]] - `rationale_for` [EXTRACTED]
- [[_pcm_bytes()]] - `calls` [EXTRACTED]
- [[app()]] - `indirect_call` [INFERRED]
- [[mock_stream()_9]] - `contains` [EXTRACTED]
- [[mock_stream()_8]] - `indirect_call` [INFERRED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/mock_stream
