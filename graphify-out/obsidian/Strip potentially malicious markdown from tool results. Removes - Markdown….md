---
source_file: "gateway/security/input_normalizer.py"
type: "rationale"
community: "ToolResultInjectionScanner"
location: "L111"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ToolResultInjectionScanner
---

# Strip potentially malicious markdown from tool results. Removes: - Markdown…

## Connections
- [[strip_markdown_exfil()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ToolResultInjectionScanner
