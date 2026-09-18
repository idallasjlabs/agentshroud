---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "TelegramAPIProxy"
location: "L296"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TelegramAPIProxy
---

# Messages above hard size cap should be blocked to prevent split bypass.

## Connections
- [[.test_long_outbound_message_blocked_for_non_owner()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TelegramAPIProxy