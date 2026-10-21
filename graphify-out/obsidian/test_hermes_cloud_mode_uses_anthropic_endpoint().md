---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "_make_proxy()"
location: "L698"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_make_proxy
---

# test_hermes_cloud_mode_uses_anthropic_endpoint()

## Connections
- [[In cloud mode, Hermes Claude model routes to Anthropic endpoint.]] - `rationale_for` [EXTRACTED]
- [[_fake_forward()_10]] - `contains` [EXTRACTED]
- [[_fake_forward()_24]] - `indirect_call` [INFERRED]
- [[_make_proxy()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_make_proxy
