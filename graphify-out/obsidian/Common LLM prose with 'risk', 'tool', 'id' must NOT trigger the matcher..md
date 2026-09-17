---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "Tool Result Sanitizer & XML Injection Filtering"
location: "L4681"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Tool_Result_Sanitizer__XML_Injection_Filtering
---

# Common LLM prose with 'risk:', 'tool:', 'id:' must NOT trigger the matcher.

## Connections
- [[dot-test_no_false_positive_on_generic_llm_response()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Tool_Result_Sanitizer__XML_Injection_Filtering