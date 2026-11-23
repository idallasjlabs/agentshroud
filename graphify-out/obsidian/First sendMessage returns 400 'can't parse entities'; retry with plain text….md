---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "TestTelegram400Retry"
location: "L4538"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestTelegram400Retry
---

# First sendMessage returns 400 'can't parse entities'; retry with plain text…

## Connections
- [[dot-test_400_retry_succeeds_when_text_strippable()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestTelegram400Retry
