---
type: community
members: 18
---

# AgentShroud Development Roadmap — 2026 Gantt Chart (2)

**Members:** 18 nodes

## Members
- [[1Password Cloud]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg
- [[1Password op-proxy (POST credentialsop-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)]] - concept - docs/diagrams/images/diagram-12-credential-flow.png
- [[Bot Container (starts with ZERO 1Password access)]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg
- [[Bot Environment (secrets live only in container memory as env vars; never written to disk, never logged)]] - image - docs/diagrams/images/diagram-12-credential-flow.png
- [[Credential Flow Sequence Diagram (1Password op-proxy)]] - image - docs/diagrams/images/diagram-12-credential-flow.png
- [[Current Status_8]] - document - docs/integrations/README.md
- [[Gateway Container (has service account)]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg
- [[Incident Response Severity Flowchart]] - image - docs/diagrams/images/diagram-19-incident-response.png
- [[Integrations Documentation]] - document - docs/integrations/README.md
- [[Network Security  Egress Control Flowchart]] - image - docs/diagrams/images/diagram-13-network-security-egress.png
- [[POST credentialsop-proxy endpoint]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg
- [[Planned Documents_5]] - document - docs/integrations/README.md
- [[Runbook branch Container crash loop → docker logs → config invalid  op-proxy failed  OOM  Node.js error]] - image - docs/diagrams/images/diagram-18-runbook.png
- [[Runbook branch Security alert → review blocked_domainHIGH threat entries → legitimate action allowlist vs kill switch]] - image - docs/diagrams/images/diagram-18-runbook.png
- [[Severity matrix P1 Critical  P2 High  P3 Medium  P4 Low, with owners and response windows]] - image - docs/diagrams/images/diagram-19-incident-response.png
- [[Troubleshooting Runbook Decision Tree]] - image - docs/diagrams/images/diagram-18-runbook.png
- [[integrationsREADME]] - document - docs/integrations/README.md
- [[op_proxy_read_with_retry() (cascading retries 5s,10s,15s,30s,60s)]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Development_Roadmap__2026_Gantt_Chart_2
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_AgentShroud Development Roadmap — 2026 Gantt Chart (3)]]
- 4 edges to [[_COMMUNITY_AgentShroud Gateway (Trust Zone 1) holds 1Password service account, enforces policy, signs ledger entries, controls approval queue, HMACJWT validation]]
- 3 edges to [[_COMMUNITY_AgentShroud Development Roadmap — 2026 Gantt Chart]]
- 1 edge to [[_COMMUNITY_AgentShroud Gateway (Trust Zone 1) holds 1Password service account, enforces policy, signs ledger entries, controls approval queue, HMACJWT validation (2)]]

## Top bridge nodes
- [[1Password op-proxy (POST credentialsop-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)]] - degree 11, connects to 4 communities
- [[Runbook branch Security alert → review blocked_domainHIGH threat entries → legitimate action allowlist vs kill switch]] - degree 3, connects to 2 communities
- [[Troubleshooting Runbook Decision Tree]] - degree 5, connects to 1 community
- [[Severity matrix P1 Critical  P2 High  P3 Medium  P4 Low, with owners and response windows]] - degree 4, connects to 1 community
- [[Incident Response Severity Flowchart]] - degree 2, connects to 1 community
