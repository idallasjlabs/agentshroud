---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "rationale"
community: "test_llm_proxy_local_parity.py"
location: "L1087"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_llm_proxy_local_paritypy
---

# The shim must not leak onto backends that accept these fields (LM Studio).

## Connections
- [[test_non_fieldflare_local_route_keeps_fields]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_llm_proxy_local_paritypy
