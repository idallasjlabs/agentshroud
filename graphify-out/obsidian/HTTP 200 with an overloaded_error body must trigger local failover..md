---
source_file: "gateway/tests/test_llm_proxy_failover.py"
type: "rationale"
community: "Community 224"
location: "L598"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_224
---

# HTTP 200 with an overloaded_error body must trigger local failover.

## Connections
- [[test_proxy_failover_anthropic_overloaded_529()]] - `rationale_for` [EXTRACTED]
- [[test_proxy_failover_anthropic_overloaded_http200()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_224