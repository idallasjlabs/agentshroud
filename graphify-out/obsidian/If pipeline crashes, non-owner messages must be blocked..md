---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "TelegramAPIProxy"
location: "L109"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TelegramAPIProxy
---

# If pipeline crashes, non-owner messages must be blocked.

## Connections
- [[.test_outbound_fails_closed_for_non_owner()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TelegramAPIProxy