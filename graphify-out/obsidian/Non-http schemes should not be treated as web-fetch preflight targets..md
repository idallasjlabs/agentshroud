---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "FakeRBAC"
location: "L6032"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/FakeRBAC
---

# Non-http schemes should not be treated as web-fetch preflight targets.

## Connections
- [[dot-test_non_owner_non_http_scheme_does_not_queue_egress_preflight()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/FakeRBAC
