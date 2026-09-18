---
source_file: "gateway/tests/test_tool_injection_scan.py"
type: "code"
community: "InjectionSeverity"
location: "L20"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/InjectionSeverity
---

# TestToolResultInjectionScanner

## Connections
- [[.setup_method()_3]] - `method` [EXTRACTED]
- [[.test_base64_encoded_injection()]] - `method` [EXTRACTED]
- [[.test_clean_content_passes_through()]] - `method` [EXTRACTED]
- [[.test_ignore_instructions_injection_high_severity()]] - `method` [EXTRACTED]
- [[.test_xml_function_injection_detection()]] - `method` [EXTRACTED]
- [[InjectionAction]] - `uses` [INFERRED]
- [[InjectionSeverity]] - `uses` [INFERRED]
- [[Test cases for ToolResultInjectionScanner.]] - `rationale_for` [EXTRACTED]
- [[ToolResultInjectionScanner]] - `uses` [INFERRED]
- [[test_tool_injection_scan.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/InjectionSeverity