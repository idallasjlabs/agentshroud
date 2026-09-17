---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Telegram Proxy Inbound Tests"
location: "L6539"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Telegram_Proxy_Inbound_Tests
---

# .test_non_owner_ip_url_does_not_queue_egress_preflight()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Literal IP URL targets should not enter domain approval preflight.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TelegramAPIProxy]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()_1]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Telegram_Proxy_Inbound_Tests