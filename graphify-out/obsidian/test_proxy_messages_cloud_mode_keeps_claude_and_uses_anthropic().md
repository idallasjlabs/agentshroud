---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "test_llm_proxy.py"
location: "L120"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxypy
---

# test_proxy_messages_cloud_mode_keeps_claude_and_uses_anthropic()

## Connections
- [[LLMProxy]] - `uses` [INFERRED]
- [[_FakeSanitizer_1]] - `calls` [EXTRACTED]
- [[_fake_forward()_17]] - `contains` [EXTRACTED]
- [[_fake_forward()_19]] - `indirect_call` [INFERRED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[test_llm_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxypy