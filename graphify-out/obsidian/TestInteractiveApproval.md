---
source_file: "gateway/tests/test_egress_filter.py"
type: "code"
community: "Egress Filter & Approval"
location: "L270"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Egress_Filter__Approval
---

# TestInteractiveApproval

## Connections
- [[.test_allowlisted_domain_still_prompts_when_approval_all_enabled()]] - `method` [EXTRACTED]
- [[.test_emits_egress_event_to_event_bus()]] - `method` [EXTRACTED]
- [[.test_unknown_domain_allowed_when_approved()]] - `method` [EXTRACTED]
- [[.test_unknown_domain_denied_when_denied()]] - `method` [EXTRACTED]
- [[ApprovalResult]] - `uses` [INFERRED]
- [[EgressAction]] - `uses` [INFERRED]
- [[EgressAttempt]] - `uses` [INFERRED]
- [[EgressFilter_1]] - `uses` [INFERRED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[Interactive egress approval flow (allow once  deny).]] - `rationale_for` [EXTRACTED]
- [[test_egress_filter.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Egress_Filter__Approval
