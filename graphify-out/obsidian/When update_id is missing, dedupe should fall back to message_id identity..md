---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Telegram Proxy Test Suite"
location: "L5165"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Proxy_Test_Suite
---

# When update_id is missing, dedupe should fall back to message_id identity.

## Connections
- [[.test_healthcheck_local_notice_dedupe_handles_missing_update_id()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Proxy_Test_Suite