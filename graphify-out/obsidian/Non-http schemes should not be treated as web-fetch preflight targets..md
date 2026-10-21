---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "ApprovalQueueConfig (2)"
location: "L6032"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ApprovalQueueConfig_2
---

# Non-http schemes should not be treated as web-fetch preflight targets.

## Connections
- [[dot-test_non_owner_non_http_scheme_does_not_queue_egress_preflight()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ApprovalQueueConfig_2
