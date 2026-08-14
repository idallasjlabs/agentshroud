---
source_file: "gateway/tests/test_mfa_guard.py"
type: "code"
community: "Enforce-Mode Auto-Revert"
location: "L310"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Enforce-Mode_Auto-Revert
---

# _submit_high_risk()

## Connections
- [[ApprovalQueue_1]] - `references` [EXTRACTED]
- [[ApprovalRequest_3]] - `calls` [EXTRACTED]
- [[test_decide_mfa_disabled_approves_without_code()]] - `calls` [EXTRACTED]
- [[test_decide_mfa_enabled_invalid_code_denied()]] - `calls` [EXTRACTED]
- [[test_decide_mfa_enabled_missing_code_denied()]] - `calls` [EXTRACTED]
- [[test_decide_mfa_enabled_replayed_code_denied()]] - `calls` [EXTRACTED]
- [[test_decide_mfa_enabled_valid_code_approves()]] - `calls` [EXTRACTED]
- [[test_decide_reject_never_requires_mfa()]] - `calls` [EXTRACTED]
- [[test_mfa_guard.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Enforce-Mode_Auto-Revert