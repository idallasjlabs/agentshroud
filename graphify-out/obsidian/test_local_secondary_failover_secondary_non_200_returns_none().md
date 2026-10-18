---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "_make_proxy()"
location: "L874"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_make_proxy
---

# test_local_secondary_failover_secondary_non_200_returns_none()

## Connections
- [[Secondary model returning non-200 increments failed stat and returns None.]] - `rationale_for` [EXTRACTED]
- [[_fake_forward()_20]] - `contains` [EXTRACTED]
- [[_fake_forward()_24]] - `indirect_call` [INFERRED]
- [[_make_proxy()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_make_proxy
