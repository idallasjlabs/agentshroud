---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: ".test_proxy_request_returns_ack_only_updates_when_all_dropped()"
location: "L297"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/test_proxy_request_returns_ack_only_updates_when_all_dropped
---

# fake_forward()

## Connections
- [[dot-test_proxy_request_returns_ack_only_updates_when_all_dropped()]] - `indirect_call` [INFERRED]
- [[dot-test_proxy_request_tracks_getupdates_stats_for_dropped_message()]] - `indirect_call` [INFERRED]
- [[dot-test_proxy_request_tracks_getupdates_stats_for_forwarded_message()]] - `indirect_call` [INFERRED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/test_proxy_request_returns_ack_only_updates_when_all_dropped
