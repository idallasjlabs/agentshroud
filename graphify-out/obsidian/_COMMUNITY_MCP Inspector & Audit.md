---
type: community
cohesion: 0.04
members: 71
---

# MCP Inspector & Audit

**Cohesion:** 0.04 - loosely connected
**Members:** 71 nodes

## Members
- [[._record_private_access_attempt()]] - code - gateway/proxy/mcp_permissions.py
- [[._redact_pii()]] - code - gateway/proxy/mcp_inspector.py
- [[._scan_text()]] - code - gateway/proxy/mcp_inspector.py
- [[._scan_value()]] - code - gateway/proxy/mcp_inspector.py
- [[._should_block()]] - code - gateway/proxy/mcp_inspector.py
- [[.check_agent_server_access()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_all()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_rate_limit()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_tool_parameters()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_tool_permission()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_trust_level()]] - code - gateway/proxy/mcp_permissions.py
- [[.has_findings()]] - code - gateway/proxy/mcp_inspector.py
- [[.highest_threat()]] - code - gateway/proxy/mcp_inspector.py
- [[.inspect_tool_call()]] - code - gateway/proxy/mcp_inspector.py
- [[.inspect_tool_result()]] - code - gateway/proxy/mcp_inspector.py
- [[.test_blocked_entries()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_failed_entries()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_filter_by_agent()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_filter_by_server()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_filter_by_tool()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_from_dict_basic()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_from_dict_defaults()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_from_dict_http_transport()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_generate_report()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_heavy_url_encoding_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_highest_threat_high()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_highest_threat_none()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_inspection_result_threat_level()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_large_base64_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_small_base64_ok()]] - code - gateway/tests/test_mcp_proxy.py
- [[A single finding from inspection.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Any_14]] - code - gateway/proxy/mcp_inspector.py
- [[Audit signal for blocked admin-private tool access attempts.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Block non-owner tool calls that reference admin-private data pathscontent.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check and update rate limits for a tool call.          Returns allowed=True and]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can access a server at all.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can call a specific tool.          Default-allow only blocks]] - rationale - gateway/proxy/mcp_permissions.py
- [[Decide whether to block based on findings and mode.]] - rationale - gateway/proxy/mcp_inspector.py
- [[FindingType]] - code - gateway/proxy/mcp_inspector.py
- [[Get trust level, defaulting to 1 (write) for unknown agents.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Inspect a tool result for PII and encoding issues.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Inspect an outgoing tool call for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[InspectionFinding]] - code - gateway/proxy/mcp_inspector.py
- [[InspectionResult]] - code - gateway/proxy/mcp_inspector.py
- [[PermissionCheck]] - code - gateway/proxy/mcp_permissions.py
- [[PrivateAccessAttempt]] - code - gateway/proxy/mcp_permissions.py
- [[ProxyResult]] - code - gateway/proxy/mcp_proxy.py
- [[RateLimitEntry]] - code - gateway/proxy/mcp_permissions.py
- [[Record blocked private-tool access attempts for SOCaudit views.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Recursively redact HIGH-severity PII from a value.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Recursively scan a value, appending findings in-place.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Result of a permission check.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Result of inspecting a tool call or response.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Result of proxying an MCP tool call.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Return the highest threat level from all findings.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Run all permission checks in order. Returns first failure or final success.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Scan a single string for all threat types.]] - rationale - gateway/proxy/mcp_inspector.py
- [[TestAuditQueries]] - code - gateway/tests/test_mcp_proxy.py
- [[TestConfigParsing]] - code - gateway/tests/test_mcp_proxy.py
- [[TestSuspiciousEncoding]] - code - gateway/tests/test_mcp_proxy.py
- [[TestThreatLevelCalc]] - code - gateway/tests/test_mcp_proxy.py
- [[Threat level classification.]] - rationale - gateway/proxy/mcp_inspector.py
- [[ThreatLevel]] - code - gateway/proxy/mcp_inspector.py
- [[Track rate limit state for a tool+agent combo.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Type of security finding.]] - rationale - gateway/proxy/mcp_inspector.py
- [[__init__.py_6]] - code - gateway/proxy/__init__.py
- [[mcp_audit.py]] - code - gateway/proxy/mcp_audit.py
- [[mcp_config.py]] - code - gateway/proxy/mcp_config.py
- [[mcp_inspector.py]] - code - gateway/proxy/mcp_inspector.py
- [[mcp_permissions.py]] - code - gateway/proxy/mcp_permissions.py
- [[mcp_proxy.py]] - code - gateway/proxy/mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCP_Inspector__Audit
SORT file.name ASC
```

## Connections to other communities
- 55 edges to [[_COMMUNITY_MCP Config & Proxy]]
- 36 edges to [[_COMMUNITY_Module Group 78]]
- 16 edges to [[_COMMUNITY_Module Group 154]]
- 15 edges to [[_COMMUNITY_MCP Permissions Manager]]
- 12 edges to [[_COMMUNITY_Module Group 139]]
- 10 edges to [[_COMMUNITY_Module Group 266]]
- 4 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 4 edges to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 3 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 3 edges to [[_COMMUNITY_SSH Proxy & Gateway Config]]
- 2 edges to [[_COMMUNITY_Enhanced Approval Queue]]
- 2 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 2 edges to [[_COMMUNITY_Module Group 387]]
- 2 edges to [[_COMMUNITY_Module Group 442]]
- 2 edges to [[_COMMUNITY_Module Group 468]]
- 2 edges to [[_COMMUNITY_Module Group 205]]
- 1 edge to [[_COMMUNITY_Dashboard Routes & WebSocket]]
- 1 edge to [[_COMMUNITY_Module Group 311]]
- 1 edge to [[_COMMUNITY_Module Group 232]]
- 1 edge to [[_COMMUNITY_Module Group 255]]

## Top bridge nodes
- [[mcp_proxy.py]] - degree 24, connects to 9 communities
- [[ThreatLevel]] - degree 27, connects to 8 communities
- [[FindingType]] - degree 26, connects to 8 communities
- [[ProxyResult]] - degree 17, connects to 8 communities
- [[__init__.py_6]] - degree 23, connects to 6 communities
