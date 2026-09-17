---
source_file: "gateway/tests/test_mcp_policy_default_failclosed.py"
type: "rationale"
community: "load_config()"
location: "L80"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/load_config
---

# A stock config (no mcp_policy:) must produce a non-empty, deny-by-default policy

## Connections
- [[.test_missing_section_yields_deny_by_default_policy()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/load_config