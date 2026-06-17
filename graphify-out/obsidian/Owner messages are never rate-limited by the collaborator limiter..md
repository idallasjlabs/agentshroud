---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Authentication & Rate Limiting"
location: "L7797"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Authentication__Rate_Limiting
---

# Owner messages are never rate-limited by the collaborator limiter.

## Connections
- [[.test_owner_unaffected_by_collaborator_rate_limiter()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Authentication__Rate_Limiting