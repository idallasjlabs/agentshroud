---
source_file: "gateway/tests/test_rate_limit_guard.py"
type: "rationale"
community: "Gateway Proxy Layer"
location: "L209"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Proxy_Layer
---

# No injected clock: the guard falls back to time.monotonic and still works.

## Connections
- [[test_default_clock_is_monotonic()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Proxy_Layer