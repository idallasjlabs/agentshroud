---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "TestInboundPipelineOnGetUpdates"
location: "L4954"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TestInboundPipelineOnGetUpdates
---

# .test_healthcheck_with_fullwidth_mention_and_punctuation_is_handled_locally()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Fullwidth + mentionpunctuation healthcheck variants should still route locally.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_urlopen()_27]] - `contains` [EXTRACTED]
- [[fake_urlopen()_19]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/TestInboundPipelineOnGetUpdates
