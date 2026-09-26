---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "test_llm_proxy.py"
location: "L237"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_llm_proxypy
---

# If the pipeline crashes on a form payload, non-owner messages must be blocked.

## Connections
- [[.test_form_outbound_fails_closed_for_non_owner()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_llm_proxypy