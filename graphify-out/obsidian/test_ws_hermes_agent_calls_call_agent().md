---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "_mock_ws"
location: "L1573"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_mock_ws
---

# test_ws_hermes_agent_calls_call_agent()

## Connections
- [[agent=hermes must route to _call_agent (gateway forward), not _call_llm.]] - `rationale_for` [EXTRACTED]
- [[_mock_agent()_3]] - `contains` [EXTRACTED]
- [[_mock_agent()_2]] - `indirect_call` [INFERRED]
- [[_mock_llm()_2]] - `contains` [EXTRACTED]
- [[_mock_llm()_1]] - `indirect_call` [INFERRED]
- [[_pcm_bytes()]] - `calls` [EXTRACTED]
- [[app()]] - `indirect_call` [INFERRED]
- [[asyncio_71]] - `references` [EXTRACTED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_mock_ws
