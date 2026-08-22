---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "code"
community: "Security Audit & Watchtower Tests"
location: "L4739"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Security_Audit__Watchtower_Tests
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

#graphify/code #graphify/INFERRED #community/Security_Audit__Watchtower_Tests