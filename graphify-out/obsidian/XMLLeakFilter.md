---
source_file: "gateway/security/xml_leak_filter.py"
type: "code"
community: "AlertDispatcher"
location: "L47"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AlertDispatcher
---

# XMLLeakFilter

## Connections
- [[dot-__init__()_10]] - `calls` [EXTRACTED]
- [[dot-__init__()_21]] - `method` [EXTRACTED]
- [[dot-filter_function_calls_only()]] - `method` [EXTRACTED]
- [[dot-filter_response()]] - `method` [EXTRACTED]
- [[dot-scan_command_injection()]] - `method` [EXTRACTED]
- [[dot-setup_method()_19]] - `calls` [EXTRACTED]
- [[dot-xml_filter()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any]] - `uses` [INFERRED]
- [[Exception]] - `uses` [INFERRED]
- [[Filter to remove sensitive XML and path information from outbound responses.]] - `rationale_for` [EXTRACTED]
- [[FilterResult]] - `references` [EXTRACTED]
- [[LogSanitizer_1]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[TestCommandInjectionScan]] - `uses` [INFERRED]
- [[TestXMLLeakFilter]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[run()]] - `calls` [EXTRACTED]
- [[test_xml_leak_filter.py]] - `imports` [EXTRACTED]
- [[xml_leak_filter.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AlertDispatcher
