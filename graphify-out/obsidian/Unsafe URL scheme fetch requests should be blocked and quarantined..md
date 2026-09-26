---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "ota.c"
location: "L4383"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/otac
---

# Unsafe URL scheme fetch requests should be blocked and quarantined.

## Connections
- [[.test_collaborator_allowlist_bypass_request_is_blocked_and_quarantined()]] - `rationale_for` [EXTRACTED]
- [[.test_collaborator_unsafe_scheme_request_is_blocked_and_quarantined()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/otac