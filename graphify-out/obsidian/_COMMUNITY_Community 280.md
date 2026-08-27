---
type: community
members: 22
---

# Community 280

**Members:** 22 nodes

## Members
- [[AgentShroud Gateway (Trust Zone 1) holds 1Password service account, enforces policy, signs ledger entries, controls approval queue, HMACJWT validation]] - concept - docs/diagrams/images/diagram-11-trust-boundary.png
- [[Allowlisted domains (api.openai.com, api.anthropic.com, api.telegram.org, googleapis.com, .github.com, .githubusercontent.com, imapsmtp.mail.me.com)]] - image - docs/diagrams/images/diagram-13-network-security-egress.png
- [[BlockedUntrusted (LAN RFC1918, unlisted domains)]] - image - docs/diagrams/images/diagram-11-trust-boundary.png
- [[Containers startup order agentshroud-gateway starts first, agentshroud-bot starts after gateway healthy]] - image - docs/diagrams/images/diagram-22-dependency-graph.png
- [[Deploying AgentShroud on Linux (docsoperationslinux.md)]] - document - docs/operations/linux.md
- [[Deploying AgentShroud on macOS (docsoperationsmacos.md)]] - document - docs/operations/macos.md
- [[Docker Buildx multi-arch build (linuxamd64, linuxarm64)]] - concept - docs/operations/linux.md
- [[Docker Deployment Dependency Graph]] - image - docs/diagrams/images/diagram-22-dependency-graph.png
- [[Docker Desktop (Apple Silicon  Intel transparent arch handling; resource allocation guidance)]] - concept - docs/operations/macos.md
- [[Docker Images docker-agentshroud (node22-bookworm-slim, Dockerfile.agentshroud), docker-gateway (python3.11-slim, gatewayDockerfile)]] - image - docs/diagrams/images/diagram-22-dependency-graph.png
- [[Docker Secrets required before containers start (openai_api_key.txt, 1password_bot_ , gateway_password.txt, 1password_service_account)]] - image - docs/diagrams/images/diagram-22-dependency-graph.png
- [[Docker Volumes (auto-created) agentshroud-config, agentshroud-workspace, agentshroud-ssh, gateway-data]] - image - docs/diagrams/images/diagram-22-dependency-graph.png
- [[External Dependencies (no deploy) 1Password Cloud, OpenAIAnthropicTelegram APIs, Tailscale Network via SSH]] - image - docs/diagrams/images/diagram-22-dependency-graph.png
- [[HTTP CONNECT egress proxy (gateway8181; domain allowlist via agentshroud.yaml proxy.allowed_domains; blocks RFC1918 + unlisted domains; logs connections)]] - concept - docs/diagrams/images/diagram-13-network-security-egress.png
- [[Native Python gateway dev run uvicorn gateway.ingest_api.mainapp --host 127.0.0.1 --port 8080]] - concept - docs/operations/macos.md
- [[Trust Boundary Diagram]] - concept - docs/diagrams/04-security.md
- [[Trust Zone 0 — Owner (Isaiah Jefferson approvereject, gateway admin, container restart, secret rotation)]] - image - docs/diagrams/images/diagram-11-trust-boundary.png
- [[Trust Zone 2 — Bot (Supervised Agent no direct credentialinternet access)]] - image - docs/diagrams/images/diagram-11-trust-boundary.png
- [[Trust Zone 3 — External Services (OpenAI, Anthropic, Telegram, GitHub, 1Password; allowlisted HTTPS only)]] - image - docs/diagrams/images/diagram-11-trust-boundary.png
- [[Trust Zone 4 — Infrastructure Nodes (raspberrypi, marvin, trillian; SSH-gated)]] - image - docs/diagrams/images/diagram-11-trust-boundary.png
- [[dockersecretssetup-secrets.sh (secret bootstrap step shared by Linux and macOS install guides)]] - concept - docs/operations/linux.md
- [[systemd service etcsystemdsystemagentshroud.service for auto-start]] - concept - docs/operations/linux.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_280
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Community 320]]
- 1 edge to [[_COMMUNITY_Community 745]]
- 1 edge to [[_COMMUNITY_Community 702]]
- 1 edge to [[_COMMUNITY_Community 1528]]
- 1 edge to [[_COMMUNITY_Community 353]]

## Top bridge nodes
- [[HTTP CONNECT egress proxy (gateway8181; domain allowlist via agentshroud.yaml proxy.allowed_domains; blocks RFC1918 + unlisted domains; logs connections)]] - degree 7, connects to 3 communities
- [[Trust Boundary Diagram]] - degree 8, connects to 2 communities
- [[AgentShroud Gateway (Trust Zone 1) holds 1Password service account, enforces policy, signs ledger entries, controls approval queue, HMACJWT validation]] - degree 10, connects to 1 community
- [[Trust Zone 2 — Bot (Supervised Agent no direct credentialinternet access)]] - degree 5, connects to 1 community
- [[Docker Secrets required before containers start (openai_api_key.txt, 1password_bot_ , gateway_password.txt, 1password_service_account)]] - degree 3, connects to 1 community