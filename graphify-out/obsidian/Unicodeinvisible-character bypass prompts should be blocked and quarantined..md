---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: ".test_collaborator_allowlist_bypass_request_is_b"
location: "L4445"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_collaborator_allowlist_bypass_request_is_b
---

# Unicode/invisible-character bypass prompts should be blocked and quarantined.

## Connections
- [[.test_collaborator_path_traversal_request_is_blocked_and_quarantined()]] - `rationale_for` [EXTRACTED]
- [[.test_collaborator_unicode_bypass_request_is_blocked_and_quarantined()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_collaborator_allowlist_bypass_request_is_b