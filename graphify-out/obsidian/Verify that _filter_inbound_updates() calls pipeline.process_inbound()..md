---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "PII Config & Test Fixtures"
location: "L152"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Config__Test_Fixtures
---

# Verify that _filter_inbound_updates() calls pipeline.process_inbound().

## Connections
- [[TestInboundPipelineOnGetUpdates]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Config__Test_Fixtures