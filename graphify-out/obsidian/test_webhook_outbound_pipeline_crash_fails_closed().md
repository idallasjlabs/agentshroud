---
source_file: "gateway/tests/test_e2e_proxy.py"
type: "code"
community: "Sidecar Security Scanner"
location: "L474"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Sidecar_Security_Scanner
---

# test_webhook_outbound_pipeline_crash_fails_closed()

## Connections
- [[If the outbound pipeline crashes, the bot response must be withheld.]] - `rationale_for` [EXTRACTED]
- [[WebhookReceiver]] - `calls` [EXTRACTED]
- [[_PassInboundPipeline]] - `calls` [EXTRACTED]
- [[_StubForwarder]] - `calls` [EXTRACTED]
- [[test_e2e_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Sidecar_Security_Scanner