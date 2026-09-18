---
source_file: "gateway/tests/test_channel_ownership.py"
type: "rationale"
community: "TestEmailSend"
location: "L185"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestEmailSend
---

# Allowed (owner) recipient receives the body verbatim — PII scan is skipped.

## Connections
- [[.test_owner_body_not_redacted()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestEmailSend