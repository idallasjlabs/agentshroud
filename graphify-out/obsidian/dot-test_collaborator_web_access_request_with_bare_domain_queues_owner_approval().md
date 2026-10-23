---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "SlackSocketClient"
location: "L1976"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SlackSocketClient
---

# .test_collaborator_web_access_request_with_bare_domain_queues_owner_approval()

## Connections
- [[Domain-only web intent should queue owner approval and pending notice.]] - `rationale_for` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_fake_approval()_8]] - `contains` [EXTRACTED]
- [[_fake_approval()_6]] - `indirect_call` [INFERRED]
- [[_fake_notify()_2]] - `contains` [EXTRACTED]
- [[_fake_notify()_1]] - `indirect_call` [INFERRED]
- [[_fake_send()_14]] - `contains` [EXTRACTED]
- [[_fake_send()_13]] - `indirect_call` [INFERRED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SlackSocketClient
