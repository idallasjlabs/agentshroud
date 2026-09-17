---
source_file: "gateway/security/xml_leak_filter.py"
type: "code"
community: "lifespan.py"
location: "L47"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/lifespanpy
---

# XMLLeakFilter

## Connections
- [[.__init__()_12]] - `calls` [EXTRACTED]
- [[.__init__()_131]] - `method` [EXTRACTED]
- [[.filter_function_calls_only()]] - `method` [EXTRACTED]
- [[.filter_response()]] - `method` [EXTRACTED]
- [[.scan_command_injection()]] - `method` [EXTRACTED]
- [[.setup_method()_29]] - `calls` [EXTRACTED]
- [[.xml_filter()]] - `calls` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_2]] - `uses` [INFERRED]
- [[Exception_1]] - `uses` [INFERRED]
- [[Filter to remove sensitive XML and path information from outbound responses.]] - `rationale_for` [EXTRACTED]
- [[FilterResult_1]] - `references` [EXTRACTED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[TestCommandInjectionScan]] - `uses` [INFERRED]
- [[TestXMLLeakFilter]] - `uses` [INFERRED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[run()_4]] - `calls` [EXTRACTED]
- [[test_xml_leak_filter.py]] - `imports` [EXTRACTED]
- [[xml_leak_filter.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/lifespanpy