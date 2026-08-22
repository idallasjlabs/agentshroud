---
source_file: "gateway/security/input_normalizer.py"
type: "rationale"
community: "Tool Result Injection (security)"
location: "L111"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Tool_Result_Injection_security
---

# Strip potentially malicious markdown from tool results.      Removes:     - Mark

## Connections
- [[strip_markdown_exfil()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Tool_Result_Injection_security