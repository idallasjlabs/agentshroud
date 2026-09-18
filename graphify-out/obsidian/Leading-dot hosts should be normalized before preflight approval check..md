---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "TelegramAPIProxy"
location: "L5944"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TelegramAPIProxy
---

# Leading-dot hosts should be normalized before preflight approval check.

## Connections
- [[.test_non_owner_malformed_url_normalizes_for_egress_preflight()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TelegramAPIProxy