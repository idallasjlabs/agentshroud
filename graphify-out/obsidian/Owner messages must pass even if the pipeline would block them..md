---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Authentication & Rate Limiting"
location: "L203"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Authentication__Rate_Limiting
---

# Owner messages must pass even if the pipeline would block them.

## Connections
- [[.test_owner_message_not_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Authentication__Rate_Limiting