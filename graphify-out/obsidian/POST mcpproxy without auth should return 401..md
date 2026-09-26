---
source_file: "gateway/tests/test_mcp_proxy_endpoint.py"
type: "rationale"
community: "Safe Refactor Specialist"
location: "L77"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Safe_Refactor_Specialist
---

# POST /mcp/proxy without auth should return 401.

## Connections
- [[.test_requires_auth()_3]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Safe_Refactor_Specialist