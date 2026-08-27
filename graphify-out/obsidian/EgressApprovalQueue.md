---
source_file: "gateway/security/egress_approval.py"
type: "code"
community: "Community 21"
location: "L109"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_21
---

# EgressApprovalQueue

## Connections
- [[.__init__()_74]] - `method` [EXTRACTED]
- [[._append_decision()]] - `method` [EXTRACTED]
- [[._assess_risk()]] - `method` [EXTRACTED]
- [[._check_existing_rule()]] - `method` [EXTRACTED]
- [[._load_rules()]] - `method` [EXTRACTED]
- [[._rule_to_dict()]] - `method` [EXTRACTED]
- [[._save_rules()]] - `method` [EXTRACTED]
- [[.add_rule()]] - `method` [EXTRACTED]
- [[.approval_queue()]] - `calls` [EXTRACTED]
- [[.approve()]] - `method` [EXTRACTED]
- [[.cleanup_expired()_2]] - `method` [EXTRACTED]
- [[.deny()]] - `method` [EXTRACTED]
- [[.get_all_rules()]] - `method` [EXTRACTED]
- [[.get_decision_log()]] - `method` [EXTRACTED]
- [[.get_emergency_status()]] - `method` [EXTRACTED]
- [[.get_pending_requests()]] - `method` [EXTRACTED]
- [[.get_rules_for_user()]] - `method` [EXTRACTED]
- [[.log_external_decision()]] - `method` [EXTRACTED]
- [[.mock_app_state()]] - `calls` [EXTRACTED]
- [[.preload_permanent_rules()]] - `method` [EXTRACTED]
- [[.remove_rule()]] - `method` [EXTRACTED]
- [[.request_approval()]] - `method` [EXTRACTED]
- [[.revoke_decision()]] - `method` [EXTRACTED]
- [[.set_emergency_block_all()]] - `method` [EXTRACTED]
- [[.set_event_bus()_1]] - `method` [EXTRACTED]
- [[DelegationManager]] - `semantically_similar_to` [INFERRED]
- [[EgressRule]] - `shares_data_with` [EXTRACTED]
- [[TelegramAPIProxy]] - `shares_data_with` [INFERRED]
- [[TestEgressApprovalAPI]] - `uses` [INFERRED]
- [[TestEgressApprovalQueue]] - `uses` [INFERRED]
- [[Thread-safe asyncio queue for managing egress approval requests.      Features]] - `rationale_for` [EXTRACTED]
- [[egress_approval.py]] - `contains` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_egress_approval.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_21