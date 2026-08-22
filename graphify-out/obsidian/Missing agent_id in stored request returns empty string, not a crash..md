---
source_file: "gateway/tests/test_egress_telegram_notify.py"
type: "rationale"
community: "Egress Telegram Notify"
location: "L254"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Egress_Telegram_Notify
---

# Missing agent_id in stored request returns empty string, not a crash.

## Connections
- [[.test_handle_callback_missing_agent_id_safe()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Egress_Telegram_Notify