---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "patch"
location: "L1134"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/patch
---

# test_call_agent_stream_yields_sentences_in_order()

## Connections
- [[_call_agent_stream POSTs to forwardstream and yields each sentence event as…]] - `rationale_for` [EXTRACTED]
- [[_call_agent_stream()]] - `calls` [EXTRACTED]
- [[_sse_body()]] - `calls` [EXTRACTED]
- [[asyncio_1]] - `references` [EXTRACTED]
- [[mock_stream()_8]] - `contains` [EXTRACTED]
- [[mock_stream()_13]] - `indirect_call` [INFERRED]
- [[patch]] - `calls` [INFERRED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/patch