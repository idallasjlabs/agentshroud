---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "_make_proxy()"
location: "L664"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_make_proxy
---

# test_hermes_openai_path_local_model_routed_correctly()

## Connections
- [[Hermes sends OpenAI-compat requests; local qwen3 model routes to LM Studio.]] - `rationale_for` [EXTRACTED]
- [[_fake_forward()_11]] - `contains` [EXTRACTED]
- [[_fake_forward()_24]] - `indirect_call` [INFERRED]
- [[_make_proxy()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_make_proxy
