---
source_file: "gateway/security/mcp_policy.py"
type: "rationale"
community: "Egress Domain Allowlist"
location: "L72"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Egress_Domain_Allowlist
---

# True only for a terminal ALLOW.          REQUIRE_APPROVAL is *not* allowed on it

## Connections
- [[.allowed()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Egress_Domain_Allowlist