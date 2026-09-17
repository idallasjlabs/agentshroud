---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "asyncio"
location: "L1522"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/asyncio
---

# test_ws_direct_agent_calls_call_llm()

## Connections
- [[agent=direct must route to _call_llm (fast path), not forward.]] - `rationale_for` [EXTRACTED]
- [[_mock_agent()_2]] - `indirect_call` [INFERRED]
- [[_mock_llm()_1]] - `indirect_call` [INFERRED]
- [[_pcm_bytes()]] - `calls` [EXTRACTED]
- [[asyncio_1]] - `references` [EXTRACTED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/asyncio