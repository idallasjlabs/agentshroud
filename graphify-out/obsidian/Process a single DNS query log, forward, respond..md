---
source_file: "gateway/proxy/dns_forwarder.py"
type: "rationale"
community: "parse_query()"
location: "L178"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/parse_query
---

# Process a single DNS query: log, forward, respond.

## Connections
- [[._handle_query()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/parse_query