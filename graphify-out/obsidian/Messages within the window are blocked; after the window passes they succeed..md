---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Telegram Proxy Inbound"
location: "L7849"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Proxy_Inbound
---

# Messages within the window are blocked; after the window passes they succeed.

## Connections
- [[.test_collaborator_rate_limit_resets_after_window()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Proxy_Inbound