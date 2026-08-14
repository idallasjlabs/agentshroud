---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "code"
community: "Gateway Test Suite"
location: "L4712"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Gateway_Test_Suite
---

# TestEgressBannerRedactionNoOwnerNotice

## Connections
- [[.test_redaction_silent_no_owner_notice()]] - `method` [EXTRACTED]
- [[CollaboratorActivityTracker]] - `uses` [INFERRED]
- [[Outbound filter must redact egress banners but NOT call _send_owner_admin_notice]] - `rationale_for` [EXTRACTED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[egress_deny_ callback token must match.]] - `rationale_for` [EXTRACTED]
- [[test_telegram_proxy_outbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Gateway_Test_Suite