---
source_file: "gateway/tests/test_soc_services_coverage.py"
type: "rationale"
community: "ServiceManager"
location: "L43"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ServiceManager
---

# Stand-in for socket.socket — records calls, never opens a real fd.

## Connections
- [[_FakeUnixSocket]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ServiceManager