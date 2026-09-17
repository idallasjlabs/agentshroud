---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Telegram Proxy Inbound Tests"
location: "L5192"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Telegram_Proxy_Inbound_Tests
---

# .test_self_diagnose_with_zero_width_char_is_handled_locally()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TelegramAPIProxy]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[Zero-width obfuscation should not bypass self-diagnose local handling.]] - `rationale_for` [EXTRACTED]
- [[_make_update()_1]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Telegram_Proxy_Inbound_Tests