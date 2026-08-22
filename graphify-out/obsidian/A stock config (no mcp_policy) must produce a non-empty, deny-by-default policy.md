---
source_file: "gateway/tests/test_mcp_policy_default_failclosed.py"
type: "rationale"
community: "Mcp Policy"
location: "L80"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Mcp_Policy
---

# A stock config (no mcp_policy:) must produce a non-empty, deny-by-default policy

## Connections
- [[.test_missing_section_yields_deny_by_default_policy()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Mcp_Policy