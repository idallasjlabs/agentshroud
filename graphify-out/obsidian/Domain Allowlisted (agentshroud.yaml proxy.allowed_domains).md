---
source_file: "docs/diagrams/images/diagram-13-network-security-egress.svg"
type: "concept"
community: "test-sunday-upgrade-scan.sh"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/test-sunday-upgrade-scansh
---

# Domain allowlisted? (agentshroud.yaml proxy.allowed_domains)

## Connections
- [[Allowlisted domains (api.openai.com, api.anthropic.com, api.telegram.org, .github.com, etc)]] - `shares_data_with` [EXTRACTED]
- [[Blocked (403 Forbidden) — all other domains + RFC1918]] - `calls` [EXTRACTED]
- [[HTTP CONNECT tunnel to gateway8181]] - `calls` [EXTRACTED]
- [[HTTP_PROXY set (httpgateway8181)]] - `calls` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/test-sunday-upgrade-scansh