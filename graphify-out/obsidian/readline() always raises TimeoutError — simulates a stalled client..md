---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "rationale"
community: "SessionManager"
location: "L69"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SessionManager
---

# readline() always raises TimeoutError — simulates a stalled client.

## Connections
- [[_TimeoutReader]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/SessionManager