---
source_file: "gateway/tests/test_router_openai_translation.py"
type: "code"
community: "AgentTarget"
location: "L100"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AgentTarget
---

# test_openai_target_returns_content_string()

## Connections
- [[AgentTarget]] - `uses` [INFERRED]
- [[asyncio_56]] - `references` [EXTRACTED]
- [[forward_to_agent extracts choices0.message.content and returns a string.]] - `rationale_for` [EXTRACTED]
- [[mock_post()_5]] - `contains` [EXTRACTED]
- [[mock_post()_6]] - `indirect_call` [INFERRED]
- [[test_router_openai_translation.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AgentTarget
