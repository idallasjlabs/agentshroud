---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "patch"
location: "L924"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/patch
---

# test_ws_full_utterance_state_sequence()

## Connections
- [[LISTEN → binary PCM → END → STT → forwardstream → TTS → PCM + END → idle.]] - `rationale_for` [EXTRACTED]
- [[_pcm_bytes()]] - `calls` [EXTRACTED]
- [[mock_stream()_13]] - `indirect_call` [INFERRED]
- [[mock_stream()_15]] - `contains` [EXTRACTED]
- [[patch]] - `calls` [INFERRED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/patch