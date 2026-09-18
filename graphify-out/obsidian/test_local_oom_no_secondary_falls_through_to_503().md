---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "test_llm_proxy_local_parity.py"
location: "L413"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxy_local_paritypy
---

# test_local_oom_no_secondary_falls_through_to_503()

## Connections
- [[If no secondary is configured and primary hits OOM, 503 is returned.]] - `rationale_for` [EXTRACTED]
- [[_fake_forward()_7]] - `contains` [EXTRACTED]
- [[_fake_forward()_15]] - `indirect_call` [INFERRED]
- [[_make_proxy()]] - `calls` [EXTRACTED]
- [[asyncio_2]] - `references` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxy_local_paritypy