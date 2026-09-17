---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "patch"
location: "L1256"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/patch
---

# test_call_agent_stream_malformed_json_line_skipped_not_fatal()

## Connections
- [[A single corrupted SSE line logs a warning and is skipped — it must not abort…]] - `rationale_for` [EXTRACTED]
- [[_call_agent_stream()]] - `calls` [EXTRACTED]
- [[_sse_body()]] - `calls` [EXTRACTED]
- [[asyncio_1]] - `references` [EXTRACTED]
- [[mock_stream()_3]] - `contains` [EXTRACTED]
- [[mock_stream()_13]] - `indirect_call` [INFERRED]
- [[patch]] - `calls` [INFERRED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/patch