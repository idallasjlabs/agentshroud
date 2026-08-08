---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L4728"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# _send_owner_pending_notice must append Pending Egress Requests when queue non-em

## Connections
- [[TestPendingNoticeIncludesEgressSection]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline