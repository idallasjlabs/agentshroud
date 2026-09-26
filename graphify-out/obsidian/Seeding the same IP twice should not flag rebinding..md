---
source_file: "gateway/tests/test_dns_filter.py"
type: "rationale"
community: "URLAnalyzer"
location: "L218"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/URLAnalyzer
---

# Seeding the same IP twice should not flag rebinding.

## Connections
- [[.test_stable_resolution_passes()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/URLAnalyzer