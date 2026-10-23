---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "ApprovalQueueConfig (2)"
location: "L6314"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ApprovalQueueConfig_2
---

# .test_non_owner_overlong_url_does_not_queue_egress_preflight()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Overly long URLs should be rejected from preflight approval path.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[check_async()_18]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ApprovalQueueConfig_2
