---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: ".test_proxy_request_returns_ack_only_updates_when_all_dropped()"
location: "L291"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_proxy_request_returns_ack_only_updates_when_all_dropped
---

# .test_proxy_request_tracks_getupdates_stats_for_forwarded_message()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_forward()_2]] - `indirect_call` [INFERRED]
- [[proxy_request should increment inbound getUpdates stats when messages pass…]] - `rationale_for` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_proxy_request_returns_ack_only_updates_when_all_dropped
