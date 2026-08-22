---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "Telegram Proxy Outbound"
location: "L4096"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Proxy_Outbound
---

# Our own protected notices must never be double-filtered.

## Connections
- [[.test_contains_high_risk_leakage_skips_protected_header_text()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Proxy_Outbound