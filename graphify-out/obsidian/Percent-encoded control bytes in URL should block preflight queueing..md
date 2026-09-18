---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "TelegramAPIProxy"
location: "L6154"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TelegramAPIProxy
---

# Percent-encoded control bytes in URL should block preflight queueing.

## Connections
- [[.test_non_owner_percent_encoded_control_url_does_not_queue_egress_preflight()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TelegramAPIProxy