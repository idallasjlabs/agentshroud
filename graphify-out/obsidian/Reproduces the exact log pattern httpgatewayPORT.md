---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "auto_remediate_cves.py"
location: "L305"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/auto_remediate_cvespy
---

# Reproduces the exact log pattern: http://gateway:[PORT]

## Connections
- [[.test_port_inline_colon()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/auto_remediate_cvespy