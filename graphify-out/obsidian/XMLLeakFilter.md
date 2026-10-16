---
source_file: "gateway/security/xml_leak_filter.py"
type: "code"
community: "MiddlewareManager"
location: "L47"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/MiddlewareManager
---

# XMLLeakFilter

## Connections
- [[dot-__init__()_162]] - `calls` [EXTRACTED]
- [[dot-__init__()_169]] - `method` [EXTRACTED]
- [[dot-filter_function_calls_only()]] - `method` [EXTRACTED]
- [[dot-filter_response()_1]] - `method` [EXTRACTED]
- [[dot-scan_command_injection()]] - `method` [EXTRACTED]
- [[dot-setup_method()_23]] - `calls` [EXTRACTED]
- [[dot-xml_filter()]] - `calls` [EXTRACTED]
- [[Action_3]] - `uses` [INFERRED]
- [[Any_63]] - `uses` [INFERRED]
- [[Exception_3]] - `uses` [INFERRED]
- [[Filter to remove sensitive XML and path information from outbound responses.]] - `rationale_for` [EXTRACTED]
- [[FilterResult]] - `references` [EXTRACTED]
- [[LogSanitizer_1]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager_2]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[TestCommandInjectionScan]] - `uses` [INFERRED]
- [[TestXMLLeakFilter]] - `uses` [INFERRED]
- [[ToolTier_1]] - `uses` [INFERRED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[middleware.py_1]] - `imports` [EXTRACTED]
- [[run()_4]] - `calls` [EXTRACTED]
- [[test_xml_leak_filter.py]] - `imports` [EXTRACTED]
- [[xml_leak_filter.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/MiddlewareManager
