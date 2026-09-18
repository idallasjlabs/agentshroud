---
source_file: "gateway/security/tool_chain_analyzer.py"
type: "rationale"
community: ".analyze_tool_call()"
location: "L588"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/analyze_tool_call
---

# Scan tool parameters for injection payloads and return sanitized copy.

## Connections
- [[.sanitize_tool_params()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/analyze_tool_call