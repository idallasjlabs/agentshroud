---
source_file: "gateway/security/input_normalizer.py"
type: "code"
community: ".analyze_message"
location: "L110"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/analyze_message
---

# strip_markdown_exfil()

## Connections
- [[dot-_filter_outbound()_1]] - `calls` [EXTRACTED]
- [[dot-_filter_outbound_multipart()]] - `calls` [EXTRACTED]
- [[dot-scan_tool_result()_1]] - `calls` [EXTRACTED]
- [[Strip potentially malicious markdown from tool results.      Removes     - Mark]] - `rationale_for` [EXTRACTED]
- [[input_normalizer.py]] - `contains` [EXTRACTED]
- [[telegram_proxy.py_2]] - `imports` [EXTRACTED]
- [[tool_result_injection.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/analyze_message
