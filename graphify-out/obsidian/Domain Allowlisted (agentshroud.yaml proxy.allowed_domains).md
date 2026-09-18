---
source_file: "docs/diagrams/images/diagram-13-network-security-egress.svg"
type: "concept"
community: "Domain allowlisted? (agentshroud.yaml proxy.allo"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Domain_allowlisted_agentshroudyaml_proxyallo
---

# Domain allowlisted? (agentshroud.yaml proxy.allowed_domains)

## Connections
- [[Allowlisted domains (api.openai.com, api.anthropic.com, api.telegram.org, .github.com, etc)]] - `shares_data_with` [EXTRACTED]
- [[Blocked (403 Forbidden) — all other domains + RFC1918]] - `calls` [EXTRACTED]
- [[HTTP CONNECT tunnel to gateway8181]] - `calls` [EXTRACTED]
- [[HTTP_PROXY set (httpgateway8181)]] - `calls` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Domain_allowlisted_agentshroudyaml_proxyallo