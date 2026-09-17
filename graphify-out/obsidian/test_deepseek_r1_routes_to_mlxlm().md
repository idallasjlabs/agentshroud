---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "test_llm_proxy_local_parity.py"
location: "L733"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxy_local_paritypy
---

# test_deepseek_r1_routes_to_mlxlm()

## Connections
- [[_fake_forward()_1]] - `contains` [EXTRACTED]
- [[_fake_forward()_15]] - `indirect_call` [INFERRED]
- [[_make_proxy()]] - `calls` [EXTRACTED]
- [[asyncio_2]] - `references` [EXTRACTED]
- [[deepseek-r1 is routed to mlx_lm endpoint.]] - `rationale_for` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxy_local_paritypy