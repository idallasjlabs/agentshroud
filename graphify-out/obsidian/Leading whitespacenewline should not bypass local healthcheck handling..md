---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "TelegramAPIProxy"
location: "L4869"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TelegramAPIProxy
---

# Leading whitespace/newline should not bypass local healthcheck handling.

## Connections
- [[.test_healthcheck_with_leading_whitespace_is_handled_locally()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TelegramAPIProxy