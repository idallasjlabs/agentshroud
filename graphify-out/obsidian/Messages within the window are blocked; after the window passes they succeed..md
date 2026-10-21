---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: ".test_stranger_within_limit_triggers_approval_workflow()"
location: "L7867"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_stranger_within_limit_triggers_approval_workflow
---

# Messages within the window are blocked; after the window passes they succeed.

## Connections
- [[dot-test_collaborator_rate_limit_resets_after_window()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_stranger_within_limit_triggers_approval_workflow
