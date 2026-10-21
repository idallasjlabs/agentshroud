---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "GroupApprovalRouter"
location: "L173"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/GroupApprovalRouter
---

# .test_prompt_injection_blocked_on_getUpdates()

## Connections
- [[BlockingPipeline]] - `calls` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Prompt injection via getUpdates must be blocked by the pipeline.]] - `rationale_for` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/GroupApprovalRouter
