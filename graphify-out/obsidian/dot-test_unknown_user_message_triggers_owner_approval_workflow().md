---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Telegram Proxy Inbound Tests"
location: "L1291"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Telegram_Proxy_Inbound_Tests
---

# .test_unknown_user_message_triggers_owner_approval_workflow()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TelegramAPIProxy]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[Unknown non-owner user should trigger pending approval workflow and not forward.]] - `rationale_for` [EXTRACTED]
- [[_make_update()_1]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Telegram_Proxy_Inbound_Tests