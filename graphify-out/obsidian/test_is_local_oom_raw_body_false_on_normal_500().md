---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "._is_local_oom()"
location: "L824"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_is_local_oom
---

# test_is_local_oom_raw_body_false_on_normal_500()

## Connections
- [[._is_local_oom()]] - `calls` [EXTRACTED]
- [[LLMProxy]] - `uses` [INFERRED]
- [[_is_local_oom returns False for non-OOM raw 500 bodies.]] - `rationale_for` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_is_local_oom