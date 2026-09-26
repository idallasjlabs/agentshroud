---
source_file: "gateway/security/egress_filter.py"
type: "rationale"
community: "Production Safety Checklist (SKILL)"
location: "L607"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Production_Safety_Checklist_SKILL
---

# Send pending egress notifications via Telegram. Called from request handler.

## Connections
- [[.flush_notifications()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Production_Safety_Checklist_SKILL