---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "BlockingPipeline"
location: "L220"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/BlockingPipeline
---

# .test_owner_message_not_blocked()

## Connections
- [[BlockingPipeline]] - `calls` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Owner messages must pass even if the pipeline would block them.]] - `rationale_for` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/BlockingPipeline
