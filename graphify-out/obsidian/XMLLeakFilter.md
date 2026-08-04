---
source_file: "gateway/security/xml_leak_filter.py"
type: "code"
community: "RBAC Middleware & Ingest API"
location: "L47"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/RBAC_Middleware__Ingest_API
---

# XMLLeakFilter

## Connections
- [[.__init__()_8]] - `calls` [EXTRACTED]
- [[.__init__()_102]] - `method` [EXTRACTED]
- [[.filter_function_calls_only()]] - `method` [EXTRACTED]
- [[.filter_response()_2]] - `method` [EXTRACTED]
- [[.scan_command_injection()]] - `method` [EXTRACTED]
- [[.setup_method()_35]] - `calls` [EXTRACTED]
- [[.xml_filter()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_6]] - `uses` [INFERRED]
- [[Filter to remove sensitive XML and path information from outbound responses.]] - `rationale_for` [EXTRACTED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[TestCommandInjectionScan]] - `uses` [INFERRED]
- [[TestXMLLeakFilter]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[run()]] - `calls` [EXTRACTED]
- [[test_xml_leak_filter.py]] - `imports` [EXTRACTED]
- [[xml_leak_filter.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/RBAC_Middleware__Ingest_API
