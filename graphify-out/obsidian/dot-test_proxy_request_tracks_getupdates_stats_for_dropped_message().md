---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "proxy_request should increment inbound getUpdates stats when messages pass…"
location: "L337"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/proxy_request_should_increment_inbound_getUpdates_stats_when_messages_pass
---

# .test_proxy_request_tracks_getupdates_stats_for_dropped_message()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_forward()_1]] - `contains` [EXTRACTED]
- [[fake_forward()_2]] - `indirect_call` [INFERRED]
- [[proxy_request should track dropped updates (e.g. collaborator blocked command).]] - `rationale_for` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/proxy_request_should_increment_inbound_getUpdates_stats_when_messages_pass
