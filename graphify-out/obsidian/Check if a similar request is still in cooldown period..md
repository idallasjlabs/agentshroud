---
source_file: "gateway/security/approval_hardening.py"
type: "rationale"
community: "Kill Switch Config"
location: "L345"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Kill_Switch_Config
---

# Check if a similar request is still in cooldown period.

## Connections
- [[.is_request_in_cooldown()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Kill_Switch_Config