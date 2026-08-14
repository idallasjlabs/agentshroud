---
source_file: "gateway/tests/test_mcp_policy.py"
type: "rationale"
community: "Egress Domain Allowlist"
location: "L105"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Egress_Domain_Allowlist
---

# An empty config denies everything — never a blanket allow.

## Connections
- [[test_default_deny_posture_when_no_config()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Egress_Domain_Allowlist