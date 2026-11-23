---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "mock_stream"
location: "L1327"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/mock_stream
---

# test_ws_sentence_chunked_tts_calls_synthesize_per_sentence()

## Connections
- [[Sentence-chunked TTS synthesize() is called once per sentence; all PCM arrives…]] - `rationale_for` [EXTRACTED]
- [[_mock_synthesize()_1]] - `indirect_call` [INFERRED]
- [[_pcm_bytes()]] - `calls` [EXTRACTED]
- [[app()]] - `indirect_call` [INFERRED]
- [[mock_stream()_11]] - `contains` [EXTRACTED]
- [[mock_stream()_8]] - `indirect_call` [INFERRED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/mock_stream
