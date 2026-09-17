---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "test_llm_proxy.py"
location: "L191"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxypy
---

# test_proxy_messages_strips_openai_local_prefix_and_routes_to_backend()

## Connections
- [[LLMProxy]] - `uses` [INFERRED]
- [[Regression 2026-09-16 openai-local is AgentShroud's own local-model…]] - `rationale_for` [EXTRACTED]
- [[_FakeSanitizer_1]] - `calls` [EXTRACTED]
- [[_fake_forward()_19]] - `indirect_call` [INFERRED]
- [[_fake_forward()_21]] - `contains` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[test_llm_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxypy