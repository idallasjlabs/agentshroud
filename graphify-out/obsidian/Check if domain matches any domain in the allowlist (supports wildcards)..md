---
source_file: "gateway/security/egress_filter.py"
type: "rationale"
community: "EgressFilter"
location: "L420"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/EgressFilter
---

# Check if domain matches any domain in the allowlist (supports wildcards).

## Connections
- [[._matches_allowlist_domain()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/EgressFilter