---
type: community
cohesion: 0.29
members: 7
---

# test-sunday-upgrade-scan.sh

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[Allowlisted domains (api.openai.com, api.anthropic.com, api.telegram.org, .github.com, etc)]] - concept - docs/diagrams/images/diagram-13-network-security-egress.svg
- [[Blocked (403 Forbidden) — all other domains + RFC1918]] - concept - docs/diagrams/images/diagram-13-network-security-egress.svg
- [[Bot makes outbound request (any HTTPS connection)]] - concept - docs/diagrams/images/diagram-13-network-security-egress.svg
- [[Connection logged (timestamp, domain, allowedblocked, count)]] - concept - docs/diagrams/images/diagram-13-network-security-egress.svg
- [[Domain allowlisted (agentshroud.yaml proxy.allowed_domains)]] - concept - docs/diagrams/images/diagram-13-network-security-egress.svg
- [[HTTP CONNECT tunnel to gateway8181]] - concept - docs/diagrams/images/diagram-13-network-security-egress.svg
- [[HTTP_PROXY set (httpgateway8181)]] - concept - docs/diagrams/images/diagram-13-network-security-egress.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test-sunday-upgrade-scansh
SORT file.name ASC
```
