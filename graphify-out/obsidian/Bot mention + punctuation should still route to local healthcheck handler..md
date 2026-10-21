---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "TestInboundPipelineOnGetUpdates"
location: "L4785"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestInboundPipelineOnGetUpdates
---

# Bot mention + punctuation should still route to local healthcheck handler.

## Connections
- [[dot-test_healthcheck_with_mention_and_punctuation_is_handled_locally()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestInboundPipelineOnGetUpdates
