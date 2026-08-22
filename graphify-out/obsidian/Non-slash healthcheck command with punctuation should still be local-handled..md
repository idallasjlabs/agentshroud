---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Telegram Inbound Proxy Tests"
location: "L4835"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Inbound_Proxy_Tests
---

# Non-slash healthcheck command with punctuation should still be local-handled.

## Connections
- [[.test_healthcheck_word_with_punctuation_is_handled_locally()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Inbound_Proxy_Tests