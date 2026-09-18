---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "TelegramAPIProxy"
location: "L411"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TelegramAPIProxy
---

# Raw tool-call JSON blobs must be suppressed before Telegram delivery.

## Connections
- [[.test_raw_tool_call_json_never_leaks()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TelegramAPIProxy