---
source_file: "gateway/tests/test_email_owner_bypasses_pii.py"
type: "rationale"
community: "Module Group 74"
location: "L84"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Module_Group_74
---

# /email/send-owner delegates to email_send and also skips PII for the owner.

## Connections
- [[.test_send_owner_endpoint_also_bypasses_pii()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Module_Group_74
