---
source_file: "gateway/tests/test_email_owner_bypasses_pii.py"
type: "rationale"
community: "Forward (routes)"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Forward_routes
---

# Owner-allowlist checked before PII sanitisation to avoid CVE/date-dense body collapse

## Connections
- [[email_send()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Forward_routes