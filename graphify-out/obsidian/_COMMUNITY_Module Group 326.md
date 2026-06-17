---
type: community
cohesion: 0.24
members: 12
---

# Module Group 326

**Cohesion:** 0.24 - loosely connected
**Members:** 12 nodes

## Members
- [[ANTHROPIC_BASE_URL (env var — routes bot LLM calls through gateway for security scanning)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/04 - Environment Variables/ANTHROPIC_BASE_URL.md
- [[Docker networks (agentshroud-internal 172.20.0.016, agentshroud-isolated 172.21.0.016)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/docker-compose.yml.md
- [[GATEWAY_OP_PROXY_URL (env var — routes 1Password op reads through gateway op-proxy endpoint)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/04 - Environment Variables/GATEWAY_OP_PROXY_URL.md
- [[LOG_LEVEL (env var — DEBUGINFOWARNINGERROR; INFO default; overrides agentshroud.yaml)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/04 - Environment Variables/LOG_LEVEL.md
- [[OPENCLAW_DISABLE_HOST_FILESYSTEM (env var — restricts agent to workspace volume only)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/04 - Environment Variables/OPENCLAW_DISABLE_HOST_FILESYSTEM.md
- [[OPENCLAW_SANDBOX_MODE (env var — strictpermissive agent sandbox enforcement level)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/04 - Environment Variables/OPENCLAW_SANDBOX_MODE.md
- [[TELEGRAM_API_BASE_URL (env var — routes bot Telegram calls through gateway for PII scanning)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/04 - Environment Variables/TELEGRAM_API_BASE_URL.md
- [[agentshroud-bot service (docker-compose port 18789, 4GB memory, isolated network)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/docker-compose.yml.md
- [[agentshroud-seccomp.json (deny-by-default syscall allowlist for botPlaywright container)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/seccomp-profiles.md
- [[docker-compose.yml (primary Docker Compose — services, networks, volumes, secrets)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/docker-compose.yml.md
- [[gateway service (docker-compose port 8080, read-only rootfs, 1280MB memory)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/docker-compose.yml.md
- [[gateway-seccomp.json (deny-by-default syscall allowlist for gateway container)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/seccomp-profiles.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_326
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Module Group 344]]
- 1 edge to [[_COMMUNITY_Module Group 345]]
- 1 edge to [[_COMMUNITY_Module Group 569]]
- 1 edge to [[_COMMUNITY_Module Group 453]]

## Top bridge nodes
- [[docker-compose.yml (primary Docker Compose — services, networks, volumes, secrets)]] - degree 8, connects to 3 communities
- [[agentshroud-bot service (docker-compose port 18789, 4GB memory, isolated network)]] - degree 9, connects to 2 communities
- [[LOG_LEVEL (env var — DEBUGINFOWARNINGERROR; INFO default; overrides agentshroud.yaml)]] - degree 2, connects to 1 community