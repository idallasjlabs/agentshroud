---
source_file: "gateway/security/egress_config.py"
type: "rationale"
community: "EgressFilterConfig"
location: "L327"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/EgressFilterConfig
---

# Public: does *domain* match any pattern in the effective default allowlist?

## Connections
- [[.matches_allowlist()]] - `rationale_for` [EXTRACTED]
- [[.matches_allowlist()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/EgressFilterConfig