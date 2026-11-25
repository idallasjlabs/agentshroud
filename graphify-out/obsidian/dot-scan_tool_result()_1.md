---
source_file: "gateway/security/tool_result_injection.py"
type: "code"
community: "ToolResultInjectionScanner"
location: "L245"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ToolResultInjectionScanner
---

# .scan_tool_result()

## Connections
- [[dot-_detect_encoded_injection()]] - `calls` [EXTRACTED]
- [[dot-_detect_unicode_obfuscation()]] - `calls` [EXTRACTED]
- [[InjectionResult]] - `calls` [EXTRACTED]
- [[Scan tool result content for injection attempts. Args tool_name Name of the…]] - `rationale_for` [EXTRACTED]
- [[ToolResultInjectionScanner]] - `method` [EXTRACTED]
- [[normalize_input()]] - `calls` [EXTRACTED]
- [[strip_markdown_exfil()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ToolResultInjectionScanner
