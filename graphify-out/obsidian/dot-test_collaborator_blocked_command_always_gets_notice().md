---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Every collaborator message must produce a response — never a silent drop."
location: "L7970"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Every_collaborator_message_must_produce_a_response__never_a_silent_drop
---

# .test_collaborator_blocked_command_always_gets_notice()

## Connections
- [[A blocked slash command must always produce a protected notice.]] - `rationale_for` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestNoResponseGuarantee]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_send()_23]] - `contains` [EXTRACTED]
- [[fake_send()_7]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Every_collaborator_message_must_produce_a_response__never_a_silent_drop
