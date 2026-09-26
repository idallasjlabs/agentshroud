---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "test_soc_bots.py"
location: "L9281"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_soc_botspy
---

# The probe is group-only; 'hello' in a DM chat must not fire the ack.

## Connections
- [[.test_dm_hello_does_not_trigger_probe()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_soc_botspy