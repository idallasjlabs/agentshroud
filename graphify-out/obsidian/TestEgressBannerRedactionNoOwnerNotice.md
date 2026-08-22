---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "code"
community: "Security Audit & Watchtower Tests"
location: "L4712"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Security_Audit__Watchtower_Tests
---

# TestEgressBannerRedactionNoOwnerNotice

## Connections
- [[.test_redaction_silent_no_owner_notice()]] - `method` [EXTRACTED]
- [[CollaboratorActivityTracker]] - `uses` [INFERRED]
- [[Outbound filter must redact egress banners but NOT call _send_owner_admin_notice]] - `rationale_for` [EXTRACTED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[test_telegram_proxy_outbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Security_Audit__Watchtower_Tests