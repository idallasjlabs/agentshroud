---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "test_voice_gateway.py"
location: "L272"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_voice_gatewaypy
---

# test_proxy_messages_plain_openai_model_substitutes_real_key()

## Connections
- [[LLMProxy]] - `uses` [INFERRED]
- [[Regression 2026-08-07 a plain (non-Claude, non-Gemini, non-local) OpenAI-model…]] - `rationale_for` [EXTRACTED]
- [[_FakeSanitizer]] - `calls` [EXTRACTED]
- [[_fake_forward()_1]] - `contains` [EXTRACTED]
- [[_fake_forward()_2]] - `indirect_call` [INFERRED]
- [[asyncio_2]] - `references` [EXTRACTED]
- [[fake_open()]] - `indirect_call` [INFERRED]
- [[test_llm_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_voice_gatewaypy
