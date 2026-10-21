---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "test_telegram_proxy_inbound.py"
location: "L243"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_telegram_proxy_inboundpy
---

# Updates without text (e.g. photos) should skip the pipeline.

## Connections
- [[dot-test_pipeline_not_called_without_text()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_telegram_proxy_inboundpy
