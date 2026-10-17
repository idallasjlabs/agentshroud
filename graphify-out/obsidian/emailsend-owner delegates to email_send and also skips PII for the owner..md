---
source_file: "gateway/tests/test_email_owner_bypasses_pii.py"
type: "rationale"
community: "AsyncMock (3)"
location: "L84"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/AsyncMock_3
---

# /email/send-owner delegates to email_send and also skips PII for the owner.

## Connections
- [[dot-test_send_owner_endpoint_also_bypasses_pii()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/AsyncMock_3
