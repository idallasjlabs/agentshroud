---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "test_llm_proxy_local_parity.py (2)"
location: "L1085-L1113"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxy_local_paritypy_2
---

# test_non_fieldflare_local_route_keeps_fields

## Connections
- [[dot-proxy_messages()]] - `calls` [INFERRED]
- [[LLMProxy.proxy_messages (non-streaming)]] - `calls` [EXTRACTED]
- [[The shim must not leak onto backends that accept these fields (LM Studio).]] - `rationale_for` [EXTRACTED]
- [[_fake_forward()_23]] - `contains` [EXTRACTED]
- [[_fake_forward()_24]] - `indirect_call` [INFERRED]
- [[_make_proxy()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxy_local_paritypy_2
