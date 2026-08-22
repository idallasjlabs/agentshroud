---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Telegram Inbound Proxy Tests"
location: "L225"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Inbound_Proxy_Tests
---

# Updates without text (e.g. photos) should skip the pipeline.

## Connections
- [[.test_pipeline_not_called_without_text()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Inbound_Proxy_Tests