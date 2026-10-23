---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "ApprovalQueueConfig (2)"
location: "L6523"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ApprovalQueueConfig_2
---

# .test_non_owner_email_only_text_does_not_queue_egress_preflight()

## Connections
- [[Email domains should not be mistaken for outbound web targets.]] - `rationale_for` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[check_async()_6]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ApprovalQueueConfig_2
