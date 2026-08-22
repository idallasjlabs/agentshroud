---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Telegram Inbound Proxy Tests"
location: "L1455"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Inbound_Proxy_Tests
---

# Unicode zero-width obfuscation should not bypass blocked command enforcement.

## Connections
- [[.test_blocked_command_with_zero_width_char_is_quarantined()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Inbound_Proxy_Tests