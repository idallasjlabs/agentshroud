---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "PassthroughPipeline"
location: "L4707"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PassthroughPipeline
---

# .test_plain_model_question_is_handled_locally()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[Plain language model question should be answered by gateway directly.]] - `rationale_for` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_19]] - `references` [EXTRACTED]
- [[fake_urlopen()_69]] - `contains` [EXTRACTED]
- [[fake_urlopen()_48]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/PassthroughPipeline
