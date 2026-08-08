---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Telegram Proxy Test Suite"
location: "L225"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Proxy_Test_Suite
---

# Updates without text (e.g. photos) should skip the pipeline.

## Connections
- [[.test_pipeline_not_called_without_text()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Proxy_Test_Suite