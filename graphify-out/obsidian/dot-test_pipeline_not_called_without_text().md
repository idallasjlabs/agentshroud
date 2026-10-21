---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "GroupApprovalRouter"
location: "L242"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/GroupApprovalRouter
---

# .test_pipeline_not_called_without_text()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[Updates without text (e.g. photos) should skip the pipeline.]] - `rationale_for` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[process_inbound()_1]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/GroupApprovalRouter
