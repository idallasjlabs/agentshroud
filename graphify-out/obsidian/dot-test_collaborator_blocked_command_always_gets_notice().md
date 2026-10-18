---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: ".test_unknown_user_always_gets_pending_or_rate_limit_notice()"
location: "L7970"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_unknown_user_always_gets_pending_or_rate_limit_notice
---

# .test_collaborator_blocked_command_always_gets_notice()

## Connections
- [[A blocked slash command must always produce a protected notice.]] - `rationale_for` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestNoResponseGuarantee]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_send()_23]] - `contains` [EXTRACTED]
- [[fake_send()_11]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_unknown_user_always_gets_pending_or_rate_limit_notice
