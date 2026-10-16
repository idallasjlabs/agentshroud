---
source_file: "gateway/security/input_normalizer.py"
type: "rationale"
community: ".analyze_message"
location: "L111"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/analyze_message
---

# Strip potentially malicious markdown from tool results.      Removes:     - Mark

## Connections
- [[strip_markdown_exfil()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/analyze_message
