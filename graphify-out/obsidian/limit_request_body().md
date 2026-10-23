---
source_file: "gateway/ingest_api/main.py"
type: "code"
community: "pick_latest_stable"
location: "L289"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/pick_latest_stable
---

# limit_request_body()

## Connections
- [[Reject request bodies larger than 1MB before parsing. Checks Content-Length…]] - `rationale_for` [EXTRACTED]
- [[Request_1]] - `references` [EXTRACTED]
- [[_body_stream()]] - `contains` [EXTRACTED]
- [[ingest_apimain.py]] - `contains` [EXTRACTED]
- [[middleware]] - `references` [EXTRACTED]
- [[test_limit_request_body_chunked_body_over_limit_rejected()]] - `calls` [EXTRACTED]
- [[test_limit_request_body_chunked_body_within_limit_passes_through()]] - `calls` [EXTRACTED]
- [[test_limit_request_body_client_disconnect_returns_clean_response()]] - `calls` [EXTRACTED]
- [[test_main_simple.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/pick_latest_stable
