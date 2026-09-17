---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "TestNoResponseGuarantee"
location: "L7845"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestNoResponseGuarantee
---

# After the rate-limit window expires, collaborator messages go through normally.

## Connections
- [[TestCollaboratorRateLimitRecovery]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestNoResponseGuarantee