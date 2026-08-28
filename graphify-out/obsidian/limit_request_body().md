---
source_file: "gateway/ingest_api/main.py"
type: "code"
community: "Ingest API & Approval Routes"
location: "L275"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Ingest_API__Approval_Routes
---

# limit_request_body()

## Connections
- [[JSONResponse]] - `calls` [EXTRACTED]
- [[Reject request bodies larger than 1MB before parsing.      Checks Content-Length]] - `rationale_for` [EXTRACTED]
- [[Request_2]] - `references` [EXTRACTED]
- [[main.py_2]] - `contains` [EXTRACTED]
- [[test_limit_request_body_chunked_body_over_limit_rejected()]] - `calls` [EXTRACTED]
- [[test_limit_request_body_chunked_body_within_limit_passes_through()]] - `calls` [EXTRACTED]
- [[test_limit_request_body_client_disconnect_returns_clean_response()]] - `calls` [EXTRACTED]
- [[test_main_simple.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Ingest_API__Approval_Routes