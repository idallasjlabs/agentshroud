---
source_file: "docs/diagrams/images/diagram-13-network-security-egress.svg"
type: "concept"
community: "test-sunday-upgrade-scan.sh"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/test-sunday-upgrade-scansh
---

# HTTP_PROXY set? (http://gateway:8181)

## Connections
- [[Bot makes outbound request (any HTTPS connection)]] - `calls` [EXTRACTED]
- [[Domain allowlisted (agentshroud.yaml proxy.allowed_domains)]] - `calls` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/test-sunday-upgrade-scansh