---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "create_auth_dependency"
location: "L47"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/create_auth_dependency
---

# Fail any real urlopen fast unless a test installs its own fake. Blocked-message…

## Connections
- [[_no_real_telegram_network()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/create_auth_dependency
