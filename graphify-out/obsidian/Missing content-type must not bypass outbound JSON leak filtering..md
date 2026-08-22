---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "Telegram Outbound Proxy Tests"
location: "L1862"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Outbound_Proxy_Tests
---

# Missing content-type must not bypass outbound JSON leak filtering.

## Connections
- [[.test_json_without_content_type_is_still_filtered()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Outbound_Proxy_Tests