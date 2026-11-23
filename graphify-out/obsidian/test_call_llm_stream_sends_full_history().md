---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "_call_llm_stream"
location: "L656"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_call_llm_stream
---

# test_call_llm_stream_sends_full_history()

## Connections
- [[The full messages history (system + prior turns) is sent in the request body.]] - `rationale_for` [EXTRACTED]
- [[_call_llm_stream()]] - `calls` [EXTRACTED]
- [[asyncio_50]] - `references` [EXTRACTED]
- [[mock_stream()_21]] - `contains` [EXTRACTED]
- [[mock_stream()_8]] - `indirect_call` [INFERRED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_call_llm_stream
