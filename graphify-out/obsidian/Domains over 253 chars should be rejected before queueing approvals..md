---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "Gateway Test Suite"
location: "L3450"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# Domains over 253 chars should be rejected before queueing approvals.

## Connections
- [[.test_raw_web_fetch_json_overlong_fqdn_does_not_queue_approval()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Test_Suite