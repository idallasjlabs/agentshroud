---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "test_a2a_proxy.py"
location: "L7928"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_a2a_proxypy
---

# Every collaborator message must produce a response — never a silent drop.

## Connections
- [[TestNoResponseGuarantee]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_a2a_proxypy