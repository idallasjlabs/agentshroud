---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "patch"
location: "L1327"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/patch
---

# test_ws_sentence_chunked_tts_calls_synthesize_per_sentence()

## Connections
- [[Sentence-chunked TTS synthesize() is called once per sentence; all PCM arrives]] - `rationale_for` [EXTRACTED]
- [[_mock_synthesize()_1]] - `indirect_call` [INFERRED]
- [[_pcm_bytes()]] - `calls` [EXTRACTED]
- [[mock_stream()_13]] - `indirect_call` [INFERRED]
- [[mock_stream()_17]] - `contains` [EXTRACTED]
- [[patch]] - `calls` [INFERRED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/patch