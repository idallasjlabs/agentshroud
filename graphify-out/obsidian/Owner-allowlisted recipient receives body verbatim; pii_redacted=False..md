---
source_file: "gateway/tests/test_email_owner_bypasses_pii.py"
type: "rationale"
community: "TestPatternDetection"
location: "L45"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestPatternDetection
---

# Owner-allowlisted recipient receives body verbatim; pii_redacted=False.

## Connections
- [[dot-test_owner_recipient_body_preserved()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestPatternDetection
