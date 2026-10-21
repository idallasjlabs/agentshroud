---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "SlackSocketClient"
location: "L1931"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SlackSocketClient
---

# .test_collaborator_web_access_request_without_url_is_restricted_without_approval()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[Web access intent without explicit URL should remain restricted and not queue…]] - `rationale_for` [EXTRACTED]
- [[_fake_approval()_9]] - `contains` [EXTRACTED]
- [[_fake_approval()_6]] - `indirect_call` [INFERRED]
- [[_fake_notify()_3]] - `contains` [EXTRACTED]
- [[_fake_notify()_1]] - `indirect_call` [INFERRED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SlackSocketClient
