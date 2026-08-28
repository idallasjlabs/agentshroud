---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "code"
community: "PII Sanitizer & E2E Tests"
location: "L4010"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PII_Sanitizer__E2E_Tests
---

# TestOutboundTextFieldResolution

## Connections
- [[.test_resolve_text_field_falls_back_to_first_string_when_all_empty()]] - `method` [EXTRACTED]
- [[.test_resolve_text_field_prefers_first_non_empty_field()]] - `method` [EXTRACTED]
- [[CollaboratorActivityTracker]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[Unit tests for outbound text field resolution helper behavior.]] - `rationale_for` [EXTRACTED]
- [[test_telegram_proxy_outbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PII_Sanitizer__E2E_Tests