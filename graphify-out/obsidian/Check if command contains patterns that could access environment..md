---
source_file: "gateway/security/env_guard.py"
type: "rationale"
community: "._record_leakage()"
location: "L201"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_record_leakage
---

# Check if command contains patterns that could access environment.

## Connections
- [[dot-_contains_env_access_patterns()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_record_leakage
