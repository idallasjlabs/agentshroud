---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Telegram Proxy Inbound"
location: "L4203"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Proxy_Inbound
---

# Collaborator requests to message other users should be blocked/quarantined.

## Connections
- [[.test_collaborator_cross_user_messaging_request_is_blocked_and_quarantined()]] - `rationale_for` [EXTRACTED]
- [[.test_collaborator_scheduler_autorun_request_is_blocked_and_quarantined()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Proxy_Inbound