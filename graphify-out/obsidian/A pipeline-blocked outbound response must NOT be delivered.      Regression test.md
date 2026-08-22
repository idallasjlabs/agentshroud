---
source_file: "gateway/tests/test_e2e_proxy.py"
type: "rationale"
community: "Middleware & Session Isolation"
location: "L443"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Middleware__Session_Isolation
---

# A pipeline-blocked outbound response must NOT be delivered.      Regression test

## Connections
- [[test_webhook_outbound_block_withheld()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Middleware__Session_Isolation