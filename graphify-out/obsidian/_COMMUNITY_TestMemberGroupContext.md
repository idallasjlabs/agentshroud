---
type: community
members: 12
---

# TestMemberGroupContext

**Members:** 12 nodes

## Members
- [[dot-test_member_allowed_read_write_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_member_allowed_web_search_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_member_denied_gmail_private_tool_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_member_denied_high_risk_tools_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_member_denied_ssh_private_tool_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[Regular member (non-owner group role) is denied high-risk tools that require…]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member IS allowed readwrite in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member IS allowed web_search in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member denied gmail (private tool) even in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member denied ssh (private tool) in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular members can use medium-risk tools but not privateadmin tools.]] - rationale - gateway/tests/test_group_rbac.py
- [[TestMemberGroupContext]] - code - gateway/tests/test_group_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestMemberGroupContext
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_group_rbac.py]]

## Top bridge nodes
- [[TestMemberGroupContext]] - degree 7, connects to 1 community
