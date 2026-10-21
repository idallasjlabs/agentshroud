---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: ".test_stranger_within_limit_triggers_approval_workflow()"
location: "L7866"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_stranger_within_limit_triggers_approval_workflow
---

# .test_collaborator_rate_limit_resets_after_window()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Messages within the window are blocked; after the window passes they succeed.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestCollaboratorRateLimitRecovery]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_rl_notice()]] - `contains` [EXTRACTED]
- [[fake_rl_notice()_1]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_stranger_within_limit_triggers_approval_workflow
