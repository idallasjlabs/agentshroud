---
source_file: "gateway/tests/test_llm_proxy_failover.py"
type: "rationale"
community: "test_llm_proxy_failover.py"
location: "L663"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_llm_proxy_failoverpy
---

# A healthy 200 message body must NOT be failed over.

## Connections
- [[test_proxy_normal_200_passthrough_untouched()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_llm_proxy_failoverpy