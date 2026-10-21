---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "TestCollaboratorPromptClassifiers"
location: "L1052-L1082"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TestCollaboratorPromptClassifiers
---

# test_fieldflare_route_strips_unsupported_fields_non_streaming

## Connections
- [[dot-proxy_messages()]] - `calls` [INFERRED]
- [[LLMProxy.proxy_messages (non-streaming)]] - `calls` [EXTRACTED]
- [[_fake_forward()_9]] - `contains` [EXTRACTED]
- [[_fake_forward()_24]] - `indirect_call` [INFERRED]
- [[_make_proxy()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[proxy_messages applies the shim only on the Fieldflare route, before forwarding.]] - `rationale_for` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/TestCollaboratorPromptClassifiers
