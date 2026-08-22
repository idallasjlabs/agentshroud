---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Telegram Proxy Inbound"
location: "L8895"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Telegram_Proxy_Inbound
---

# TestIsGroupMessage

## Connections
- [[.test_channel_is_not_group()]] - `method` [EXTRACTED]
- [[.test_group_is_group()]] - `method` [EXTRACTED]
- [[.test_missing_chat_is_not_group()]] - `method` [EXTRACTED]
- [[.test_private_is_not_group()]] - `method` [EXTRACTED]
- [[.test_supergroup_is_group()]] - `method` [EXTRACTED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RateLimiter]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[Unit tests for TelegramAPIProxy._is_group_message().]] - `rationale_for` [EXTRACTED]
- [[test_telegram_proxy_inbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Telegram_Proxy_Inbound