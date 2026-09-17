---
source_file: "gateway/security/scanner_integration.py"
type: "rationale"
community: "scanner_integration.py"
location: "L412"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scanner_integrationpy
---

# Return True if running inside a Docker container (/.dockerenv present).

## Connections
- [[_is_containerized()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scanner_integrationpy