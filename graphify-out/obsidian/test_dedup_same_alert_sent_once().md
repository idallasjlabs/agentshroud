---
source_file: "gateway/tests/test_alert_telegram_relay.py"
type: "code"
community: "AlertTelegramRelay"
location: "L72"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AlertTelegramRelay
---

# test_dedup_same_alert_sent_once()

## Connections
- [[AlertTelegramRelay]] - `uses` [INFERRED]
- [[_SendSpy]] - `calls` [EXTRACTED]
- [[_alert_event()]] - `calls` [EXTRACTED]
- [[asyncio_67]] - `references` [EXTRACTED]
- [[test_alert_telegram_relay.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AlertTelegramRelay
