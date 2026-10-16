---
type: community
cohesion: 0.53
members: 6
---

# Containers startup order: agentshroud-gateway starts first, agentshroud-bot starts after gateway healthy

**Cohesion:** 0.53 - moderately connected
**Members:** 6 nodes

## Members
- [[Containers startup order agentshroud-gateway starts first, agentshroud-bot starts after gateway healthy]] - image - docs/diagrams/images/diagram-22-dependency-graph.png
- [[Docker Deployment Dependency Graph]] - image - docs/diagrams/images/diagram-22-dependency-graph.png
- [[Docker Images docker-agentshroud (node22-bookworm-slim, Dockerfile.agentshroud), docker-gateway (python3.11-slim, gatewayDockerfile)]] - image - docs/diagrams/images/diagram-22-dependency-graph.png
- [[Docker Secrets required before containers start (openai_api_key.txt, 1password_bot_ , gateway_password.txt, 1password_service_account)]] - image - docs/diagrams/images/diagram-22-dependency-graph.png
- [[Docker Volumes (auto-created) agentshroud-config, agentshroud-workspace, agentshroud-ssh, gateway-data]] - image - docs/diagrams/images/diagram-22-dependency-graph.png
- [[External Dependencies (no deploy) 1Password Cloud, OpenAIAnthropicTelegram APIs, Tailscale Network via SSH]] - image - docs/diagrams/images/diagram-22-dependency-graph.png

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Containers_startup_order_agentshroud-gateway_starts_first_agentshroud-bot_starts_after_gateway_healthy
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_AgentShroud Gateway (Trust Zone 1) holds 1Password service account, enforces policy, signs ledger entries, controls approval queue, HMACJWT validation]]
- 1 edge to [[_COMMUNITY_1Password op-proxy (POST credentialsop-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)]]

## Top bridge nodes
- [[Containers startup order agentshroud-gateway starts first, agentshroud-bot starts after gateway healthy]] - degree 5, connects to 1 community
- [[Docker Secrets required before containers start (openai_api_key.txt, 1password_bot_ , gateway_password.txt, 1password_service_account)]] - degree 3, connects to 1 community
- [[External Dependencies (no deploy) 1Password Cloud, OpenAIAnthropicTelegram APIs, Tailscale Network via SSH]] - degree 3, connects to 1 community
