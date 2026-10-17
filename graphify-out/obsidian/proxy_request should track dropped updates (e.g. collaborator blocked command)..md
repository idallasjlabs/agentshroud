---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "proxy_request should increment inbound getUpdates stats when messages pass…"
location: "L338"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/proxy_request_should_increment_inbound_getUpdates_stats_when_messages_pass
---

# proxy_request should track dropped updates (e.g. collaborator blocked command).

## Connections
- [[dot-test_proxy_request_tracks_getupdates_stats_for_dropped_message()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/proxy_request_should_increment_inbound_getUpdates_stats_when_messages_pass
