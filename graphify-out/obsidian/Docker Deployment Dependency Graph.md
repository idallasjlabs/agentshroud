---
source_file: "docs/diagrams/images/diagram-22-dependency-graph.png"
type: "image"
community: "Diagram 11 Trust Boundary (images)"
tags:
  - graphify/image
  - graphify/EXTRACTED
  - community/Diagram_11_Trust_Boundary_images
---

# Docker Deployment Dependency Graph

## Connections
- [[Containers startup order agentshroud-gateway starts first, agentshroud-bot starts after gateway healthy]] - `conceptually_related_to` [EXTRACTED]
- [[Docker Images docker-agentshroud (node22-bookworm-slim, Dockerfile.agentshroud), docker-gateway (python3.11-slim, gatewayDockerfile)]] - `conceptually_related_to` [EXTRACTED]
- [[Docker Secrets required before containers start (openai_api_key.txt, 1password_bot_ , gateway_password.txt, 1password_service_account)]] - `conceptually_related_to` [EXTRACTED]
- [[Docker Volumes (auto-created) agentshroud-config, agentshroud-workspace, agentshroud-ssh, gateway-data]] - `conceptually_related_to` [EXTRACTED]
- [[External Dependencies (no deploy) 1Password Cloud, OpenAIAnthropicTelegram APIs, Tailscale Network via SSH]] - `conceptually_related_to` [EXTRACTED]

#graphify/image #graphify/EXTRACTED #community/Diagram_11_Trust_Boundary_images