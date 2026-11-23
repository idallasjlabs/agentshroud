---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "._make_proxy"
location: "L7970"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_make_proxy
---

# .test_collaborator_blocked_command_always_gets_notice()

## Connections
- [[A blocked slash command must always produce a protected notice.]] - `rationale_for` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestNoResponseGuarantee]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_21]] - `references` [EXTRACTED]
- [[fake_send()_15]] - `contains` [EXTRACTED]
- [[fake_send()_12]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/_make_proxy
