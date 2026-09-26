---
source_file: "gateway/tests/test_mcp_policy_default_failclosed.py"
type: "rationale"
community: "test_e2e_proxy.py"
location: "L80"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_e2e_proxypy
---

# A stock config (no mcp_policy:) must produce a non-empty, deny-by-default policy

## Connections
- [[.test_missing_section_yields_deny_by_default_policy()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_e2e_proxypy