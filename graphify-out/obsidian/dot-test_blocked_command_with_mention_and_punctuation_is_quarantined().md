---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "FakeRBAC"
location: "L1497"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/FakeRBAC
---

# .test_blocked_command_with_mention_and_punctuation_is_quarantined()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Mention + punctuation variants should still be blocked for collaborators.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/FakeRBAC
