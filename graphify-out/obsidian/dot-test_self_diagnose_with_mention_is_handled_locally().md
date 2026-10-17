---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "test_llm_proxy_local_parity.py"
location: "L5102"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxy_local_paritypy
---

# .test_self_diagnose_with_mention_is_handled_locally()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Mentioned self-diagnose variant should still route to local diagnostics…]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_urlopen()_45]] - `contains` [EXTRACTED]
- [[fake_urlopen()_20]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxy_local_paritypy
