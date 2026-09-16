---
type: community
cohesion: 0.11
members: 19
---

# Community 496

**Cohesion:** 0.11 - loosely connected
**Members:** 19 nodes

## Members
- [[dot-test_is_high_risk_false_for_web_search()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_is_high_risk_true_for_email_sending()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_is_high_risk_true_for_external_api_calls()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_is_high_risk_true_for_file_deletion()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_is_high_risk_true_for_skill_installation()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_member_resolves_to_member_role()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_non_member_defaults_to_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_owner_resolves_to_owner_role()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_readonly_user_resolves_to_readonly_role()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_unknown_group_defaults_to_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[GroupRoleResolver correctly maps Telegram user IDs to per-group roles.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only user resolves to GroupRole.READ_ONLY.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member resolves to GroupRole.MEMBER.]] - rationale - gateway/tests/test_group_rbac.py
- [[TestGroupRoleResolver]] - code - gateway/tests/test_group_rbac.py
- [[Unknown group_chat_id defaults to GroupRole.READ_ONLY.]] - rationale - gateway/tests/test_group_rbac.py
- [[User not in role map defaults to GroupRole.READ_ONLY (deny-by-default).]] - rationale - gateway/tests/test_group_rbac.py
- [[email_sending is recognized as a high-risk tool.]] - rationale - gateway/tests/test_group_rbac.py
- [[owner_in_group resolves to GroupRole.OWNER.]] - rationale - gateway/tests/test_group_rbac.py
- [[web_search is NOT a high-risk tool.]] - rationale - gateway/tests/test_group_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_496
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Community 134]]
- 2 edges to [[_COMMUNITY_Community 121]]
- 1 edge to [[_COMMUNITY_Ingest API & RBAC Core]]
- 1 edge to [[_COMMUNITY_TeamsGroup Collaborator Responses]]
- 1 edge to [[_COMMUNITY_Community 746]]

## Top bridge nodes
- [[TestGroupRoleResolver]] - degree 18, connects to 5 communities