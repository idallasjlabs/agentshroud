---
type: community
cohesion: 0.10
members: 32
---

# Community 242

**Cohesion:** 0.10 - loosely connected
**Members:** 32 nodes

## Members
- [[.test_execute_nonzero_exit()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_execute_success()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_execute_timeout()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_execute_unknown_host()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_is_auto_approved_no()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_is_auto_approved_unknown_host()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_is_auto_approved_yes()]] - code - gateway/tests/test_ssh_proxy.py
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
- [[SSHProxy_1]] - code - gateway/tests/test_ssh_proxy.py
- [[Test newline-based injection attempts (Finding 11)]] - rationale - gateway/tests/test_ssh_proxy.py
- [[TestExecute]] - code - gateway/tests/test_ssh_proxy.py
- [[TestInjectionNewline]] - code - gateway/tests/test_ssh_proxy.py
- [[TestIsAutoApproved]] - code - gateway/tests/test_ssh_proxy.py
- [[TestValidateCommand]] - code - gateway/tests/test_ssh_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_242
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_Community 15]]
- 5 edges to [[_COMMUNITY_Community 64]]
- 3 edges to [[_COMMUNITY_Community 24]]

## Top bridge nodes
- [[SSHProxy_1]] - degree 30, connects to 2 communities
- [[TestValidateCommand]] - degree 17, connects to 2 communities
- [[TestInjectionNewline]] - degree 12, connects to 2 communities
- [[TestExecute]] - degree 9, connects to 2 communities
- [[TestIsAutoApproved]] - degree 8, connects to 2 communities