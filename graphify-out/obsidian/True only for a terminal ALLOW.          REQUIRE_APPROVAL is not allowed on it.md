---
source_file: "gateway/security/mcp_policy.py"
type: "rationale"
community: "load_config()"
location: "L72"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/load_config
---

# True only for a terminal ALLOW.          REQUIRE_APPROVAL is *not* allowed on it

## Connections
- [[.allowed()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/load_config