---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "_wrap_response()"
location: "L9252"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_wrap_response
---

# /status in a group sends only the short liveness ack (no operational details).

## Connections
- [[.test_status_in_group_sends_short_ack_not_full_status()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_wrap_response