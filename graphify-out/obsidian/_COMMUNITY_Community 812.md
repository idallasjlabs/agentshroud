---
type: community
cohesion: 0.17
members: 12
---

# Community 812

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
TABLE source_file, type FROM #community/Community_812
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Community 134]]
- 2 edges to [[_COMMUNITY_Community 121]]
- 1 edge to [[_COMMUNITY_Ingest API & RBAC Core]]
- 1 edge to [[_COMMUNITY_TeamsGroup Collaborator Responses]]
- 1 edge to [[_COMMUNITY_Community 746]]

## Top bridge nodes
- [[TestMemberGroupContext]] - degree 13, connects to 5 communities