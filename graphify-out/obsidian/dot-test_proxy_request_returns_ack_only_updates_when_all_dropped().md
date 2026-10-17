---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "proxy_request should increment inbound getUpdates stats when messages pass…"
location: "L311"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/proxy_request_should_increment_inbound_getUpdates_stats_when_messages_pass
---

# .test_proxy_request_returns_ack_only_updates_when_all_dropped()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[When all getUpdates items are locally handleddropped, return ack-only…]] - `rationale_for` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_forward()]] - `contains` [EXTRACTED]
- [[fake_forward()_2]] - `indirect_call` [INFERRED]
- [[fake_start_notice()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/proxy_request_should_increment_inbound_getUpdates_stats_when_messages_pass
