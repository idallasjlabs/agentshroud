---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "test_voice_gateway.py"
location: "L83"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_voice_gatewaypy
---

# test_proxy_messages_rewrites_claude_opus_to_local_model()

## Connections
- [[LLMProxy]] - `uses` [INFERRED]
- [[_FakeSanitizer]] - `calls` [EXTRACTED]
- [[_fake_forward()_2]] - `indirect_call` [INFERRED]
- [[asyncio_2]] - `references` [EXTRACTED]
- [[test_llm_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_voice_gatewaypy
