---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Collaborator URL web-access prompts should queue owner approval and return…"
location: "L2321"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Collaborator_URL_web-access_prompts_should_queue_owner_approval_and_return
---

# .test_collaborator_web_access_imperative_with_url_queues_owner_approval()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Imperative URL requests should queue owner approval and not expose command…]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_fake_approval()_1]] - `contains` [EXTRACTED]
- [[_fake_approval()_6]] - `indirect_call` [INFERRED]
- [[_fake_notify()]] - `contains` [EXTRACTED]
- [[_fake_notify()_1]] - `indirect_call` [INFERRED]
- [[_fake_send()]] - `contains` [EXTRACTED]
- [[_fake_send()_1]] - `indirect_call` [INFERRED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Collaborator_URL_web-access_prompts_should_queue_owner_approval_and_return
