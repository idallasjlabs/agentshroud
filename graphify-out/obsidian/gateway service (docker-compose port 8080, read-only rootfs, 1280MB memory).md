---
source_file: "docs/vault/03 - Configuration/docker-compose.yml.md"
type: "concept"
community: "docs/vault"
location: "docker/docker-compose.yml"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/docs/vault
---

# gateway service (docker-compose: port 8080, read-only rootfs, 1280MB memory)

## Connections
- [[ANTHROPIC_BASE_URL (env var — routes bot LLM calls through gateway for security scanning)]] - `routes_traffic_to` [EXTRACTED]
- [[LOG_LEVEL (env var — DEBUGINFOWARNINGERROR; INFO default; overrides agentshroud.yaml)]] - `sets` [EXTRACTED]
- [[TELEGRAM_API_BASE_URL (env var — routes bot Telegram calls through gateway for PII scanning)]] - `routes_traffic_to` [EXTRACTED]
- [[docker-compose.yml (primary Docker Compose — services, networks, volumes, secrets)]] - `defines` [EXTRACTED]
- [[gateway-seccomp.json (deny-by-default syscall allowlist for gateway container)]] - `applied_to` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/docs/vault