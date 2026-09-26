---
source_file: "gateway/security/audit_store.py"
type: "rationale"
community: "load_config()"
location: "L103"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/load_config
---

# Compute SHA-256 hash of event content (excluding hashes).

## Connections
- [[.compute_content_hash()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/load_config