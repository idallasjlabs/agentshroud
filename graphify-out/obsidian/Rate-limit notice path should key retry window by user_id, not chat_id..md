---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Gateway Test Suite"
location: "L3690"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# Rate-limit notice path should key retry window by user_id, not chat_id.

## Connections
- [[.test_collaborator_rate_limit_uses_user_id_when_chat_id_differs()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Test_Suite