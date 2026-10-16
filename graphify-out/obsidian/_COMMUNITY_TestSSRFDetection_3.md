---
type: community
cohesion: 0.17
members: 12
---

# TestSSRFDetection

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[dot-test_member_allowed_read_write_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_member_allowed_web_search_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_member_denied_gmail_private_tool_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_member_denied_high_risk_tools_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_member_denied_ssh_private_tool_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[Regular member (non-owner group role) is denied high-risk tools that require app]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member IS allowed readwrite in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member IS allowed web_search in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member denied gmail (private tool) even in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member denied ssh (private tool) in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular members can use medium-risk tools but not privateadmin tools.]] - rationale - gateway/tests/test_group_rbac.py
- [[TestMemberGroupContext]] - code - gateway/tests/test_group_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSSRFDetection
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_GroupRoleResolver]]
- 2 edges to [[_COMMUNITY_RBACConfig_1]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[TestMemberGroupContext]] - degree 13, connects to 4 communities
