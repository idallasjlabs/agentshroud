---
source_file: "gateway/security/tool_result_injection.py"
type: "code"
community: "InjectionSeverity"
location: "L24"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/InjectionSeverity
---

# InjectionSeverity

## Connections
- [[._detect_encoded_injection()]] - `references` [EXTRACTED]
- [[._detect_unicode_obfuscation()]] - `references` [EXTRACTED]
- [[Enum_3]] - `inherits` [EXTRACTED]
- [[TestCleanContent]] - `uses` [INFERRED]
- [[TestEncodedInjection]] - `uses` [INFERRED]
- [[TestHighSeverity]] - `uses` [INFERRED]
- [[TestMediumSeverity]] - `uses` [INFERRED]
- [[TestSanitization]] - `uses` [INFERRED]
- [[TestToolResultInjectionScanner]] - `uses` [INFERRED]
- [[TestUnicodeObfuscation]] - `uses` [INFERRED]
- [[str_2]] - `inherits` [EXTRACTED]
- [[test_tool_injection_scan.py]] - `imports` [EXTRACTED]
- [[test_tool_result_injection.py]] - `imports` [EXTRACTED]
- [[tool_result_injection.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/InjectionSeverity