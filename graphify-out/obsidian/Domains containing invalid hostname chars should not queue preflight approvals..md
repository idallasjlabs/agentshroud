---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Telegram Proxy Test Suite"
location: "L6548"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Proxy_Test_Suite
---

# Domains containing invalid hostname chars should not queue preflight approvals.

## Connections
- [[.test_non_owner_domain_with_invalid_chars_does_not_queue_egress_preflight()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Proxy_Test_Suite