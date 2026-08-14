---
source_file: "docs/vault/03 - Configuration/docker-compose.yml.md"
type: "concept"
community: "Gateway Test Suite"
location: "docker/docker-compose.yml"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# agentshroud-bot service (docker-compose: port 18789, 4GB memory, isolated network)

## Connections
- [[ANTHROPIC_BASE_URL (env var — routes bot LLM calls through gateway for security scanning)]] - `sets` [EXTRACTED]
- [[GATEWAY_OP_PROXY_URL (env var — routes 1Password op reads through gateway op-proxy endpoint)]] - `sets` [EXTRACTED]
- [[OPENCLAW_DISABLE_HOST_FILESYSTEM (env var — restricts agent to workspace volume only)]] - `sets` [EXTRACTED]
- [[OPENCLAW_SANDBOX_MODE (env var — strictpermissive agent sandbox enforcement level)]] - `sets` [EXTRACTED]
- [[SSH client config (bot container — pimarvin hosts, key-only auth, StrictHostKeyChecking)]] - `configures` [INFERRED]
- [[TELEGRAM_API_BASE_URL (env var — routes bot Telegram calls through gateway for PII scanning)]] - `sets` [EXTRACTED]
- [[agentshroud-seccomp.json (deny-by-default syscall allowlist for botPlaywright container)]] - `applied_to` [EXTRACTED]
- [[docker-compose.yml (primary Docker Compose — services, networks, volumes, secrets)]] - `defines` [EXTRACTED]
- [[falco-rules.yaml (runtime security rules — shell spawn, outbound, privilege escalation)]] - `monitors` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Gateway_Test_Suite