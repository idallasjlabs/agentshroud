---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "patch"
location: "L1408"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/patch
---

# test_ws_one_sentence_reply_unchanged()

## Connections
- [[Regression a single-sentence reply still produces exactly one synthesize call.]] - `rationale_for` [EXTRACTED]
- [[_mock_synthesize()]] - `contains` [EXTRACTED]
- [[_mock_synthesize()_1]] - `indirect_call` [INFERRED]
- [[_pcm_bytes()]] - `calls` [EXTRACTED]
- [[mock_stream()_13]] - `indirect_call` [INFERRED]
- [[mock_stream()_16]] - `contains` [EXTRACTED]
- [[patch]] - `calls` [INFERRED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/patch