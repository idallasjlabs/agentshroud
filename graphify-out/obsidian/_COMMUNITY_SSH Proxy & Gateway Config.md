---
type: community
cohesion: 0.05
members: 75
---

# SSH Proxy & Gateway Config

**Cohesion:** 0.05 - loosely connected
**Members:** 75 nodes

## Members
- [[.__init__()_107]] - code - gateway/ssh_proxy/proxy.py
- [[.disabled_client()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.execute()]] - code - gateway/ssh_proxy/proxy.py
- [[.is_auto_approved()]] - code - gateway/ssh_proxy/proxy.py
- [[.no_approval_client()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_config_with_tool_result_pii()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_get_module_mode_no_env_override()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_global_monitor_override_downgrades_all()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_mcp_proxy_data_defaults_to_empty_when_absent()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_mcp_proxy_data_parsed_from_yaml()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_non_auto_approved_executes_directly()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_proxy_allowed_domains_defaults_to_empty_when_absent()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_proxy_allowed_domains_parsed_from_yaml()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_ssh_approval_sanitizes_command_pii()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ssh_exec_auto_approved()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_command_not_in_allowlist()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_denied_command()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_disabled_returns_503()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_injection_attempt()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_no_auth()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_requires_approval()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_exec_unknown_host()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_history()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_ssh_hosts_list()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.validate_command()]] - code - gateway/ssh_proxy/proxy.py
- [[AGENTSHROUD_MODE=monitor must downgrade ALL modules to monitor.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[Approval queue details must be PII-sanitized before storage]] - rationale - gateway/tests/test_security_fixes.py
- [[Check if a command is auto-approved (no human approval needed).          Auto-ap]] - rationale - gateway/ssh_proxy/proxy.py
- [[Complete gateway configuration]] - rationale - gateway/ingest_api/config.py
- [[Config with all security modules enabled.]] - rationale - gateway/tests/test_security_integration.py
- [[Create a router configuration for testing]] - rationale - gateway/tests/test_router.py
- [[Execute a command on a remote host via SSH.]] - rationale - gateway/ssh_proxy/proxy.py
- [[GatewayConfig_3]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[GatewayConfig_1]] - code - gateway/ingest_api/config.py
- [[Multi-agent router configuration]] - rationale - gateway/ingest_api/config.py
- [[Result of an SSH command execution]] - rationale - gateway/ssh_proxy/proxy.py
- [[RouterConfig]] - code - gateway/ingest_api/config.py
- [[SSH command proxy with validation and audit support]] - rationale - gateway/ssh_proxy/proxy.py
- [[SSH exec requiring approval sanitizes PII in command before storing]] - rationale - gateway/tests/test_security_fixes.py
- [[SSHConfig_1]] - code - gateway/ssh_proxy/proxy.py
- [[SSHConfig]] - code - gateway/ingest_api/ssh_config.py
- [[SSHProxy]] - code - gateway/ssh_proxy/proxy.py
- [[SSHResult]] - code - gateway/ssh_proxy/proxy.py
- [[Set up app state and provide TestClient.]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[Test require_approval=false executes directly (Finding 5)]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[Test that SSH disabled returns 503 (Finding 12)]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[Test that configuration includes tool result PII settings]] - rationale - gateway/tests/test_tool_result_pii.py
- [[TestApprovalQueuePIISanitization]] - code - gateway/tests/test_security_fixes.py
- [[TestMCPProxyConfigLoading]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[TestSSHDisabledEndpoint]] - code - gateway/tests/test_ssh_endpoints.py
- [[TestSSHExec]] - code - gateway/tests/test_ssh_endpoints.py
- [[TestSSHHistory]] - code - gateway/tests/test_ssh_endpoints.py
- [[TestSSHHosts]] - code - gateway/tests/test_ssh_endpoints.py
- [[TestSSHRequireApprovalFalse]] - code - gateway/tests/test_ssh_endpoints.py
- [[Top-level SSH proxy configuration]] - rationale - gateway/ingest_api/ssh_config.py
- [[Validate a command against allowdeny lists and injection patterns.          Ret]] - rationale - gateway/ssh_proxy/proxy.py
- [[When require_approval=false, non-auto-approved commands execute directly.]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[__init__.py_10]] - code - gateway/ssh_proxy/__init__.py
- [[auth_headers()_2]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[auth_headers()_3]] - code - gateway/tests/test_ssh_endpoints.py
- [[client()_13]] - code - gateway/tests/test_ssh_endpoints.py
- [[full_pipeline_config()]] - code - gateway/tests/test_security_integration.py
- [[load_config computes CORS origins from the configured port.]] - rationale - gateway/tests/test_router.py
- [[mcp_proxy_data is an empty dict when section is absent from YAML.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[mcp_proxy_data is populated from the mcp_proxy YAML section.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[proxy.py]] - code - gateway/ssh_proxy/proxy.py
- [[proxy_allowed_domains is empty list when proxy section is absent from YAML.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[proxy_allowed_domains is populated from the proxy.allowed_domains YAML section.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[router_config()]] - code - gateway/tests/test_router.py
- [[ssh_config()]] - code - gateway/tests/test_ssh_endpoints.py
- [[test_config()_1]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[test_config_with_ssh()]] - code - gateway/tests/test_ssh_endpoints.py
- [[test_cors_origins_include_configured_port()]] - code - gateway/tests/test_router.py
- [[test_mcp_result_endpoint.py]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[test_ssh_endpoints.py]] - code - gateway/tests/test_ssh_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SSH_Proxy__Gateway_Config
SORT file.name ASC
```

## Connections to other communities
- 35 edges to [[_COMMUNITY_Module Group 94]]
- 33 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 31 edges to [[_COMMUNITY_Ledger Config & Test Infra]]
- 25 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 22 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 17 edges to [[_COMMUNITY_Enhanced Approval Queue]]
- 15 edges to [[_COMMUNITY_Module Group 132]]
- 11 edges to [[_COMMUNITY_Agent Routing & Request Models]]
- 9 edges to [[_COMMUNITY_Approval Queue Core]]
- 8 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 6 edges to [[_COMMUNITY_Module Group 99]]
- 6 edges to [[_COMMUNITY_Module Group 126]]
- 5 edges to [[_COMMUNITY_Module Group 246]]
- 5 edges to [[_COMMUNITY_Config Validation Tests]]
- 4 edges to [[_COMMUNITY_Module Group 495]]
- 3 edges to [[_COMMUNITY_Module Group 83]]
- 3 edges to [[_COMMUNITY_Module Group 189]]
- 3 edges to [[_COMMUNITY_Module Group 255]]
- 3 edges to [[_COMMUNITY_Module Group 216]]
- 3 edges to [[_COMMUNITY_MCP Inspector & Audit]]
- 2 edges to [[_COMMUNITY_Module Group 127]]
- 2 edges to [[_COMMUNITY_Module Group 98]]
- 2 edges to [[_COMMUNITY_Module Group 444]]
- 2 edges to [[_COMMUNITY_Module Group 337]]
- 1 edge to [[_COMMUNITY_Authentication & Rate Limiting]]
- 1 edge to [[_COMMUNITY_Module Group 233]]
- 1 edge to [[_COMMUNITY_Module Group 488]]
- 1 edge to [[_COMMUNITY_Module Group 336]]
- 1 edge to [[_COMMUNITY_Module Group 311]]

## Top bridge nodes
- [[GatewayConfig_1]] - degree 69, connects to 17 communities
- [[RouterConfig]] - degree 54, connects to 12 communities
- [[SSHConfig]] - degree 51, connects to 11 communities
- [[SSHProxy]] - degree 40, connects to 7 communities
- [[test_mcp_result_endpoint.py]] - degree 12, connects to 7 communities
