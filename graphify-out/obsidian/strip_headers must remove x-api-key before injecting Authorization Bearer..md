---
source_file: "gateway/tests/test_credential_injector.py"
type: "rationale"
community: "tailscale-check.sh"
location: "L90"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/tailscale-checksh
---

# strip_headers must remove x-api-key before injecting Authorization: Bearer.

## Connections
- [[.test_strip_headers_removes_conflicting_header()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/tailscale-checksh