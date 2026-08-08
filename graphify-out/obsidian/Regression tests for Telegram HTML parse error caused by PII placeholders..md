---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L4321"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Regression tests for Telegram HTML parse error caused by PII placeholders.

## Connections
- [[TestParseModeStrippedAfterPIIRedaction]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline