---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "rationale"
community: "._is_local_oom()"
location: "L825"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_is_local_oom
---

# _is_local_oom returns False for non-OOM raw 500 bodies.

## Connections
- [[test_is_local_oom_raw_body_false_on_normal_500()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_is_local_oom