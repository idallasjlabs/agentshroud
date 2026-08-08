---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "code"
community: "PII Sanitizer Pipeline"
location: "L4777"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PII_Sanitizer_Pipeline
---

# TestOwnerActivityNotice

## Connections
- [[.test_activity_command_renders_entries()]] - `method` [EXTRACTED]
- [[.test_activity_command_reports_tracker_unhealthy()]] - `method` [EXTRACTED]
- [[CollaboratorActivityTracker]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[_send_owner_activity_notice must render tracker entries or honest error.]] - `rationale_for` [EXTRACTED]
- [[test_telegram_proxy_outbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PII_Sanitizer_Pipeline