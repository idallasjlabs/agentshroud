---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "TelegramAPIProxy"
location: "L2840"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TelegramAPIProxy
---

# Non-domain hosts should not queue egress approval requests.

## Connections
- [[.test_raw_web_fetch_json_invalid_host_does_not_queue_approval()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TelegramAPIProxy