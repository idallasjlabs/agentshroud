---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "TelegramAPIProxy"
location: "L753"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TelegramAPIProxy
---

# Unknown model errors should be rewritten without leaking raw stack text.

## Connections
- [[.test_unknown_model_error_is_sanitized()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TelegramAPIProxy