---
source_file: "gateway/tests/test_token_validation.py"
type: "code"
community: "_make_token()"
location: "L114"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_make_token
---

# TestScopeEnforcement

## Connections
- [[.test_empty_scope_accepted_when_none_required()]] - `method` [EXTRACTED]
- [[.test_no_scope_claim_rejected_when_required()]] - `method` [EXTRACTED]
- [[.test_requested_scope_exceeds_granted()]] - `method` [EXTRACTED]
- [[.test_requested_scope_within_granted()]] - `method` [EXTRACTED]
- [[ScopeViolation]] - `uses` [INFERRED]
- [[test_token_validation.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_make_token