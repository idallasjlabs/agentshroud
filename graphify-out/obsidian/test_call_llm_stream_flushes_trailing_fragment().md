---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "test_voice_gateway.py"
location: "L595"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_voice_gatewaypy
---

# test_call_llm_stream_flushes_trailing_fragment()

## Connections
- [[A final delta with no terminal punctuation is flushed once the SSE stream ends,…]] - `rationale_for` [EXTRACTED]
- [[_call_llm_stream()]] - `calls` [EXTRACTED]
- [[_openai_delta_lines()]] - `calls` [EXTRACTED]
- [[asyncio_71]] - `references` [EXTRACTED]
- [[mock_stream()_16]] - `contains` [EXTRACTED]
- [[mock_stream()_20]] - `indirect_call` [INFERRED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_voice_gatewaypy
