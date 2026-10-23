---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "ApprovalQueueConfig (2)"
location: "L725"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ApprovalQueueConfig_2
---

# .test_owner_revoke_command_requires_target_user_id()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Owner revoke without target should return usage guidance.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_urlopen()_73]] - `contains` [EXTRACTED]
- [[fake_urlopen()_19]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/ApprovalQueueConfig_2
