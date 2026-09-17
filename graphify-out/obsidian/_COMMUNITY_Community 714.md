---
type: community
cohesion: 0.14
members: 14
---

# Community 714

**Cohesion:** 0.14 - loosely connected
**Members:** 14 nodes

## Members
- [[dot-test_readonly_allowed_read_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_readonly_allowed_web_search_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_readonly_denied_email_sending_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_readonly_denied_external_api_calls_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_readonly_denied_file_deletion_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_readonly_denied_skill_installation_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[Read-only member IS allowed read tool in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only member IS allowed web_search (low-risk) in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only member denied email_sending even when called from group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only member denied external_api_calls in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only member denied file_deletion in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only member denied skill_installation in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only members must be denied high-risk tools in any group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[TestReadOnlyMemberGroupContext]] - code - gateway/tests/test_group_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_714
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Community 134]]
- 2 edges to [[_COMMUNITY_Community 121]]
- 1 edge to [[_COMMUNITY_Ingest API & RBAC Core]]
- 1 edge to [[_COMMUNITY_TeamsGroup Collaborator Responses]]
- 1 edge to [[_COMMUNITY_Community 746]]

## Top bridge nodes
- [[TestReadOnlyMemberGroupContext]] - degree 14, connects to 5 communities