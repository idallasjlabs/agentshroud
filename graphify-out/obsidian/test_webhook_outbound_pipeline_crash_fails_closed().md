---
source_file: "gateway/tests/test_e2e_proxy.py"
type: "code"
community: "Middleware & Session Isolation"
location: "L474"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Middleware__Session_Isolation
---

# test_webhook_outbound_pipeline_crash_fails_closed()

## Connections
- [[If the outbound pipeline crashes, the bot response must be withheld.]] - `rationale_for` [EXTRACTED]
- [[WebhookReceiver]] - `calls` [EXTRACTED]
- [[_PassInboundPipeline]] - `calls` [EXTRACTED]
- [[_StubForwarder_2]] - `calls` [EXTRACTED]
- [[test_e2e_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Middleware__Session_Isolation