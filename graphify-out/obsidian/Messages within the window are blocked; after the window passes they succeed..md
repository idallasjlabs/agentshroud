---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "RateLimiter"
location: "L7849"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/RateLimiter
---

# Messages within the window are blocked; after the window passes they succeed.

## Connections
- [[dot-test_collaborator_rate_limit_resets_after_window()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/RateLimiter
