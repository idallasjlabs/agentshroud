---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Owner /approve should fail closed when target has no pending request."
location: "L1310"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Owner_/approve_should_fail_closed_when_target_has_no_pending_request
---

# Unknown non-owner user should trigger pending approval workflow and not forward.

## Connections
- [[dot-test_unknown_user_message_triggers_owner_approval_workflow()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Owner_/approve_should_fail_closed_when_target_has_no_pending_request
