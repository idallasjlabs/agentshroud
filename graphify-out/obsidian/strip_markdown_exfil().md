---
source_file: "gateway/security/input_normalizer.py"
type: "code"
community: ".scan()"
location: "L110"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/scan
---

# strip_markdown_exfil()

## Connections
- [[._filter_outbound()_1]] - `calls` [EXTRACTED]
- [[._filter_outbound_multipart()]] - `calls` [EXTRACTED]
- [[.scan_tool_result()_2]] - `calls` [EXTRACTED]
- [[Strip potentially malicious markdown from tool results.      Removes     - Mark]] - `rationale_for` [EXTRACTED]
- [[input_normalizer.py]] - `contains` [EXTRACTED]
- [[telegram_proxy.py]] - `imports` [EXTRACTED]
- [[tool_result_injection.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/scan