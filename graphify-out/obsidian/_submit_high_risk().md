---
source_file: "gateway/tests/test_mfa_guard.py"
type: "code"
community: "test_mfa_guard.py"
location: "L310"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_mfa_guardpy
---

# _submit_high_risk()

## Connections
- [[ApprovalQueue]] - `references` [EXTRACTED]
- [[ApprovalRequest_2]] - `calls` [EXTRACTED]
- [[test_decide_mfa_disabled_approves_without_code()]] - `calls` [EXTRACTED]
- [[test_decide_mfa_enabled_invalid_code_denied()]] - `calls` [EXTRACTED]
- [[test_decide_mfa_enabled_missing_code_denied()]] - `calls` [EXTRACTED]
- [[test_decide_mfa_enabled_replayed_code_denied()]] - `calls` [EXTRACTED]
- [[test_decide_mfa_enabled_valid_code_approves()]] - `calls` [EXTRACTED]
- [[test_decide_reject_never_requires_mfa()]] - `calls` [EXTRACTED]
- [[test_mfa_guard.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_mfa_guardpy