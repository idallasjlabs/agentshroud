---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "SecurityPipeline"
location: "L8605"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SecurityPipeline
---

# _quarantine_blocked_message must NOT increment lockdown count for immune users.

## Connections
- [[dot-test_immune_user_lockdown_not_incremented()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/SecurityPipeline
