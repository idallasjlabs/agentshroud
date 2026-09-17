---
source_file: "gateway/tests/test_email_owner_bypasses_pii.py"
type: "rationale"
community: "Approval Routing & Event Bus"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Approval_Routing__Event_Bus
---

# Owner-allowlist checked before PII sanitisation to avoid CVE/date-dense body collapse

## Connections
- [[email_send()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Approval_Routing__Event_Bus