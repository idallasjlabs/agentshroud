---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "PassthroughPipeline"
location: "L635"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PassthroughPipeline
---

# .test_collaborator_whoami_without_slash_uses_local_notice()

## Connections
- [[Collaborator plain 'whoami' should be treated as local command.]] - `rationale_for` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_19]] - `references` [EXTRACTED]
- [[fake_urlopen()_50]] - `contains` [EXTRACTED]
- [[fake_urlopen()_48]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/PassthroughPipeline
