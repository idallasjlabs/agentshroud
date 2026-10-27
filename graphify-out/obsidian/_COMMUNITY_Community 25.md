---
type: community
members: 52
---

# Community 25

**Members:** 52 nodes

## Members
- [[.execute()]] - code - gateway/ssh_proxy/proxy.py
- [[.test_execute_nonzero_exit()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_execute_success()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_execute_timeout()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_execute_unknown_host()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_is_auto_approved_no()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_is_auto_approved_unknown_host()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_is_auto_approved_yes()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_non_auto_approved_executes_directly()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_disabled_config()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_ssh_exec_cwd_accepted_and_forwarded()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_cwd_none_forwards_none()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_history()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_validate_auto_approve_exact_only()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_validate_command_allowed()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_validate_command_backslash_n_injection()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_validate_command_carriage_return_injection()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_validate_command_denied()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_validate_command_dollar_brace_injection()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_validate_command_dollar_var_injection()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_validate_command_global_denied()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_validate_command_injection_blocked_and()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_validate_command_injection_blocked_backticks()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_validate_command_injection_blocked_dollar_paren()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_validate_command_injection_blocked_or()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_validate_command_injection_blocked_pipe()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_validate_command_injection_blocked_semicolon()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_validate_command_newline_injection()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_validate_command_not_in_allowlist()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_validate_command_unknown_host()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_validate_empty_command()]] - code - gateway/tests/test_ssh_proxy.py
- [[Auto-approve must be exact match, not prefix (Finding 3)]] - rationale - gateway/tests/test_ssh_proxy.py
- [[Execute a command on a remote host via SSH.]] - rationale - gateway/ssh_proxy/proxy.py
- [[Omitting cwd passes cwd=None to proxy.execute().]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[Result of an SSH command execution]] - rationale - gateway/ssh_proxy/proxy.py
- [[SSHConfig_2]] - code - gateway/tests/test_ssh_proxy.py
- [[SSHProxy_1]] - code - gateway/tests/test_ssh_proxy.py
- [[SSHResult]] - code - gateway/ssh_proxy/proxy.py
- [[Test SSH disabled returns 503 (Finding 12)]] - rationale - gateway/tests/test_ssh_proxy.py
- [[Test newline-based injection attempts (Finding 11)]] - rationale - gateway/tests/test_ssh_proxy.py
- [[TestExecute]] - code - gateway/tests/test_ssh_proxy.py
- [[TestInjectionNewline]] - code - gateway/tests/test_ssh_proxy.py
- [[TestIsAutoApproved]] - code - gateway/tests/test_ssh_proxy.py
- [[TestSSHDisabled]] - code - gateway/tests/test_ssh_proxy.py
- [[TestValidateCommand]] - code - gateway/tests/test_ssh_proxy.py
- [[When require_approval=false, non-auto-approved commands execute directly.]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[__init__.py_12]] - code - gateway/ssh_proxy/__init__.py
- [[cwd is validated and passed to proxy.execute().]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[proxy()_3]] - code - gateway/tests/test_ssh_proxy.py
- [[proxy.py]] - code - gateway/ssh_proxy/proxy.py
- [[ssh_config()_1]] - code - gateway/tests/test_ssh_proxy.py
- [[test_ssh_proxy.py]] - code - gateway/tests/test_ssh_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_25
SORT file.name ASC
```

## Connections to other communities
- 32 edges to [[_COMMUNITY_Community 7]]
- 12 edges to [[_COMMUNITY_Community 50]]
- 3 edges to [[_COMMUNITY_Community 37]]
- 2 edges to [[_COMMUNITY_Community 104]]
- 1 edge to [[_COMMUNITY_Community 978]]
- 1 edge to [[_COMMUNITY_Community 162]]

## Top bridge nodes
- [[proxy.py]] - degree 10, connects to 5 communities
- [[SSHProxy_1]] - degree 30, connects to 2 communities
- [[SSHResult]] - degree 25, connects to 2 communities
- [[TestValidateCommand]] - degree 17, connects to 2 communities
- [[TestInjectionNewline]] - degree 12, connects to 2 communities