---
source_file: "gateway/security/egress_filter.py"
type: "rationale"
community: "EgressAttempt"
location: "L460"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/EgressAttempt
---

# Check if host is a private, loopback, link-local, or reserved IP.          Cover

## Connections
- [[dot-_is_private_ip()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/EgressAttempt
