---
type: community
cohesion: 0.11
members: 21
---

# ._can_use_tool_impl()

**Cohesion:** 0.11 - loosely connected
**Members:** 21 nodes

## Members
- [[._can_use_tool_impl()]] - code - gateway/security/tool_acl.py
- [[._can_use_tool_impl()_1]] - code - gateway/security/tool_acl.py
- [[._get_group_tool_allowlist()]] - code - gateway/security/tool_acl.py
- [[._get_group_tool_allowlist()_1]] - code - gateway/security/tool_acl.py
- [[._get_role()]] - code - gateway/security/tool_acl.py
- [[._get_role()_1]] - code - gateway/security/tool_acl.py
- [[.can_use_tool()_2]] - code - gateway/security/tool_acl.py
- [[.can_use_tool_from_origin()_1]] - code - gateway/security/tool_acl.py
- [[.can_use_tool_in_group_context()_1]] - code - gateway/security/tool_acl.py
- [[.get_allowed_tools()]] - code - gateway/security/tool_acl.py
- [[.get_allowed_tools()_1]] - code - gateway/security/tool_acl.py
- [[.get_denied_tools()]] - code - gateway/security/tool_acl.py
- [[.get_denied_tools()_1]] - code - gateway/security/tool_acl.py
- [[Authorize a tool call, refusing owner elevation over an unverified origin.]] - rationale - gateway/security/tool_acl.py
- [[Check whether user_id may invoke the named tool.          Returns             (]] - rationale - gateway/security/tool_acl.py
- [[Check whether user_id may invoke the named tool. Returns (allowed bool,…]] - rationale - gateway/security/tool_acl.py
- [[Check whether user_id may invoke tool_name when acting inside a group workspace.]] - rationale - gateway/security/tool_acl.py
- [[Collect additional tools granted to the user via their group memberships.]] - rationale - gateway/security/tool_acl.py
- [[Public entry — records the decision for the SOC heat-map (SCRUM-80),         the_1]] - rationale - gateway/security/tool_acl.py
- [[Return the list of tools the user is allowed to use (union of all sets).]] - rationale - gateway/security/tool_acl.py
- [[Return tools explicitly denied for this user.]] - rationale - gateway/security/tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_can_use_tool_impl
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_ToolACLEnforcer]]
- 6 edges to [[_COMMUNITY_ToolACLEnforcer]]

## Top bridge nodes
- [[._can_use_tool_impl()]] - degree 5, connects to 1 community
- [[.can_use_tool()_2]] - degree 5, connects to 1 community
- [[._can_use_tool_impl()_1]] - degree 5, connects to 1 community
- [[.get_allowed_tools()]] - degree 4, connects to 1 community
- [[._get_group_tool_allowlist()]] - degree 4, connects to 1 community