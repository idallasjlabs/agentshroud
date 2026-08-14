---
source_file: "gateway/security/xml_leak_filter.py"
type: "code"
community: "Egress & RBAC Security Core"
location: "L47"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Egress__RBAC_Security_Core
---

# XMLLeakFilter

## Connections
- [[.__init__()_13]] - `calls` [EXTRACTED]
- [[.__init__()_124]] - `method` [EXTRACTED]
- [[.filter_function_calls_only()]] - `method` [EXTRACTED]
- [[.filter_response()_2]] - `method` [EXTRACTED]
- [[.scan_command_injection()]] - `method` [EXTRACTED]
- [[.setup_method()_38]] - `calls` [EXTRACTED]
- [[.xml_filter()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_8]] - `uses` [INFERRED]
- [[Exception_2]] - `uses` [INFERRED]
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
- [[run()_3]] - `calls` [EXTRACTED]
- [[test_xml_leak_filter.py]] - `imports` [EXTRACTED]
- [[xml_leak_filter.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Egress__RBAC_Security_Core