---
type: community
cohesion: 0.08
members: 44
---

# Module Group 94

**Cohesion:** 0.08 - loosely connected
**Members:** 44 nodes

## Members
- [[.expand_key_path()]] - code - gateway/ingest_api/ssh_config.py
- [[.expand_known_hosts()]] - code - gateway/ingest_api/ssh_config.py
- [[.test_execute_nonzero_exit()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_execute_success()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_execute_timeout()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_execute_unknown_host()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_is_auto_approved_no()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_is_auto_approved_unknown_host()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_is_auto_approved_yes()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_ssh_disabled_config()]] - code - gateway/tests/test_ssh_proxy.py
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
- [[Configuration for a single SSH host]] - rationale - gateway/ingest_api/ssh_config.py
- [[SSHConfig_2]] - code - gateway/tests/test_ssh_proxy.py
- [[SSHHostConfig]] - code - gateway/ingest_api/ssh_config.py
- [[SSHProxy_1]] - code - gateway/tests/test_ssh_proxy.py
- [[Test SSH disabled returns 503 (Finding 12)]] - rationale - gateway/tests/test_ssh_proxy.py
- [[Test newline-based injection attempts (Finding 11)]] - rationale - gateway/tests/test_ssh_proxy.py
- [[TestExecute]] - code - gateway/tests/test_ssh_proxy.py
- [[TestInjectionNewline]] - code - gateway/tests/test_ssh_proxy.py
- [[TestIsAutoApproved]] - code - gateway/tests/test_ssh_proxy.py
- [[TestSSHDisabled]] - code - gateway/tests/test_ssh_proxy.py
- [[TestValidateCommand]] - code - gateway/tests/test_ssh_proxy.py
- [[proxy()_1]] - code - gateway/tests/test_ssh_proxy.py
- [[ssh_config()_1]] - code - gateway/tests/test_ssh_proxy.py
- [[ssh_config.py]] - code - gateway/ingest_api/ssh_config.py
- [[test_ssh_proxy.py]] - code - gateway/tests/test_ssh_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_94
SORT file.name ASC
```

## Connections to other communities
- 35 edges to [[_COMMUNITY_SSH Proxy & Gateway Config]]
- 7 edges to [[_COMMUNITY_Module Group 132]]
- 3 edges to [[_COMMUNITY_Module Group 74]]
- 2 edges to [[_COMMUNITY_Module Group 495]]
- 1 edge to [[_COMMUNITY_Module Group 83]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_Module Group 444]]
- 1 edge to [[_COMMUNITY_Module Group 337]]

## Top bridge nodes
- [[SSHHostConfig]] - degree 35, connects to 6 communities
- [[ssh_config.py]] - degree 3, connects to 2 communities
- [[SSHProxy_1]] - degree 30, connects to 1 community
- [[TestValidateCommand]] - degree 17, connects to 1 community
- [[TestInjectionNewline]] - degree 12, connects to 1 community
