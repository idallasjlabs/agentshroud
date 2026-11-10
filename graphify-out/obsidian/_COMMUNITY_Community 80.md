---
type: community
members: 79
---

# Community 80

**Members:** 79 nodes

## Members
- [[.execute()]] - code - gateway/ssh_proxy/proxy.py
- [[.expand_key_path()]] - code - gateway/ingest_api/ssh_config.py
- [[.expand_known_hosts()]] - code - gateway/ingest_api/ssh_config.py
- [[.no_approval_client()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_invalid_router_url_rejected()]] - code - gateway/tests/test_config_validation.py
- [[.test_invalid_target_url_rejected()]] - code - gateway/tests/test_config_validation.py
- [[.test_non_auto_approved_executes_directly()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_router_url_must_be_localhost_or_openclaw()]] - code - gateway/tests/test_config_validation.py
- [[.test_ssh_approval_sanitizes_command_pii()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ssh_command_uses_strict_checking()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ssh_disabled_config()]] - code - gateway/tests/test_ssh_proxy.py
- [[.test_ssh_exec_auto_approved()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_command_not_in_allowlist()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_cwd_accepted_and_forwarded()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_cwd_invalid_rejects_400()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_cwd_none_forwards_none()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_cwd_relative_path_rejects_400()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_denied_command()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_disabled_returns_503()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_injection_attempt()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_no_auth()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_requires_approval()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_unknown_host()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_history()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_hosts_list()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_strict_host_key_checking_in_source()]] - code - gateway/tests/test_security_fixes.py
- [[.validate_default_url()]] - code - gateway/ingest_api/config.py
- [[.validate_targets()]] - code - gateway/ingest_api/config.py
- [[Approval queue details must be PII-sanitized before storage]] - rationale - gateway/tests/test_security_fixes.py
- [[Both bots must be reachable via the same router without conflict.]] - rationale - gateway/tests/test_router.py
- [[Configuration for a single SSH host]] - rationale - gateway/ingest_api/ssh_config.py
- [[Execute a command on a remote host via SSH.]] - rationale - gateway/ssh_proxy/proxy.py
- [[Multi-agent router configuration]] - rationale - gateway/ingest_api/config.py
- [[MultiAgentRouter]] - code - gateway/ingest_api/router.py
- [[Omitting cwd passes cwd=None to proxy.execute().]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[Result of an SSH command execution]] - rationale - gateway/ssh_proxy/proxy.py
- [[RouterConfig]] - code - gateway/ingest_api/config.py
- [[Routes content to appropriate agent containers      Routing priority     1. Exp]] - rationale - gateway/ingest_api/router.py
- [[SSH exec requiring approval sanitizes PII in command before storing]] - rationale - gateway/tests/test_security_fixes.py
- [[SSH execute builds command with StrictHostKeyChecking=yes]] - rationale - gateway/tests/test_security_fixes.py
- [[SSHConfig]] - code - gateway/ingest_api/ssh_config.py
- [[SSHConfig_2]] - code - gateway/tests/test_ssh_proxy.py
- [[SSHHostConfig]] - code - gateway/ingest_api/ssh_config.py
- [[SSHResult]] - code - gateway/ssh_proxy/proxy.py
- [[Set up app state and provide TestClient.]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[Source code uses StrictHostKeyChecking=yes]] - rationale - gateway/tests/test_security_fixes.py
- [[Test SSH disabled returns 503 (Finding 12)]] - rationale - gateway/tests/test_ssh_proxy.py
- [[Test require_approval=false executes directly (Finding 5)]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[Test that SSH disabled returns 503 (Finding 12)]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[TestApprovalQueuePIISanitization]] - code - gateway/tests/test_security_fixes.py
- [[TestSSHDisabled]] - code - gateway/tests/test_ssh_proxy.py
- [[TestSSHDisabledEndpoint]] - code - gateway/tests/test_ssh_endpoints.py
- [[TestSSHExec]] - code - gateway/tests/test_ssh_endpoints.py
- [[TestSSHHistory]] - code - gateway/tests/test_ssh_endpoints.py
- [[TestSSHHosts]] - code - gateway/tests/test_ssh_endpoints.py
- [[TestSSHRequireApprovalFalse]] - code - gateway/tests/test_ssh_endpoints.py
- [[TestSSHStrictHostKeyChecking]] - code - gateway/tests/test_security_fixes.py
- [[Top-level MCP proxy configuration.]] - rationale - gateway/proxy/mcp_config.py
- [[Top-level SSH proxy configuration]] - rationale - gateway/ingest_api/ssh_config.py
- [[Validate that default_url uses httphttps and targets an internal Docker host.]] - rationale - gateway/ingest_api/config.py
- [[Validate that each target URL uses httphttps and targets an internal Docker hos]] - rationale - gateway/ingest_api/config.py
- [[Verify SSH proxy uses StrictHostKeyChecking=yes, not accept-new]] - rationale - gateway/tests/test_security_fixes.py
- [[When require_approval=false, non-auto-approved commands execute directly.]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[auth_headers()_3]] - code - gateway/tests/test_ssh_endpoints.py
- [[client()_16]] - code - gateway/tests/test_ssh_endpoints.py
- [[cwd is validated and passed to proxy.execute().]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[cwd must be an absolute path.]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[cwd with shell metacharacters is rejected before execution.]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[proxy()_3]] - code - gateway/tests/test_ssh_proxy.py
- [[route_to='hermes' must resolve to the Hermes AgentTarget.]] - rationale - gateway/tests/test_router.py
- [[router()_2]] - code - gateway/tests/test_router_openai_translation.py
- [[ssh_config()]] - code - gateway/tests/test_ssh_endpoints.py
- [[ssh_config()_1]] - code - gateway/tests/test_ssh_proxy.py
- [[ssh_config.py]] - code - gateway/ingest_api/ssh_config.py
- [[test_config_with_ssh()]] - code - gateway/tests/test_ssh_endpoints.py
- [[test_hermes_and_openclaw_coexist()]] - code - gateway/tests/test_router.py
- [[test_resolves_hermes_target()]] - code - gateway/tests/test_router.py
- [[test_ssh_endpoints.py]] - code - gateway/tests/test_ssh_endpoints.py
- [[test_ssh_proxy.py]] - code - gateway/tests/test_ssh_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_80
SORT file.name ASC
```

## Connections to other communities
- 57 edges to [[_COMMUNITY_Community 50]]
- 44 edges to [[_COMMUNITY_Community 7]]
- 20 edges to [[_COMMUNITY_Community 25]]
- 18 edges to [[_COMMUNITY_Community 2051]]
- 13 edges to [[_COMMUNITY_Community 861]]
- 11 edges to [[_COMMUNITY_Community 707]]
- 11 edges to [[_COMMUNITY_Community 30]]
- 10 edges to [[_COMMUNITY_Community 104]]
- 8 edges to [[_COMMUNITY_Community 439]]
- 6 edges to [[_COMMUNITY_Community 36]]
- 6 edges to [[_COMMUNITY_Community 34]]
- 5 edges to [[_COMMUNITY_Community 541]]
- 5 edges to [[_COMMUNITY_Community 78]]
- 5 edges to [[_COMMUNITY_Community 325]]
- 5 edges to [[_COMMUNITY_Community 72]]
- 4 edges to [[_COMMUNITY_Community 105]]
- 3 edges to [[_COMMUNITY_Community 10]]
- 3 edges to [[_COMMUNITY_Community 35]]
- 3 edges to [[_COMMUNITY_Community 92]]
- 2 edges to [[_COMMUNITY_Community 1360]]
- 1 edge to [[_COMMUNITY_Community 47]]
- 1 edge to [[_COMMUNITY_Community 532]]
- 1 edge to [[_COMMUNITY_Community 229]]
- 1 edge to [[_COMMUNITY_Community 94]]
- 1 edge to [[_COMMUNITY_Community 43]]
- 1 edge to [[_COMMUNITY_Community 54]]

## Top bridge nodes
- [[RouterConfig]] - degree 66, connects to 14 communities
- [[SSHConfig]] - degree 61, connects to 11 communities
- [[MultiAgentRouter]] - degree 47, connects to 11 communities
- [[SSHHostConfig]] - degree 44, connects to 5 communities
- [[TestSSHExec]] - degree 25, connects to 5 communities