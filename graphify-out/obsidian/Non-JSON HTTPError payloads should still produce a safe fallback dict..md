---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "scanner_integration.py"
location: "L3666"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scanner_integrationpy
---

# Non-JSON HTTPError payloads should still produce a safe fallback dict.

## Connections
- [[.test_forward_to_telegram_handles_http_error_non_json()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scanner_integrationpy