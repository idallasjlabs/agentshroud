---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "FakeRBAC"
location: "L6384"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/FakeRBAC
---

# Domains over 253 chars should be rejected from preflight approval.

## Connections
- [[dot-test_non_owner_overlong_fqdn_does_not_queue_egress_preflight()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/FakeRBAC
