---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "SecurityPipeline"
location: "L6924"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SecurityPipeline
---

# .test_notify_user_blocked_uses_owner_fallback_when_send_fails()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Owner block notice should retry with owner-specific fallback when first send…]] - `rationale_for` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_send()_12]] - `contains` [EXTRACTED]
- [[fake_send()_11]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/SecurityPipeline
