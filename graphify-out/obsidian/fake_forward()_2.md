---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "proxy_request should increment inbound getUpdates stats when messages pass…"
location: "L297"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/proxy_request_should_increment_inbound_getUpdates_stats_when_messages_pass
---

# fake_forward()

## Connections
- [[dot-test_proxy_request_returns_ack_only_updates_when_all_dropped()]] - `indirect_call` [INFERRED]
- [[dot-test_proxy_request_tracks_getupdates_stats_for_dropped_message()]] - `indirect_call` [INFERRED]
- [[dot-test_proxy_request_tracks_getupdates_stats_for_forwarded_message()]] - `indirect_call` [INFERRED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/proxy_request_should_increment_inbound_getUpdates_stats_when_messages_pass
