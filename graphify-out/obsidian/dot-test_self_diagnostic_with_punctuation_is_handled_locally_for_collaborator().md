---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "test_llm_proxy_local_parity.py"
location: "L5066"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxy_local_paritypy
---

# .test_self_diagnostic_with_punctuation_is_handled_locally_for_collaborator()

## Connections
- [[Collaborator self-diagnostic punctuation variant should still be local-handled.]] - `rationale_for` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_urlopen()_49]] - `contains` [EXTRACTED]
- [[fake_urlopen()_20]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxy_local_paritypy
