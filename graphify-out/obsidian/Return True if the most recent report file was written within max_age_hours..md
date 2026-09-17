---
source_file: "gateway/security/scanner_integration.py"
type: "rationale"
community: "test_scorecard_integrity.py"
location: "L322"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_scorecard_integritypy
---

# Return True if the most recent report file was written within max_age_hours.

## Connections
- [[_is_fresh()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_scorecard_integritypy