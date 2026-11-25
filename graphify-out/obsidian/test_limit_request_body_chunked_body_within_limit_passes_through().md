---
source_file: "gateway/tests/test_main_simple.py"
type: "code"
community: "AgentTarget"
location: "L136"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AgentTarget
---

# test_limit_request_body_chunked_body_within_limit_passes_through()

## Connections
- [[asyncio_52]] - `references` [EXTRACTED]
- [[limit_request_body re-injects a fully-read chunked body and calls downstream.]] - `rationale_for` [EXTRACTED]
- [[limit_request_body()]] - `calls` [EXTRACTED]
- [[mock_call_next()_1]] - `contains` [EXTRACTED]
- [[mock_call_next()_3]] - `indirect_call` [INFERRED]
- [[small_stream()]] - `indirect_call` [INFERRED]
- [[test_main_simple.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AgentTarget
