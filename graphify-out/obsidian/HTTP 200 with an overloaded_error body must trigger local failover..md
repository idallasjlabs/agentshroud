---
source_file: "gateway/tests/test_llm_proxy_failover.py"
type: "rationale"
community: "Gateway Test Suite"
location: "L597"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# HTTP 200 with an overloaded_error body must trigger local failover.

## Connections
- [[test_proxy_failover_anthropic_overloaded_529()]] - `rationale_for` [EXTRACTED]
- [[test_proxy_failover_anthropic_overloaded_http200()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Test_Suite