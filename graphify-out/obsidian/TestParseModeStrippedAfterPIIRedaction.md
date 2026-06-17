---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "code"
community: "Tool Result Sanitizer"
location: "L4320"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Tool_Result_Sanitizer
---

# TestParseModeStrippedAfterPIIRedaction

## Connections
- [[._make_owner_proxy()]] - `method` [EXTRACTED]
- [[.test_parse_mode_preserved_when_no_pii_detected()]] - `method` [EXTRACTED]
- [[.test_parse_mode_stripped_when_email_redacted_fallback_path()]] - `method` [EXTRACTED]
- [[.test_parse_mode_stripped_when_phone_redacted_fallback_path()]] - `method` [EXTRACTED]
- [[.test_parse_mode_stripped_when_pipeline_sanitizes_email()]] - `method` [EXTRACTED]
- [[CollaboratorActivityTracker]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[Regression tests for Telegram HTML parse error caused by PII placeholders.]] - `rationale_for` [EXTRACTED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[test_telegram_proxy_outbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Tool_Result_Sanitizer