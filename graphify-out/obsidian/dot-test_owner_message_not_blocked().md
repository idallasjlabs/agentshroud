---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "GroupApprovalRouter"
location: "L220"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/GroupApprovalRouter
---

# .test_owner_message_not_blocked()

## Connections
- [[BlockingPipeline]] - `calls` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Owner messages must pass even if the pipeline would block them.]] - `rationale_for` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/GroupApprovalRouter
