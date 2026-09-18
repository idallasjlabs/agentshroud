---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "test_llm_proxy.py"
location: "L479"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxypy
---

# test_credential_injector_not_applied_for_non_anthropic_dest()

## Connections
- [[LLMProxy]] - `uses` [INFERRED]
- [[Localnon-Anthropic destination injector must NOT be called.]] - `rationale_for` [EXTRACTED]
- [[_FakeSanitizer_1]] - `calls` [EXTRACTED]
- [[_TrackingInjector]] - `calls` [EXTRACTED]
- [[_make_fake_urlopen()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[test_llm_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxypy