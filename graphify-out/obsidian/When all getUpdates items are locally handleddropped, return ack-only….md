---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "proxy_request should increment inbound getUpdates stats when messages pass…"
location: "L312"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/proxy_request_should_increment_inbound_getUpdates_stats_when_messages_pass
---

# When all getUpdates items are locally handled/dropped, return ack-only…

## Connections
- [[dot-test_proxy_request_returns_ack_only_updates_when_all_dropped()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/proxy_request_should_increment_inbound_getUpdates_stats_when_messages_pass
