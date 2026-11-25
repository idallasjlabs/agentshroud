---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "asyncio"
location: "L1447"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/asyncio
---

# .test_blocked_command_with_punctuation_is_quarantined()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[Punctuation-obfuscated blocked commands should still be quarantined.]] - `rationale_for` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_19]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/asyncio
