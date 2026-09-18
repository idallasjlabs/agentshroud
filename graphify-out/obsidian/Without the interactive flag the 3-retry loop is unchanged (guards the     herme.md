---
source_file: "gateway/tests/test_llm_proxy_failover.py"
type: "rationale"
community: "test_llm_proxy_failover.py"
location: "L140"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_llm_proxy_failoverpy
---

# Without the interactive flag the 3-retry loop is unchanged (guards the     herme

## Connections
- [[test_forward_request_default_still_retries_429()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_llm_proxy_failoverpy