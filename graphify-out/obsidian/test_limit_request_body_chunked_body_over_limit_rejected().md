---
source_file: "gateway/tests/test_main_simple.py"
type: "code"
community: "AgentTarget"
location: "L162"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AgentTarget
---

# test_limit_request_body_chunked_body_over_limit_rejected()

## Connections
- [[asyncio_52]] - `references` [EXTRACTED]
- [[limit_request_body rejects chunked bodies over 1MB with 413.]] - `rationale_for` [EXTRACTED]
- [[limit_request_body()]] - `calls` [EXTRACTED]
- [[mock_call_next()]] - `contains` [EXTRACTED]
- [[mock_call_next()_3]] - `indirect_call` [INFERRED]
- [[oversized_stream()]] - `indirect_call` [INFERRED]
- [[test_main_simple.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AgentTarget
