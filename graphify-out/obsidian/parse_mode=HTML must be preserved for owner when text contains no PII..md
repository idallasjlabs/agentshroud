---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "Telegram Proxy Outbound"
location: "L4411"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Proxy_Outbound
---

# parse_mode=HTML must be preserved for owner when text contains no PII.

## Connections
- [[.test_parse_mode_preserved_when_no_pii_detected()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Proxy_Outbound