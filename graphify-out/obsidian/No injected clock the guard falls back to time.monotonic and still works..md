---
source_file: "gateway/tests/test_rate_limit_guard.py"
type: "rationale"
community: "Community 177"
location: "L209"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_177
---

# No injected clock: the guard falls back to time.monotonic and still works.

## Connections
- [[test_default_clock_is_monotonic()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_177