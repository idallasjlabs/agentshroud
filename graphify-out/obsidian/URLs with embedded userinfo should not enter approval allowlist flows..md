---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "_wrap_response()"
location: "L6136"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_wrap_response
---

# URLs with embedded userinfo should not enter approval allowlist flows.

## Connections
- [[dot-test_non_owner_userinfo_url_does_not_queue_egress_preflight()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_wrap_response
