---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "FakeRBAC"
location: "L373"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/FakeRBAC
---

# .test_start_resets_multi_turn_tracker_for_collaborator()

## Connections
- [[Collaborator start should reset blocked multi-turn tracker session.]] - `rationale_for` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[reset_session()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/FakeRBAC
