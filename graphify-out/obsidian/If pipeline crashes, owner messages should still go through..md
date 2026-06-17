---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "Telegram Outbound Test Coverage"
location: "L137"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Outbound_Test_Coverage
---

# If pipeline crashes, owner messages should still go through.

## Connections
- [[.test_outbound_owner_exempt_from_fail_closed()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Outbound_Test_Coverage