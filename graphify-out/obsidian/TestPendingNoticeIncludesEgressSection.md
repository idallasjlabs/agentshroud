---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "code"
community: "PII Sanitizer Pipeline"
location: "L4727"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PII_Sanitizer_Pipeline
---

# TestPendingNoticeIncludesEgressSection

## Connections
- [[.test_pending_includes_egress_entries()]] - `method` [EXTRACTED]
- [[CollaboratorActivityTracker]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[_send_owner_pending_notice must append Pending Egress Requests when queue non-em]] - `rationale_for` [EXTRACTED]
- [[test_telegram_proxy_outbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PII_Sanitizer_Pipeline