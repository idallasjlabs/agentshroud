---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "test_soc_bots.py"
location: "L8484"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_soc_botspy
---

# Immune user must not be dropped by the suspension path (stub must not appear).

## Connections
- [[.test_immune_user_message_passes_through_when_suspended()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_soc_botspy