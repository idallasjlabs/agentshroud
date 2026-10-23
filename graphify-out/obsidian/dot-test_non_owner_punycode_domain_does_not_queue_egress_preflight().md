---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "ApprovalQueueConfig (2)"
location: "L6418"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ApprovalQueueConfig_2
---

# .test_non_owner_punycode_domain_does_not_queue_egress_preflight()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[PunycodeIDN domains should not enter preflight approval queue.]] - `rationale_for` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[check_async()_21]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ApprovalQueueConfig_2
