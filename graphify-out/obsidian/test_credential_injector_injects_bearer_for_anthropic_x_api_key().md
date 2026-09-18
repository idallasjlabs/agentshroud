---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "test_llm_proxy.py"
location: "L428"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxypy
---

# test_credential_injector_injects_bearer_for_anthropic_x_api_key()

## Connections
- [[Anthropic-bound request with x-api-key injector injects Bearer + beta, strips…]] - `rationale_for` [EXTRACTED]
- [[LLMProxy]] - `uses` [INFERRED]
- [[_FakeSanitizer_1]] - `calls` [EXTRACTED]
- [[_TrackingInjector]] - `calls` [EXTRACTED]
- [[_make_fake_urlopen()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[test_llm_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxypy