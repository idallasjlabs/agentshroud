---
source_file: "gateway/tests/test_rate_limit_failover.py"
type: "rationale"
community: "is_rate_limited_post_retry()"
location: "L73"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/is_rate_limited_post_retry
---

# A 429 that escaped the retry loop must trigger local failover.

## Connections
- [[test_proxy_failover_on_post_retry_429()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/is_rate_limited_post_retry