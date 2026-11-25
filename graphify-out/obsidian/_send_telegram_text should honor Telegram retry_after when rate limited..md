---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "PassthroughPipeline"
location: "L3915"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PassthroughPipeline
---

# _send_telegram_text should honor Telegram retry_after when rate limited.

## Connections
- [[dot-test_send_telegram_text_honors_retry_after_on_http_429()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PassthroughPipeline
