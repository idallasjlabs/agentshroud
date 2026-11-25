---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "PassthroughPipeline"
location: "L665"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PassthroughPipeline
---

# .test_owner_revoke_command_revokes_target_user()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Owner revoke should locally revoke collaborator access for the target user id.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_19]] - `references` [EXTRACTED]
- [[fake_urlopen()_65]] - `contains` [EXTRACTED]
- [[fake_urlopen()_48]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/PassthroughPipeline
