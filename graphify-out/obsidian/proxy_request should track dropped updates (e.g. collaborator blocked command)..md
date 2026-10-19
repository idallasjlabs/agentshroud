---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: ".test_proxy_request_returns_ack_only_updates_when_all_dropped()"
location: "L338"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_proxy_request_returns_ack_only_updates_when_all_dropped
---

# proxy_request should track dropped updates (e.g. collaborator blocked command).

## Connections
- [[dot-test_proxy_request_tracks_getupdates_stats_for_dropped_message()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_proxy_request_returns_ack_only_updates_when_all_dropped
