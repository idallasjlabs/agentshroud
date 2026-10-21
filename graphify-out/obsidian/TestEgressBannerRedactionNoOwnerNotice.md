---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "code"
community: "test_collaborator_tracker.py"
location: "L4712"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/test_collaborator_trackerpy
---

# TestEgressBannerRedactionNoOwnerNotice

## Connections
- [[dot-test_redaction_silent_no_owner_notice()]] - `method` [EXTRACTED]
- [[CollaboratorActivityTracker]] - `uses` [INFERRED]
- [[Outbound filter must redact egress banners but NOT call _send_owner_admin_notice]] - `rationale_for` [EXTRACTED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer_2]] - `uses` [INFERRED]
- [[TelegramAPIProxy_2]] - `uses` [INFERRED]
- [[test_telegram_proxy_outbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/test_collaborator_trackerpy
