---
source_file: "gateway/tests/test_e2e_proxy.py"
type: "rationale"
community: "Middleware & Session Isolation"
location: "L475"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Middleware__Session_Isolation
---

# If the outbound pipeline crashes, the bot response must be withheld.

## Connections
- [[test_webhook_outbound_pipeline_crash_fails_closed()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Middleware__Session_Isolation