---
source_file: "gateway/tests/test_rate_limit_failover.py"
type: "rationale"
community: "Community 979"
location: "L73"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_979
---

# A 429 that escaped the retry loop must trigger local failover.

## Connections
- [[test_proxy_failover_on_post_retry_429()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_979