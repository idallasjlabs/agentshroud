---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "FakeRBAC"
location: "L605"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/FakeRBAC
---

# .test_owner_whoami_with_bot_mention_uses_local_notice()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Owner whoami@bot should be normalized and handled locally.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_21]] - `references` [EXTRACTED]
- [[fake_urlopen()_14]] - `contains` [EXTRACTED]
- [[fake_urlopen()_62]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/FakeRBAC
