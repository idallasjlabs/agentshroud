---
source_file: "gateway/tests/test_e2e_proxy.py"
type: "rationale"
community: "HTTP Forwarder"
location: "L475"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/HTTP_Forwarder
---

# If the outbound pipeline crashes, the bot response must be withheld.

## Connections
- [[test_webhook_outbound_pipeline_crash_fails_closed()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/HTTP_Forwarder