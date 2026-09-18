---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "test_llm_proxy_local_parity.py"
location: "L664"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxy_local_paritypy
---

# test_hermes_openai_path_local_model_routed_correctly()

## Connections
- [[Hermes sends OpenAI-compat requests; local qwen3 model routes to LM Studio.]] - `rationale_for` [EXTRACTED]
- [[_fake_forward()_3]] - `contains` [EXTRACTED]
- [[_fake_forward()_15]] - `indirect_call` [INFERRED]
- [[_make_proxy()]] - `calls` [EXTRACTED]
- [[asyncio_2]] - `references` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxy_local_paritypy