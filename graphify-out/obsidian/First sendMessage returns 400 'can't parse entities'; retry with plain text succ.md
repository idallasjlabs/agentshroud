---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "Tool Result Sanitizer & XML Injection Filtering"
location: "L4538"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Tool_Result_Sanitizer__XML_Injection_Filtering
---

# First sendMessage returns 400 'can't parse entities'; retry with plain text succ

## Connections
- [[dot-test_400_retry_succeeds_when_text_strippable()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Tool_Result_Sanitizer__XML_Injection_Filtering