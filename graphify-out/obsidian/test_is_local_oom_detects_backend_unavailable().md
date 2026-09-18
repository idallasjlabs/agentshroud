---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "._is_local_oom()"
location: "L792"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_is_local_oom
---

# test_is_local_oom_detects_backend_unavailable()

## Connections
- [[._is_local_oom()]] - `calls` [EXTRACTED]
- [[LLMProxy]] - `uses` [INFERRED]
- [[_is_local_oom returns True for backend_unavailable 503 bodies.]] - `rationale_for` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_is_local_oom