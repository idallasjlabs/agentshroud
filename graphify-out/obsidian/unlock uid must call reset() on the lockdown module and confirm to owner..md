---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "test_soc_bots.py"
location: "L8090"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_soc_botspy
---

# /unlock <uid> must call reset() on the lockdown module and confirm to owner.

## Connections
- [[.test_unlock_calls_reset_on_lockdown()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_soc_botspy