---
type: community
cohesion: 0.09
members: 33
---

# Community 225

**Cohesion:** 0.09 - loosely connected
**Members:** 33 nodes

## Members
- [[1Password Cloud]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg
- [[1Password op-proxy (POST credentialsop-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)]] - concept - docs/diagrams/images/diagram-12-credential-flow.png
- [[AgentShroud Gateway (Trust Zone 1) holds 1Password service account, enforces policy, signs ledger entries, controls approval queue, HMACJWT validation]] - concept - docs/diagrams/images/diagram-11-trust-boundary.png
- [[Allowlisted domains (api.openai.com, api.anthropic.com, api.telegram.org, googleapis.com, .github.com, .githubusercontent.com, imapsmtp.mail.me.com)]] - image - docs/diagrams/images/diagram-13-network-security-egress.png
- [[BlockedUntrusted (LAN RFC1918, unlisted domains)]] - image - docs/diagrams/images/diagram-11-trust-boundary.png
- [[Bot Container (starts with ZERO 1Password access)]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg
- [[Bot Environment (secrets live only in container memory as env vars; never written to disk, never logged)]] - image - docs/diagrams/images/diagram-12-credential-flow.png
- [[Containers startup order agentshroud-gateway starts first, agentshroud-bot starts after gateway healthy]] - image - docs/diagrams/images/diagram-22-dependency-graph.png
- [[Credential Flow Sequence Diagram (1Password op-proxy)]] - image - docs/diagrams/images/diagram-12-credential-flow.png
- [[Current Status_6]] - document - docs/integrations/README.md
- [[Docker Deployment Dependency Graph]] - image - docs/diagrams/images/diagram-22-dependency-graph.png
- [[Docker Images docker-agentshroud (node22-bookworm-slim, Dockerfile.agentshroud), docker-gateway (python3.11-slim, gatewayDockerfile)]] - image - docs/diagrams/images/diagram-22-dependency-graph.png
- [[Docker Secrets required before containers start (openai_api_key.txt, 1password_bot_ , gateway_password.txt, 1password_service_account)]] - image - docs/diagrams/images/diagram-22-dependency-graph.png
- [[Docker Volumes (auto-created) agentshroud-config, agentshroud-workspace, agentshroud-ssh, gateway-data]] - image - docs/diagrams/images/diagram-22-dependency-graph.png
- [[External Dependencies (no deploy) 1Password Cloud, OpenAIAnthropicTelegram APIs, Tailscale Network via SSH]] - image - docs/diagrams/images/diagram-22-dependency-graph.png
- [[Gateway Container (has service account)]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg
- [[HTTP CONNECT egress proxy (gateway8181; domain allowlist via agentshroud.yaml proxy.allowed_domains; blocks RFC1918 + unlisted domains; logs connections)]] - concept - docs/diagrams/images/diagram-13-network-security-egress.png
- [[Incident Response Severity Flowchart]] - image - docs/diagrams/images/diagram-19-incident-response.png
- [[Integrations Documentation]] - document - docs/integrations/README.md
- [[Network Security  Egress Control Flowchart]] - image - docs/diagrams/images/diagram-13-network-security-egress.png
- [[POST credentialsop-proxy endpoint]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg
- [[Planned Documents_5]] - document - docs/integrations/README.md
- [[Runbook branch Container crash loop → docker logs → config invalid  op-proxy failed  OOM  Node.js error]] - image - docs/diagrams/images/diagram-18-runbook.png
- [[Runbook branch Security alert → review blocked_domainHIGH threat entries → legitimate action allowlist vs kill switch]] - image - docs/diagrams/images/diagram-18-runbook.png
- [[Severity matrix P1 Critical  P2 High  P3 Medium  P4 Low, with owners and response windows]] - image - docs/diagrams/images/diagram-19-incident-response.png
- [[Troubleshooting Runbook Decision Tree]] - image - docs/diagrams/images/diagram-18-runbook.png
- [[Trust Boundary Diagram]] - concept - docs/diagrams/04-security.md
- [[Trust Zone 0 — Owner (Isaiah Jefferson approvereject, gateway admin, container restart, secret rotation)]] - image - docs/diagrams/images/diagram-11-trust-boundary.png
- [[Trust Zone 2 — Bot (Supervised Agent no direct credentialinternet access)]] - image - docs/diagrams/images/diagram-11-trust-boundary.png
- [[Trust Zone 3 — External Services (OpenAI, Anthropic, Telegram, GitHub, 1Password; allowlisted HTTPS only)]] - image - docs/diagrams/images/diagram-11-trust-boundary.png
- [[Trust Zone 4 — Infrastructure Nodes (raspberrypi, marvin, trillian; SSH-gated)]] - image - docs/diagrams/images/diagram-11-trust-boundary.png
- [[integrationsREADME]] - document - docs/integrations/README.md
- [[op_proxy_read_with_retry() (cascading retries 5s,10s,15s,30s,60s)]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_225
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Community 184]]
- 2 edges to [[_COMMUNITY_Community 1078]]
- 1 edge to [[_COMMUNITY_Community 451]]
- 1 edge to [[_COMMUNITY_Community 728]]

## Top bridge nodes
- [[Trust Boundary Diagram]] - degree 8, connects to 2 communities
- [[1Password op-proxy (POST credentialsop-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)]] - degree 11, connects to 1 community
- [[AgentShroud Gateway (Trust Zone 1) holds 1Password service account, enforces policy, signs ledger entries, controls approval queue, HMACJWT validation]] - degree 10, connects to 1 community
- [[HTTP CONNECT egress proxy (gateway8181; domain allowlist via agentshroud.yaml proxy.allowed_domains; blocks RFC1918 + unlisted domains; logs connections)]] - degree 7, connects to 1 community
- [[Troubleshooting Runbook Decision Tree]] - degree 5, connects to 1 community