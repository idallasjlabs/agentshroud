---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "ApprovalQueueConfig (2)"
location: "L3399"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ApprovalQueueConfig_2
---

# .test_collaborator_show_high_level_policy_question_gets_safe_guidance()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[High-level 'show' policy questions should be treated as conceptual safe-info…]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_urlopen()_69]] - `contains` [EXTRACTED]
- [[fake_urlopen()_19]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/ApprovalQueueConfig_2
