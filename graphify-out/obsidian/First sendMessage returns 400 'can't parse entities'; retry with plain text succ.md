---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "Telegram Proxy Outbound"
location: "L4538"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Proxy_Outbound
---

# First sendMessage returns 400 'can't parse entities'; retry with plain text succ

## Connections
- [[.test_400_retry_succeeds_when_text_strippable()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Proxy_Outbound