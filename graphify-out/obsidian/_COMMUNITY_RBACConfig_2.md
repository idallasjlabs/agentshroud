---
type: community
cohesion: 0.25
members: 9
---

# RBACConfig

**Cohesion:** 0.25 - loosely connected
**Members:** 9 nodes

## Members
- [[dot-_can_use_tool_impl()]] - code - gateway/security/tool_acl.py
- [[dot-_get_group_tool_allowlist()]] - code - gateway/security/tool_acl.py
- [[dot-_get_role()]] - code - gateway/security/tool_acl.py
- [[dot-get_allowed_tools()]] - code - gateway/security/tool_acl.py
- [[dot-get_denied_tools()]] - code - gateway/security/tool_acl.py
- [[Check whether user_id may invoke the named tool.          Returns             (]] - rationale - gateway/security/tool_acl.py
- [[Collect additional tools granted to the user via their group memberships.]] - rationale - gateway/security/tool_acl.py
- [[Return the list of tools the user is allowed to use (union of all sets).]] - rationale - gateway/security/tool_acl.py
- [[Return tools explicitly denied for this user.]] - rationale - gateway/security/tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RBACConfig
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_ModuleStatsCollector]]

## Top bridge nodes
- [[dot-_can_use_tool_impl()]] - degree 5, connects to 2 communities
- [[dot-get_allowed_tools()]] - degree 4, connects to 1 community
- [[dot-_get_group_tool_allowlist()]] - degree 4, connects to 1 community
- [[dot-_get_role()]] - degree 4, connects to 1 community
- [[dot-get_denied_tools()]] - degree 3, connects to 1 community
