---
source_file: "gateway/security/dns_filter.py"
type: "rationale"
community: "URLAnalyzer"
location: "L182"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/URLAnalyzer
---

# Resolve domain to an IP and cache it for 5 minutes.

## Connections
- [[.resolve_and_cache()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/URLAnalyzer