---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "TestInboundPipelineOnGetUpdates"
location: "L4853"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestInboundPipelineOnGetUpdates
---

# Non-slash healthcheck command with punctuation should still be local-handled.

## Connections
- [[dot-test_healthcheck_word_with_punctuation_is_handled_locally()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestInboundPipelineOnGetUpdates
