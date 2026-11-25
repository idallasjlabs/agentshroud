---
source_file: "gateway/tests/test_router_openai_translation.py"
type: "code"
community: "_mock_response"
location: "L100"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_mock_response
---

# test_openai_target_returns_content_string()

## Connections
- [[AgentTarget]] - `uses` [INFERRED]
- [[asyncio_65]] - `references` [EXTRACTED]
- [[forward_to_agent extracts choices0.message.content and returns a string.]] - `rationale_for` [EXTRACTED]
- [[mock_post()_9]] - `contains` [EXTRACTED]
- [[mock_post()_10]] - `indirect_call` [INFERRED]
- [[test_router_openai_translation.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_mock_response
