---
source_file: "gateway/tests/test_rate_limit_failover.py"
type: "code"
community: "is_quota_exhausted"
location: "L72"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/is_quota_exhausted
---

# test_proxy_failover_on_post_retry_429()

## Connections
- [[A 429 that escaped the retry loop must trigger local failover.]] - `rationale_for` [EXTRACTED]
- [[LLMProxy]] - `uses` [INFERRED]
- [[asyncio_53]] - `references` [EXTRACTED]
- [[mock_forward()_18]] - `indirect_call` [INFERRED]
- [[test_rate_limit_failover.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/is_quota_exhausted
