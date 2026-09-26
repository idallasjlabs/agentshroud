---
source_file: "gateway/tests/test_redteam_probes.py"
type: "rationale"
community: "test_approval_queue.py"
location: "L151"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_approval_queuepy
---

# Probe 1.9: PII sanitizer must redact SSN on inbound messages.

## Connections
- [[test_ssn_redacted_inbound()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_approval_queuepy