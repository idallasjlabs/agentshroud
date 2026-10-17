---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Collaborator URL web-access prompts should queue owner approval and return…"
location: "L2080"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Collaborator_URL_web-access_prompts_should_queue_owner_approval_and_return
---

# .test_collaborator_web_access_policy_question_with_url_does_not_queue_preflight()

## Connections
- [[Conceptual policy questions that mention a URL should not be treated as fetch…]] - `rationale_for` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_fake_approval()_4]] - `contains` [EXTRACTED]
- [[_fake_approval()_6]] - `indirect_call` [INFERRED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_urlopen()_57]] - `contains` [EXTRACTED]
- [[fake_urlopen()_20]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Collaborator_URL_web-access_prompts_should_queue_owner_approval_and_return
