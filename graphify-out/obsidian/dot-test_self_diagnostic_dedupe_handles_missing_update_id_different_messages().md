---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "TestInboundPipelineOnGetUpdates"
location: "L5439"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TestInboundPipelineOnGetUpdates
---

# .test_self_diagnostic_dedupe_handles_missing_update_id_different_messages()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[When update_id is missing, different message_id values should not dedupe…]] - `rationale_for` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_urlopen()_49]] - `contains` [EXTRACTED]
- [[fake_urlopen()_19]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/TestInboundPipelineOnGetUpdates
