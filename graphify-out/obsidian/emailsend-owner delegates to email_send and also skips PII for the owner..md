---
source_file: "gateway/tests/test_email_owner_bypasses_pii.py"
type: "rationale"
community: "Email Owner Bypasses Pii"
location: "L84"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Email_Owner_Bypasses_Pii
---

# /email/send-owner delegates to email_send and also skips PII for the owner.

## Connections
- [[.test_send_owner_endpoint_also_bypasses_pii()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Email_Owner_Bypasses_Pii