---
source_file: "gateway/security/egress_approval.py"
type: "code"
community: "Community 88"
location: "L109"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_88
---

# EgressApprovalQueue

## Connections
- [[dot-__init__()_191]] - `method` [EXTRACTED]
- [[dot-_append_decision()]] - `method` [EXTRACTED]
- [[dot-_assess_risk()]] - `method` [EXTRACTED]
- [[dot-_check_existing_rule()]] - `method` [EXTRACTED]
- [[dot-_load_rules()]] - `method` [EXTRACTED]
- [[dot-_rule_to_dict()]] - `method` [EXTRACTED]
- [[dot-_save_rules()]] - `method` [EXTRACTED]
- [[dot-add_rule()]] - `method` [EXTRACTED]
- [[dot-approval_queue()]] - `calls` [EXTRACTED]
- [[dot-approve()]] - `method` [EXTRACTED]
- [[dot-cleanup_expired()_3]] - `method` [EXTRACTED]
- [[dot-deny()]] - `method` [EXTRACTED]
- [[dot-get_all_rules()]] - `method` [EXTRACTED]
- [[dot-get_decision_log()]] - `method` [EXTRACTED]
- [[dot-get_emergency_status()]] - `method` [EXTRACTED]
- [[dot-get_pending_requests()]] - `method` [EXTRACTED]
- [[dot-get_rules_for_user()]] - `method` [EXTRACTED]
- [[dot-log_external_decision()]] - `method` [EXTRACTED]
- [[dot-mock_app_state()]] - `calls` [EXTRACTED]
- [[dot-preload_permanent_rules()]] - `method` [EXTRACTED]
- [[dot-remove_rule()]] - `method` [EXTRACTED]
- [[dot-request_approval()]] - `method` [EXTRACTED]
- [[dot-revoke_decision()]] - `method` [EXTRACTED]
- [[dot-set_emergency_block_all()]] - `method` [EXTRACTED]
- [[dot-set_event_bus()_2]] - `method` [EXTRACTED]
- [[DelegationManager_1]] - `semantically_similar_to` [INFERRED]
- [[EgressRule]] - `shares_data_with` [EXTRACTED]
- [[TelegramAPIProxy_2]] - `shares_data_with` [INFERRED]
- [[TestEgressApprovalAPI]] - `uses` [INFERRED]
- [[TestEgressApprovalQueue]] - `uses` [INFERRED]
- [[Thread-safe asyncio queue for managing egress approval requests.      Features]] - `rationale_for` [EXTRACTED]
- [[egress_approval.py]] - `contains` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_egress_approval.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_88