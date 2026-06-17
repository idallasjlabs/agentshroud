---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Authentication & Rate Limiting"
location: "L3660"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Authentication__Rate_Limiting
---

# Repeated rate-limited messages should each receive a deterministic notice.

## Connections
- [[.test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Authentication__Rate_Limiting