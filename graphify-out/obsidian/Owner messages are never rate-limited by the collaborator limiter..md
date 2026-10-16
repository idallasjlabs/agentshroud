---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "RateLimiter"
location: "L7897"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/RateLimiter
---

# Owner messages are never rate-limited by the collaborator limiter.

## Connections
- [[dot-test_owner_unaffected_by_collaborator_rate_limiter()]] - `rationale_for` [EXTRACTED]
- [[TestNoResponseGuarantee]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/RateLimiter
