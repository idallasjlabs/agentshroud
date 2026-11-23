---
source_file: "gateway/ingest_api/routes/dashboard.py"
type: "code"
community: "ingest_api/main.py"
location: "L606"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ingest_api/mainpy
---

# egress_websocket()

## Connections
- [[WebSocket stream specialized for egresssecurity dashboard updates.]] - `rationale_for` [EXTRACTED]
- [[_build_egress_live_snapshot()]] - `calls` [EXTRACTED]
- [[_validate_ws_token()]] - `calls` [EXTRACTED]
- [[dashboard.py]] - `contains` [EXTRACTED]
- [[make_event()]] - `calls` [EXTRACTED]
- [[on_event()_1]] - `contains` [EXTRACTED]
- [[on_event()]] - `indirect_call` [INFERRED]
- [[websocket_8]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ingest_api/mainpy
