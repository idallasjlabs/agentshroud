---
source_file: "gateway/proxy/url_analyzer.py"
type: "rationale"
community: "ToolResultSanitizer"
location: "L217"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ToolResultSanitizer
---

# Check if hostname is a private/reserved address (SSRF attempt).

## Connections
- [[._is_ssrf()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ToolResultSanitizer