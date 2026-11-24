---
source_file: "gateway/approval_queue/group_router.py"
type: "code"
community: "ApprovalRequest"
location: "L37"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ApprovalRequest
---

# GroupApprovalRouter

## Connections
- [[dot-__init__()_24]] - `method` [EXTRACTED]
- [[dot-_build_group_reply_text()]] - `method` [EXTRACTED]
- [[dot-_build_owner_dm_text()]] - `method` [EXTRACTED]
- [[dot-_default_send()]] - `method` [EXTRACTED]
- [[dot-extract_group_chat_id()]] - `method` [EXTRACTED]
- [[dot-is_group_context()]] - `method` [EXTRACTED]
- [[dot-route_approval()]] - `method` [EXTRACTED]
- [[dot-test_extract_chat_id_from_group_agent_id()]] - `calls` [EXTRACTED]
- [[dot-test_extract_chat_id_returns_none_for_non_group()]] - `calls` [EXTRACTED]
- [[dot-test_is_group_context_false_for_collab_agent_id()]] - `calls` [EXTRACTED]
- [[dot-test_is_group_context_false_for_default()]] - `calls` [EXTRACTED]
- [[dot-test_is_group_context_true_for_group_agent_id()]] - `calls` [EXTRACTED]
- [[dot-test_router_works_without_send_fn()]] - `calls` [EXTRACTED]
- [[ApprovalRequest]] - `uses` [INFERRED]
- [[Routes approval notifications to owner DM and (optionally) group thread. Args…]] - `rationale_for` [EXTRACTED]
- [[TestGroupApprovalRouterContextDetection]] - `uses` [INFERRED]
- [[TestGroupApprovalRouterDefaultSend]] - `uses` [INFERRED]
- [[group_router.py]] - `contains` [EXTRACTED]
- [[router()]] - `uses` [INFERRED]
- [[router_with_sent()]] - `uses` [INFERRED]
- [[test_group_approval_routing.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ApprovalRequest
