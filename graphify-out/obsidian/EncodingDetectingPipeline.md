---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "models.py"
location: "L102"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/modelspy
---

# EncodingDetectingPipeline

## Connections
- [[.process_inbound()_9]] - `method` [EXTRACTED]
- [[.test_encoding_detected_on_getUpdates()]] - `calls` [EXTRACTED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[Pipeline that detects base64-encoded injections.]] - `rationale_for` [EXTRACTED]
- [[RateLimiter]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[test_telegram_proxy_inbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/modelspy