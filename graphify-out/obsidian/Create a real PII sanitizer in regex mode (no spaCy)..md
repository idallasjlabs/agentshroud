---
source_file: "gateway/tests/test_redteam_probes.py"
type: "rationale"
community: "test_agent_cve_registry.py"
location: "L31"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_agent_cve_registrypy
---

# Create a real PII sanitizer in regex mode (no spaCy).

## Connections
- [[_make_pii_sanitizer()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_agent_cve_registrypy
