---
source_file: "gateway/tests/test_e2e_proxy.py"
type: "code"
community: "test_e2e_proxy.py"
location: "L442"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_e2e_proxypy
---

# test_webhook_outbound_block_withheld()

## Connections
- [[A pipeline-blocked outbound response must NOT be delivered. Regression test…]] - `rationale_for` [EXTRACTED]
- [[WebhookReceiver]] - `uses` [INFERRED]
- [[_PassInboundPipeline]] - `calls` [EXTRACTED]
- [[_StubForwarder]] - `calls` [EXTRACTED]
- [[asyncio_49]] - `references` [EXTRACTED]
- [[blocking_outbound()]] - `indirect_call` [INFERRED]
- [[test_e2e_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_e2e_proxypy
