---
source_file: "scripts/migrate-cve-registry-ghsa.py"
type: "rationale"
community: "scripts/migrate-cve-registry-ghsa.py"
location: "L369"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/migrate-cve-registry-ghsapy
---

# Rewrite every ``"id": "<old>"`` line and set ghsa_id/cve_id right after it.

## Connections
- [[rewrite_registry_text()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/migrate-cve-registry-ghsapy