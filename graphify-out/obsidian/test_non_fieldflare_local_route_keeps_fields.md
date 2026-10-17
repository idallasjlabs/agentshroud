---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "test_llm_proxy_local_parity.py"
location: "L1085-L1113"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxy_local_paritypy
---

# test_non_fieldflare_local_route_keeps_fields

## Connections
- [[dot-proxy_messages()]] - `calls` [INFERRED]
- [[LLMProxy.proxy_messages (non-streaming)]] - `calls` [EXTRACTED]
- [[The shim must not leak onto backends that accept these fields (LM Studio).]] - `rationale_for` [EXTRACTED]
- [[_fake_forward()_21]] - `contains` [EXTRACTED]
- [[_fake_forward()_22]] - `indirect_call` [INFERRED]
- [[_make_proxy()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxy_local_paritypy
