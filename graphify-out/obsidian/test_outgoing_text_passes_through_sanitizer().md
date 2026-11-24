---
source_file: "gateway/tests/test_alert_telegram_relay.py"
type: "code"
community: "AlertTelegramRelay"
location: "L166"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AlertTelegramRelay
---

# test_outgoing_text_passes_through_sanitizer()

## Connections
- [[AlertTelegramRelay]] - `uses` [INFERRED]
- [[_SendSpy]] - `calls` [EXTRACTED]
- [[_alert_event()]] - `calls` [EXTRACTED]
- [[asyncio_64]] - `references` [EXTRACTED]
- [[test_alert_telegram_relay.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AlertTelegramRelay
