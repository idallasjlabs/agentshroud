---
source_file: "scripts/migrate-cve-registry-ghsa.py"
type: "rationale"
community: "migrate-cve-registry-ghsa.py"
location: "L369"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/migrate-cve-registry-ghsapy
---

# Rewrite every ``"id": "<old>"`` line and set ghsa_id/cve_id right after it.

## Connections
- [[rewrite_registry_text()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/migrate-cve-registry-ghsapy