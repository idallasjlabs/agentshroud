---
source_file: "gateway/proxy/mcp_permissions.py"
type: "rationale"
community: "Enforce-Mode Auto-Revert"
location: "L626"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Enforce-Mode_Auto-Revert
---

# Run all permission checks in order. Returns first failure or final success.

## Connections
- [[.check_all()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Enforce-Mode_Auto-Revert