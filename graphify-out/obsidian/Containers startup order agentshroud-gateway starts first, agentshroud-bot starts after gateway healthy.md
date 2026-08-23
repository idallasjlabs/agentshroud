---
source_file: "docs/diagrams/images/diagram-22-dependency-graph.png"
type: "image"
community: "Diagram 11 Trust Boundary (images)"
tags:
  - graphify/image
  - graphify/EXTRACTED
  - community/Diagram_11_Trust_Boundary_images
---

# Containers startup order: agentshroud-gateway starts first, agentshroud-bot starts after gateway healthy

## Connections
- [[AgentShroud Gateway (Trust Zone 1) holds 1Password service account, enforces policy, signs ledger entries, controls approval queue, HMACJWT validation]] - `semantically_similar_to` [INFERRED]
- [[Docker Deployment Dependency Graph]] - `conceptually_related_to` [EXTRACTED]
- [[Docker Images docker-agentshroud (node22-bookworm-slim, Dockerfile.agentshroud), docker-gateway (python3.11-slim, gatewayDockerfile)]] - `shares_data_with` [EXTRACTED]
- [[Docker Secrets required before containers start (openai_api_key.txt, 1password_bot_ , gateway_password.txt, 1password_service_account)]] - `shares_data_with` [EXTRACTED]
- [[External Dependencies (no deploy) 1Password Cloud, OpenAIAnthropicTelegram APIs, Tailscale Network via SSH]] - `shares_data_with` [EXTRACTED]

#graphify/image #graphify/EXTRACTED #community/Diagram_11_Trust_Boundary_images