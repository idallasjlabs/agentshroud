---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "_wrap_response()"
location: "L6350"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_wrap_response
---

# Approval preflight should reject domains with non-alphabetic TLDs.

## Connections
- [[dot-test_non_owner_numeric_tld_does_not_queue_egress_preflight()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_wrap_response
