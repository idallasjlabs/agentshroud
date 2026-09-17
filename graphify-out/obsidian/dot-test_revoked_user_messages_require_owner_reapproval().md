---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Telegram Proxy Inbound Tests"
location: "L1367"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Telegram_Proxy_Inbound_Tests
---

# .test_revoked_user_messages_require_owner_reapproval()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[Revoked users should be routed into owner re-approval workflow.]] - `rationale_for` [EXTRACTED]
- [[TelegramAPIProxy]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()_1]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Telegram_Proxy_Inbound_Tests