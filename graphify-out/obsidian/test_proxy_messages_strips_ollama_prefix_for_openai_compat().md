---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "test_llm_proxy.py"
location: "L155"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxypy
---

# test_proxy_messages_strips_ollama_prefix_for_openai_compat()

## Connections
- [[LLMProxy]] - `uses` [INFERRED]
- [[_FakeSanitizer_1]] - `calls` [EXTRACTED]
- [[_fake_forward()_19]] - `indirect_call` [INFERRED]
- [[_fake_forward()_20]] - `contains` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[test_llm_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxypy