---
source_file: "gateway/security/audit_export.py"
type: "code"
community: "Audit Export Pipeline"
location: "L62"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Audit_Export_Pipeline
---

# AuditExporter

## Connections
- [[.__init__()_53]] - `method` [EXTRACTED]
- [[._export_cef()]] - `method` [EXTRACTED]
- [[._export_json()]] - `method` [EXTRACTED]
- [[._export_jsonld()]] - `method` [EXTRACTED]
- [[._parse_cef_for_verification()]] - `method` [EXTRACTED]
- [[.export_events()]] - `method` [EXTRACTED]
- [[.test_export_cef()]] - `calls` [EXTRACTED]
- [[.test_export_filtering()]] - `calls` [EXTRACTED]
- [[.test_export_json()]] - `calls` [EXTRACTED]
- [[.test_export_json_ld()]] - `calls` [EXTRACTED]
- [[.test_tamper_detection()]] - `calls` [EXTRACTED]
- [[.test_verify_export_integrity()]] - `calls` [EXTRACTED]
- [[.verify_export_integrity()]] - `method` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_10]] - `uses` [INFERRED]
- [[AuditEvent_1]] - `uses` [INFERRED]
- [[AuditStore_1]] - `uses` [INFERRED]
- [[AuthRequired_1]] - `uses` [INFERRED]
- [[Exception_1]] - `uses` [INFERRED]
- [[Exports audit events in various compliance formats.]] - `rationale_for` [EXTRACTED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MCPProxyRequest]] - `uses` [INFERRED]
- [[MCPResultRequest]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[OpProxyRequest]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Request_3]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[SSHExecRequest_1]] - `uses` [INFERRED]
- [[SSHWriteFileRequest_1]] - `uses` [INFERRED]
- [[TestAuditEvent]] - `uses` [INFERRED]
- [[TestAuditExporter]] - `uses` [INFERRED]
- [[TestAuditStore]] - `uses` [INFERRED]
- [[TestAuditStoreBotId]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[WebSocket_3]] - `uses` [INFERRED]
- [[audit_export.py]] - `contains` [EXTRACTED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[soc_export()]] - `calls` [EXTRACTED]
- [[test_audit_export.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Audit_Export_Pipeline