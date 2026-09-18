---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "TelegramAPIProxy"
location: "L5694"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TelegramAPIProxy
---

# Malformed callback payloads should not crash inbound processing.

## Connections
- [[.test_egress_callback_non_dict_result_is_handled()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TelegramAPIProxy