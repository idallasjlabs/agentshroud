---
source_file: "gateway/tests/test_redteam_probes.py"
type: "rationale"
community: "test_approval_queue.py"
location: "L170"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_approval_queuepy
---

# Probe 1.9c: PII sanitizer must redact credit card numbers.

## Connections
- [[test_credit_card_redacted_inbound()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_approval_queuepy