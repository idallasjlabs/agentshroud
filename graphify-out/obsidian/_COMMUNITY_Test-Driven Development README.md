---
type: community
cohesion: 0.12
members: 16
---

# Test-Driven Development README

**Cohesion:** 0.12 - loosely connected
**Members:** 16 nodes

## Members
- [[.test_ssh_exec_auto_approved()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_command_not_in_allowlist()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_cwd_accepted_and_forwarded()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_cwd_invalid_rejects_400()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_cwd_none_forwards_none()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_cwd_relative_path_rejects_400()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_denied_command()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_injection_attempt()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_no_auth()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_requires_approval()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_unknown_host()]] - code - gateway/tests/test_ssh_endpoints.py
- [[Omitting cwd passes cwd=None to proxy.execute().]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[TestSSHExec]] - code - gateway/tests/test_ssh_endpoints.py
- [[cwd is validated and passed to proxy.execute().]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[cwd must be an absolute path.]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[cwd with shell metacharacters is rejected before execution.]] - rationale - gateway/tests/test_ssh_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Test-Driven_Development_README
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 2 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_EgressPolicy]]
- 2 edges to [[_COMMUNITY_ApprovalRequest]]
- 1 edge to [[_COMMUNITY_ModeRequest]]

## Top bridge nodes
- [[TestSSHExec]] - degree 25, connects to 6 communities
- [[.test_ssh_exec_cwd_accepted_and_forwarded()]] - degree 3, connects to 1 community
- [[.test_ssh_exec_cwd_none_forwards_none()]] - degree 3, connects to 1 community
- [[.test_ssh_exec_auto_approved()]] - degree 2, connects to 1 community