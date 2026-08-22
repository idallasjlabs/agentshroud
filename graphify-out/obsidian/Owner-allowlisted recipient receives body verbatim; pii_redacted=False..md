---
source_file: "gateway/tests/test_email_owner_bypasses_pii.py"
type: "rationale"
community: "Email Owner Bypasses Pii"
location: "L45"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Email_Owner_Bypasses_Pii
---

# Owner-allowlisted recipient receives body verbatim; pii_redacted=False.

## Connections
- [[.test_owner_recipient_body_preserved()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Email_Owner_Bypasses_Pii