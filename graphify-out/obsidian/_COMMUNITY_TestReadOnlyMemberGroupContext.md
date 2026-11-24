---
type: community
members: 14
---

# TestReadOnlyMemberGroupContext

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
TABLE source_file, type FROM #community/TestReadOnlyMemberGroupContext
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_GroupRoleResolver]]

## Top bridge nodes
- [[TestReadOnlyMemberGroupContext]] - degree 8, connects to 1 community
