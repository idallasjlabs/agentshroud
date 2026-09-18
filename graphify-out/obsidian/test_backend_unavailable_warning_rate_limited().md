---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "test_llm_proxy.py"
location: "L682"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxypy
---

# test_backend_unavailable_warning_rate_limited()

## Connections
- [[LLMProxy]] - `uses` [INFERRED]
- [[Repeated connect failures log one WARNING per window, not per request.]] - `rationale_for` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[mock_forward()]] - `indirect_call` [INFERRED]
- [[mock_forward()_1]] - `contains` [EXTRACTED]
- [[test_llm_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxypy