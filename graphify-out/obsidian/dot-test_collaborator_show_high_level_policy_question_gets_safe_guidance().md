---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "test_llm_proxy_local_parity.py"
location: "L3399"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxy_local_paritypy
---

# .test_collaborator_show_high_level_policy_question_gets_safe_guidance()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[High-level 'show' policy questions should be treated as conceptual safe-info…]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_urlopen()_19]] - `contains` [EXTRACTED]
- [[fake_urlopen()_20]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxy_local_paritypy
