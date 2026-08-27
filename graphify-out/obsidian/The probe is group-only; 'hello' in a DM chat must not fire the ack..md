---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Community 32"
location: "L9281"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_32
---

# The probe is group-only; 'hello' in a DM chat must not fire the ack.

## Connections
- [[.test_dm_hello_does_not_trigger_probe()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_32