---
source_file: "gateway/approval_queue/group_router.py"
type: "code"
community: "Group Approval Routing"
location: "L37"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Group_Approval_Routing
---

# GroupApprovalRouter

## Connections
- [[.__init__()_4]] - `method` [EXTRACTED]
- [[._build_group_reply_text()]] - `method` [EXTRACTED]
- [[._build_owner_dm_text()]] - `method` [EXTRACTED]
- [[._default_send()]] - `method` [EXTRACTED]
- [[.extract_group_chat_id()]] - `method` [EXTRACTED]
- [[.is_group_context()]] - `method` [EXTRACTED]
- [[.route_approval()]] - `method` [EXTRACTED]
- [[.test_extract_chat_id_from_group_agent_id()]] - `calls` [EXTRACTED]
- [[.test_extract_chat_id_returns_none_for_non_group()]] - `calls` [EXTRACTED]
- [[.test_is_group_context_false_for_collab_agent_id()]] - `calls` [EXTRACTED]
- [[.test_is_group_context_false_for_default()]] - `calls` [EXTRACTED]
- [[.test_is_group_context_true_for_group_agent_id()]] - `calls` [EXTRACTED]
- [[.test_router_works_without_send_fn()]] - `calls` [EXTRACTED]
- [[ApprovalRequest_3]] - `uses` [INFERRED]
- [[Routes approval notifications to owner DM and (optionally) group thread.      Ar]] - `rationale_for` [EXTRACTED]
- [[TestDMApprovalOwnerOnly]] - `uses` [INFERRED]
- [[TestGroupApprovalOwnerDM]] - `uses` [INFERRED]
- [[TestGroupApprovalRouterContextDetection]] - `uses` [INFERRED]
- [[TestGroupApprovalRouterDefaultSend]] - `uses` [INFERRED]
- [[group_router.py]] - `contains` [EXTRACTED]
- [[router()]] - `calls` [EXTRACTED]
- [[router_with_sent()]] - `calls` [EXTRACTED]
- [[test_group_approval_routing.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Group_Approval_Routing