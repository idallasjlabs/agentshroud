---
type: community
members: 25
---

# SSHResult

**Members:** 25 nodes

## Members
- [[dot-execute()]] - code - gateway/ssh_proxy/proxy.py
- [[dot-test_non_auto_approved_executes_directly()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_ssh_exec_auto_approved()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_ssh_exec_command_not_in_allowlist()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_ssh_exec_cwd_accepted_and_forwarded()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_ssh_exec_cwd_invalid_rejects_400()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_ssh_exec_cwd_none_forwards_none()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_ssh_exec_cwd_relative_path_rejects_400()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_ssh_exec_denied_command()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_ssh_exec_injection_attempt()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_ssh_exec_no_auth()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_ssh_exec_requires_approval()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_ssh_exec_unknown_host()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_ssh_history()]] - code - gateway/tests/test_ssh_endpoints.py
- [[Execute a command on a remote host via SSH.]] - rationale - gateway/ssh_proxy/proxy.py
- [[Omitting cwd passes cwd=None to proxy.execute().]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[Result of an SSH command execution]] - rationale - gateway/ssh_proxy/proxy.py
- [[SSHResult]] - code - gateway/ssh_proxy/proxy.py
- [[TestSSHExec]] - code - gateway/tests/test_ssh_endpoints.py
- [[TestSSHHistory]] - code - gateway/tests/test_ssh_endpoints.py
- [[When require_approval=false, non-auto-approved commands execute directly.]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[cwd is validated and passed to proxy.execute().]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[cwd must be an absolute path.]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[cwd with shell metacharacters is rejected before execution.]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[ssh_proxy__init__.py]] - code - gateway/ssh_proxy/__init__.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SSHResult
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 4 edges to [[_COMMUNITY_SSHProxy]]

## Top bridge nodes
- [[SSHResult]] - degree 15, connects to 2 communities
- [[ssh_proxy__init__.py]] - degree 3, connects to 2 communities
- [[TestSSHExec]] - degree 13, connects to 1 community
- [[TestSSHHistory]] - degree 3, connects to 1 community
- [[dot-execute()]] - degree 3, connects to 1 community
