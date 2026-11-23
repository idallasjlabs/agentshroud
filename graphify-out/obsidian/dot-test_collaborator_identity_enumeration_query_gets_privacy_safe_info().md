---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "fake_urlopen"
location: "L2236"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/fake_urlopen
---

# .test_collaborator_identity_enumeration_query_gets_privacy_safe_info()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Identity enumeration prompts should return privacy-safe guidance.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_21]] - `references` [EXTRACTED]
- [[fake_urlopen()_57]] - `contains` [EXTRACTED]
- [[fake_urlopen()_62]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/fake_urlopen
