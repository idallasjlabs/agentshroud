---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Telegram Proxy Inbound Tests"
location: "L1556"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Telegram_Proxy_Inbound_Tests
---

# .test_blocked_command_with_fullwidth_chars_is_quarantined()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TelegramAPIProxy]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[Unicode fullwidth command variants should still be blocked for collaborators.]] - `rationale_for` [EXTRACTED]
- [[_make_update()_1]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Telegram_Proxy_Inbound_Tests