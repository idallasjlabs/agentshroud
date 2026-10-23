---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "ApprovalQueueConfig (2)"
location: "L6557"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ApprovalQueueConfig_2
---

# .test_non_owner_ip_url_does_not_queue_egress_preflight()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Literal IP URL targets should not enter domain approval preflight.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[check_async()_8]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ApprovalQueueConfig_2
