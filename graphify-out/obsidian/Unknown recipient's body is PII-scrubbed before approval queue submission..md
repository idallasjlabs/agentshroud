---
source_file: "gateway/tests/test_email_owner_bypasses_pii.py"
type: "rationale"
community: "Email Owner Bypasses Pii"
location: "L114"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Email_Owner_Bypasses_Pii
---

# Unknown recipient's body is PII-scrubbed before approval queue submission.

## Connections
- [[.test_unknown_recipient_body_still_scrubbed()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Email_Owner_Bypasses_Pii