---
type: community
cohesion: 0.05
members: 73
---

# SSHHostConfig

**Cohesion:** 0.05 - loosely connected
**Members:** 73 nodes

## Members
- [[dot-execute()]] - code - gateway/ssh_proxy/proxy.py
- [[dot-expand_key_path()]] - code - gateway/ingest_api/ssh_config.py
- [[dot-expand_known_hosts()]] - code - gateway/ingest_api/ssh_config.py
- [[dot-test_execute_nonzero_exit()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_execute_success()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_execute_timeout()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_execute_unknown_host()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_is_auto_approved_no()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_is_auto_approved_unknown_host()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_is_auto_approved_yes()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_non_auto_approved_executes_directly()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_ssh_approval_sanitizes_command_pii()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ssh_disabled_config()]] - code - gateway/tests/test_ssh_proxy.py
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
- [[dot-test_validate_auto_approve_exact_only()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_allowed()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_backslash_n_injection()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_carriage_return_injection()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_denied()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_dollar_brace_injection()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_dollar_var_injection()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_global_denied()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_injection_blocked_and()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_injection_blocked_backticks()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_injection_blocked_dollar_paren()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_injection_blocked_or()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_injection_blocked_pipe()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_injection_blocked_semicolon()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_newline_injection()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_not_in_allowlist()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_unknown_host()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_empty_command()]] - code - gateway/tests/test_ssh_proxy.py
- [[Approval queue details must be PII-sanitized before storage]] - rationale - gateway/tests/test_security_fixes.py
- [[Auto-approve must be exact match, not prefix (Finding 3)]] - rationale - gateway/tests/test_ssh_proxy.py
- [[Configuration for a single SSH host]] - rationale - gateway/ingest_api/ssh_config.py
- [[Execute a command on a remote host via SSH.]] - rationale - gateway/ssh_proxy/proxy.py
- [[Omitting cwd passes cwd=None to proxy.execute().]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[Result of an SSH command execution]] - rationale - gateway/ssh_proxy/proxy.py
- [[SSH exec requiring approval sanitizes PII in command before storing]] - rationale - gateway/tests/test_security_fixes.py
- [[SSHConfig_1]] - code - gateway/tests/test_ssh_proxy.py
- [[SSHHostConfig]] - code - gateway/ingest_api/ssh_config.py
- [[SSHProxy_1]] - code - gateway/tests/test_ssh_proxy.py
- [[SSHResult]] - code - gateway/ssh_proxy/proxy.py
- [[Test SSH disabled returns 503 (Finding 12)]] - rationale - gateway/tests/test_ssh_proxy.py
- [[Test newline-based injection attempts (Finding 11)]] - rationale - gateway/tests/test_ssh_proxy.py
- [[TestApprovalQueuePIISanitization]] - code - gateway/tests/test_security_fixes.py
- [[TestExecute]] - code - gateway/tests/test_ssh_proxy.py
- [[TestInjectionNewline]] - code - gateway/tests/test_ssh_proxy.py
- [[TestIsAutoApproved]] - code - gateway/tests/test_ssh_proxy.py
- [[TestSSHDisabled]] - code - gateway/tests/test_ssh_proxy.py
- [[TestSSHExec]] - code - gateway/tests/test_ssh_endpoints.py
- [[TestValidateCommand]] - code - gateway/tests/test_ssh_proxy.py
- [[When require_approval=false, non-auto-approved commands execute directly.]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[cwd is validated and passed to proxy.execute().]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[cwd must be an absolute path.]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[cwd with shell metacharacters is rejected before execution.]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[proxy()_1]] - code - gateway/tests/test_ssh_proxy.py
- [[proxy.py]] - code - gateway/ssh_proxy/proxy.py
- [[ssh_config()]] - code - gateway/tests/test_ssh_proxy.py
- [[ssh_config.py]] - code - gateway/ingest_api/ssh_config.py
- [[ssh_proxy__init__.py]] - code - gateway/ssh_proxy/__init__.py
- [[test_ssh_proxy.py]] - code - gateway/tests/test_ssh_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SSHHostConfig
SORT file.name ASC
```

## Connections to other communities
- 41 edges to [[_COMMUNITY_DataLedger]]
- 21 edges to [[_COMMUNITY_SSHProxy]]
- 12 edges to [[_COMMUNITY_test_security_fixes.py]]
- 3 edges to [[_COMMUNITY_AsyncMock]]
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_load_config]]
- 1 edge to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig]]

## Top bridge nodes
- [[SSHHostConfig]] - degree 44, connects to 4 communities
- [[TestSSHExec]] - degree 25, connects to 4 communities
- [[proxy.py]] - degree 9, connects to 4 communities
- [[TestApprovalQueuePIISanitization]] - degree 6, connects to 3 communities
- [[SSHProxy_1]] - degree 30, connects to 2 communities
