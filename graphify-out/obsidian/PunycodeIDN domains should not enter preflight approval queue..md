---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "ingest_api/main.py"
location: "L6401"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ingest_api/mainpy
---

# Punycode/IDN domains should not enter preflight approval queue.

## Connections
- [[.test_non_owner_punycode_domain_does_not_queue_egress_preflight()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ingest_api/mainpy