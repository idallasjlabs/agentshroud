---
type: community
cohesion: 0.22
members: 9
---

# ProxyAction

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[dot-test_admin_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_allowed_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_terminal_in_private_tools()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_terminal_tool_in_private_tools()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_terminal_tool_not_in_collab_allowed()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_viewer_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[TestCVE2026_9367TerminalToolDenied]] - code - gateway/tests/test_tool_acl.py
- [[terminal_tool must be in PRIVATE_TOOLS and blocked for non-owner principals.]] - rationale - gateway/tests/test_tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ProxyAction
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_RBACConfig_1]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]

## Top bridge nodes
- [[TestCVE2026_9367TerminalToolDenied]] - degree 14, connects to 3 communities
