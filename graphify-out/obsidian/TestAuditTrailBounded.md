---
source_file: "gateway/tests/test_mcp_proxy.py"
type: "code"
community: "MCPAuditTrail"
location: "L351"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/MCPAuditTrail
---

# TestAuditTrailBounded

## Connections
- [[.test_default_window_is_10k()_1]] - `method` [EXTRACTED]
- [[.test_report_total_reflects_all_appended()]] - `method` [EXTRACTED]
- [[.test_tamper_in_retained_window_detected()_1]] - `method` [EXTRACTED]
- [[.test_verify_chain_valid_after_wrap()_1]] - `method` [EXTRACTED]
- [[.test_window_capped_at_max_entries()_1]] - `method` [EXTRACTED]
- [[FindingType]] - `uses` [INFERRED]
- [[In-memory MCP audit window must be bounded (mirrors AuditChain).]] - `rationale_for` [EXTRACTED]
- [[MCPAuditTrail_1]] - `uses` [INFERRED]
- [[MCPInspector_1]] - `uses` [INFERRED]
- [[MCPPermissionManager]] - `uses` [INFERRED]
- [[MCPProxy_1]] - `uses` [INFERRED]
- [[MCPProxyConfig_2]] - `uses` [INFERRED]
- [[MCPServerConfig_2]] - `uses` [INFERRED]
- [[MCPToolCall_1]] - `uses` [INFERRED]
- [[MCPToolConfig]] - `uses` [INFERRED]
- [[MCPToolResult]] - `uses` [INFERRED]
- [[MCPTransport]] - `uses` [INFERRED]
- [[PermissionLevel_1]] - `uses` [INFERRED]
- [[ThreatLevel_2]] - `uses` [INFERRED]
- [[test_mcp_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/MCPAuditTrail