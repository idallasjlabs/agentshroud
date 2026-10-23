---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "TestInboundPipelineOnGetUpdates"
location: "L4921"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestInboundPipelineOnGetUpdates
---

# Unicode fullwidth healthcheck command should still route to local handler.

## Connections
- [[dot-test_healthcheck_with_fullwidth_chars_is_handled_locally()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestInboundPipelineOnGetUpdates
