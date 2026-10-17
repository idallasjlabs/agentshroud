---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Owner /approve should fail closed when target has no pending request."
location: "L1320"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Owner_/approve_should_fail_closed_when_target_has_no_pending_request
---

# fake_pending_notice()

## Connections
- [[dot-test_revoked_user_messages_require_owner_reapproval()]] - `indirect_call` [INFERRED]
- [[dot-test_stranger_within_limit_triggers_approval_workflow()]] - `indirect_call` [INFERRED]
- [[dot-test_unknown_user_message_triggers_owner_approval_workflow()]] - `indirect_call` [INFERRED]
- [[dot-test_unknown_user_repeated_start_still_gets_pending_notice()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/INFERRED #community/Owner_/approve_should_fail_closed_when_target_has_no_pending_request
