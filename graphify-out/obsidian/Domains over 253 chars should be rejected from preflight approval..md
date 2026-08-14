---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Gateway Test Suite"
location: "L6335"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# Domains over 253 chars should be rejected from preflight approval.

## Connections
- [[.test_non_owner_overlong_fqdn_does_not_queue_egress_preflight()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Test_Suite