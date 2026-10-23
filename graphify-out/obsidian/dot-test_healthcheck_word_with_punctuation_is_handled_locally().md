---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: ".test_healthcheck_word_with_punctuation_is_handled_locally()"
location: "L4852"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_healthcheck_word_with_punctuation_is_handled_locally
---

# .test_healthcheck_word_with_punctuation_is_handled_locally()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Non-slash healthcheck command with punctuation should still be local-handled.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_urlopen()_58]] - `contains` [EXTRACTED]
- [[fake_urlopen()_19]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_healthcheck_word_with_punctuation_is_handled_locally
