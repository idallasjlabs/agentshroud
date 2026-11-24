---
source_file: "gateway/security/xml_leak_filter.py"
type: "code"
community: "run"
location: "L47"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/run
---

# XMLLeakFilter

## Connections
- [[dot-__init__()]] - `calls` [EXTRACTED]
- [[dot-__init__()_4]] - `method` [EXTRACTED]
- [[dot-filter_function_calls_only()]] - `method` [EXTRACTED]
- [[dot-filter_response()]] - `method` [EXTRACTED]
- [[dot-scan_command_injection()]] - `method` [EXTRACTED]
- [[dot-setup_method()_2]] - `calls` [EXTRACTED]
- [[dot-xml_filter()]] - `calls` [EXTRACTED]
- [[Filter to remove sensitive XML and path information from outbound responses.]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[TestCommandInjectionScan]] - `uses` [INFERRED]
- [[TestXMLLeakFilter]] - `uses` [INFERRED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[middleware.py_2]] - `imports` [EXTRACTED]
- [[run()]] - `calls` [EXTRACTED]
- [[test_xml_leak_filter.py]] - `imports` [EXTRACTED]
- [[xml_leak_filter.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/run
