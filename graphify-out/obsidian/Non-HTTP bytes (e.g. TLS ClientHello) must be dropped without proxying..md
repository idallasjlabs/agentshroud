---
source_file: "gateway/tests/test_telegram_executor.py"
type: "rationale"
community: "Telegram Executor"
location: "L46"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Executor
---

# Non-HTTP bytes (e.g. TLS ClientHello) must be dropped without proxying.

## Connections
- [[test_hermes_forwarder_drops_non_http()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Executor