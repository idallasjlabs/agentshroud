---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "mock_stream"
location: "L1408"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/mock_stream
---

# test_ws_one_sentence_reply_unchanged()

## Connections
- [[Regression a single-sentence reply still produces exactly one synthesize call.]] - `rationale_for` [EXTRACTED]
- [[_mock_synthesize()]] - `contains` [EXTRACTED]
- [[_mock_synthesize()_1]] - `indirect_call` [INFERRED]
- [[_pcm_bytes()]] - `calls` [EXTRACTED]
- [[app()]] - `indirect_call` [INFERRED]
- [[mock_stream()_10]] - `contains` [EXTRACTED]
- [[mock_stream()_8]] - `indirect_call` [INFERRED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/mock_stream
