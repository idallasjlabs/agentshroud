---
source_file: "gateway/tests/test_mcp_proxy_endpoint.py"
type: "rationale"
community: "scripts/sync-llm-settings.sh"
location: "L77"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/sync-llm-settingssh
---

# POST /mcp/proxy without auth should return 401.

## Connections
- [[.test_requires_auth()_3]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/sync-llm-settingssh