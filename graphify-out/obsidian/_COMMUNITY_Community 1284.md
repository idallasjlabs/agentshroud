---
type: community
members: 12
---

# Community 1284

**Members:** 12 nodes

## Members
- [[.test_member_allowed_read_write_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_member_allowed_web_search_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_member_denied_gmail_private_tool_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_member_denied_high_risk_tools_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_member_denied_ssh_private_tool_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[Regular member (non-owner group role) is denied high-risk tools that require app]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member IS allowed readwrite in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member IS allowed web_search in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member denied gmail (private tool) even in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member denied ssh (private tool) in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular members can use medium-risk tools but not privateadmin tools.]] - rationale - gateway/tests/test_group_rbac.py
- [[TestMemberGroupContext]] - code - gateway/tests/test_group_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1284
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 33]]
- 1 edge to [[_COMMUNITY_Community 196]]
- 1 edge to [[_COMMUNITY_Community 6]]
- 1 edge to [[_COMMUNITY_Community 194]]
- 1 edge to [[_COMMUNITY_Community 11]]

## Top bridge nodes
- [[TestMemberGroupContext]] - degree 13, connects to 5 communities