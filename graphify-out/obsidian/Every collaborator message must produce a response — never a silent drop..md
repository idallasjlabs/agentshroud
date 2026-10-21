---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: ".test_unknown_user_always_gets_pending_or_rate_limit_notice()"
location: "L7946"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_unknown_user_always_gets_pending_or_rate_limit_notice
---

# Every collaborator message must produce a response — never a silent drop.

## Connections
- [[TestNoResponseGuarantee]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_unknown_user_always_gets_pending_or_rate_limit_notice
