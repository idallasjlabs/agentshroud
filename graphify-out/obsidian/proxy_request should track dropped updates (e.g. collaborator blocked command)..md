---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "ingest_api/main.py"
location: "L320"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ingest_api/mainpy
---

# proxy_request should track dropped updates (e.g. collaborator blocked command).

## Connections
- [[.test_proxy_request_tracks_getupdates_stats_for_dropped_message()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ingest_api/mainpy