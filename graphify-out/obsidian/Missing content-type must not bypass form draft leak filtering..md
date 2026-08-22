---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "Telegram Outbound Proxy Tests"
location: "L1875"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Outbound_Proxy_Tests
---

# Missing content-type must not bypass form draft leak filtering.

## Connections
- [[.test_urlencoded_without_content_type_caption_is_still_filtered()]] - `rationale_for` [EXTRACTED]
- [[.test_urlencoded_without_content_type_draft_is_still_filtered()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Outbound_Proxy_Tests