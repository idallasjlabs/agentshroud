---
type: community
cohesion: 0.08
members: 53
---

# GitGuard

**Cohesion:** 0.08 - loosely connected
**Members:** 53 nodes

## Members
- [[.__ge__()]] - code - gateway/proxy/mcp_config.py
- [[.__gt__()]] - code - gateway/proxy/mcp_config.py
- [[.__le__()]] - code - gateway/proxy/mcp_config.py
- [[.__lt__()]] - code - gateway/proxy/mcp_config.py
- [[._record_private_access_attempt()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_agent_server_access()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_all()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_rate_limit()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_tool_parameters()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_tool_permission()]] - code - gateway/proxy/mcp_permissions.py
- [[.from_dict()]] - code - gateway/proxy/mcp_config.py
- [[.get_trust_level()]] - code - gateway/proxy/mcp_permissions.py
- [[.infer_permission_level()]] - code - gateway/proxy/mcp_permissions.py
- [[.level_value()]] - code - gateway/proxy/mcp_config.py
- [[.test_no_limit_always_allowed()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_rate_limit_enforced()_1]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_rate_limit_per_agent()]] - code - gateway/tests/test_mcp_permissions.py
- [[A single finding from inspection.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Any_16]] - code - gateway/proxy/mcp_config.py
- [[Audit signal for blocked admin-private tool access attempts.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Audit signal when admin-private data is redacted from tool results.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Block non-owner tool calls that reference admin-private data pathscontent.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check and update rate limits for a tool call.          Returns allowed=True and]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can access a server at all.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can call a specific tool.          Default-allow only blocks]] - rationale - gateway/proxy/mcp_permissions.py
- [[Configuration for an MCP server.]] - rationale - gateway/proxy/mcp_config.py
- [[Get trust level, defaulting to 1 (write) for unknown agents.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Infer the permission level needed for a tool based on its name.          Checks]] - rationale - gateway/proxy/mcp_permissions.py
- [[InspectionFinding]] - code - gateway/proxy/mcp_inspector.py
- [[MCPProxyConfig_1]] - code - gateway/proxy/mcp_permissions.py
- [[MCPProxyConfig]] - code - gateway/proxy/mcp_config.py
- [[MCPServerConfig_1]] - code - gateway/proxy/mcp_permissions.py
- [[MCPServerConfig]] - code - gateway/proxy/mcp_config.py
- [[Parse config from a dictionary (e.g. loaded from YAML).]] - rationale - gateway/proxy/mcp_config.py
- [[PermissionCheck]] - code - gateway/proxy/mcp_permissions.py
- [[PermissionLevel_1]] - code - gateway/proxy/mcp_permissions.py
- [[PermissionLevel]] - code - gateway/proxy/mcp_config.py
- [[PrivateAccessAttempt]] - code - gateway/proxy/mcp_permissions.py
- [[PrivateRedactionEvent]] - code - gateway/proxy/mcp_permissions.py
- [[RateLimitEntry]] - code - gateway/proxy/mcp_permissions.py
- [[Record blocked private-tool access attempts for SOCaudit views.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Result of permission check.]] - rationale - gateway/security/rbac.py
- [[Run all permission checks in order. Returns first failure or final success.]] - rationale - gateway/proxy/mcp_permissions.py
- [[TestRateLimiting_2]] - code - gateway/tests/test_mcp_permissions.py
- [[Track rate limit state for a tool+agent combo.]] - rationale - gateway/proxy/mcp_permissions.py
- [[__init__.py_7]] - code - gateway/proxy/__init__.py
- [[config()_2]] - code - gateway/tests/test_mcp_permissions.py
- [[config()_3]] - code - gateway/tests/test_mcp_proxy.py
- [[mcp_audit.py]] - code - gateway/proxy/mcp_audit.py
- [[mcp_config.py]] - code - gateway/proxy/mcp_config.py
- [[mcp_inspector.py]] - code - gateway/proxy/mcp_inspector.py
- [[mcp_permissions.py]] - code - gateway/proxy/mcp_permissions.py
- [[mcp_proxy.py]] - code - gateway/proxy/mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GitGuard
SORT file.name ASC
```

## Connections to other communities
- 82 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 75 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py]]
- 43 edges to [[_COMMUNITY_asyncio]]
- 19 edges to [[_COMMUNITY_TestParanoidConfig]]
- 9 edges to [[_COMMUNITY_brand-guidelines]]
- 9 edges to [[_COMMUNITY_MiddlewareManager]]
- 7 edges to [[_COMMUNITY_AgentShroud v0.9.0 — Human Interface Testing Gui]]
- 4 edges to [[_COMMUNITY_EncryptedStore]]
- 4 edges to [[_COMMUNITY__wrap_response()]]
- 4 edges to [[_COMMUNITY_Safe Refactor Specialist]]
- 3 edges to [[_COMMUNITY_Operating Rules (Non-Negotiable)]]
- 3 edges to [[_COMMUNITY_NetworkSecurityFinding]]
- 3 edges to [[_COMMUNITY_v0.9.0 Sentinel — Data Isolation + SOC + Remed]]
- 3 edges to [[_COMMUNITY_→ {site site1, test_mode True, output_p]]
- 3 edges to [[_COMMUNITY_Vulcan — Subject Matter Auditor]]
- 3 edges to [[_COMMUNITY_Steps]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_TestAlertDispatcher]]
- 1 edge to [[_COMMUNITY_TestCollaboratorPromptClassifiers]]
- 1 edge to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_EgressPolicy]]
- 1 edge to [[_COMMUNITY_AuditStore]]
- 1 edge to [[_COMMUNITY_chatbotmain.py]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_ModeRequest]]

## Top bridge nodes
- [[MCPProxyConfig]] - degree 88, connects to 14 communities
- [[mcp_proxy.py]] - degree 27, connects to 13 communities
- [[MCPServerConfig]] - degree 90, connects to 12 communities
- [[PermissionLevel]] - degree 71, connects to 11 communities
- [[__init__.py_7]] - degree 23, connects to 7 communities