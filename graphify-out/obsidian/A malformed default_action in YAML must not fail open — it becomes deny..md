---
source_file: "gateway/tests/test_mcp_policy.py"
type: "rationale"
community: "Community 33"
location: "L197"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_33
---

# A malformed default_action in YAML must not fail open — it becomes deny.

## Connections
- [[test_invalid_default_action_falls_back_to_deny()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_33