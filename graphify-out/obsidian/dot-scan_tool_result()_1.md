---
source_file: "gateway/security/tool_result_injection.py"
type: "code"
community: ".analyze_message"
location: "L245"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/analyze_message
---

# .scan_tool_result()

## Connections
- [[dot-_detect_encoded_injection()]] - `calls` [EXTRACTED]
- [[dot-_detect_unicode_obfuscation()]] - `calls` [EXTRACTED]
- [[InjectionResult]] - `references` [EXTRACTED]
- [[Scan tool result content for injection attempts.          Args             tool]] - `rationale_for` [EXTRACTED]
- [[ToolResultInjectionScanner]] - `method` [EXTRACTED]
- [[normalize_input()]] - `calls` [EXTRACTED]
- [[strip_markdown_exfil()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/analyze_message
