---
source_file: "gateway/tests/test_mcp_policy_default_failclosed.py"
type: "rationale"
community: "Egress Domain Allowlist"
location: "L100"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Egress_Domain_Allowlist
---

# A known/allowlisted server's non-high-risk tool is still ALLOWED — no breakage.

## Connections
- [[.test_engine_allows_known_server_under_default()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Egress_Domain_Allowlist