---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Authentication & Rate Limiting"
location: "L3621"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Authentication__Rate_Limiting
---

# Rate-limit notice path should key retry window by user_id, not chat_id.

## Connections
- [[.test_collaborator_rate_limit_uses_user_id_when_chat_id_differs()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Authentication__Rate_Limiting
