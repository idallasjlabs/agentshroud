---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "patch"
location: "L573"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/patch
---

# test_call_llm_stream_yields_sentences()

## Connections
- [[_call_llm_stream posts to v1chatcompletions with streamtrue and yields each…]] - `rationale_for` [EXTRACTED]
- [[_call_llm_stream()]] - `calls` [EXTRACTED]
- [[_openai_delta_lines()]] - `calls` [EXTRACTED]
- [[asyncio_1]] - `references` [EXTRACTED]
- [[mock_stream()_13]] - `indirect_call` [INFERRED]
- [[patch]] - `calls` [INFERRED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/patch