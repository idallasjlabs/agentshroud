---
source_file: "gateway/tests/test_email_owner_bypasses_pii.py"
type: "rationale"
community: "UserSessionManager (2) (2)"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/UserSessionManager_2_2
---

# Owner-allowlist checked before PII sanitisation to avoid CVE/date-dense body collapse

## Connections
- [[email_send()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/UserSessionManager_2_2
