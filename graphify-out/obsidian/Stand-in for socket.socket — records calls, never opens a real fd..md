---
source_file: "gateway/tests/test_soc_services_coverage.py"
type: "rationale"
community: "_patch_http_connection"
location: "L43"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_patch_http_connection
---

# Stand-in for socket.socket — records calls, never opens a real fd.

## Connections
- [[_FakeUnixSocket]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_patch_http_connection
