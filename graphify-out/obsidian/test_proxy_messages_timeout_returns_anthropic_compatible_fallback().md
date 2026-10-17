---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "test_llm_proxy.py"
location: "L350"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxypy
---

# test_proxy_messages_timeout_returns_anthropic_compatible_fallback()

## Connections
- [[LLMProxy]] - `uses` [INFERRED]
- [[_FakeSanitizer]] - `calls` [EXTRACTED]
- [[_fake_forward()_5]] - `contains` [EXTRACTED]
- [[_fake_forward()_2]] - `indirect_call` [INFERRED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[test_llm_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxypy
