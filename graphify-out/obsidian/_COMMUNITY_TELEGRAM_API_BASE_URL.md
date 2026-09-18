---
type: community
cohesion: 0.12
members: 16
---

# TELEGRAM_API_BASE_URL

**Cohesion:** 0.12 - loosely connected
**Members:** 16 nodes

## Members
- [[Description_2]] - document - docs/vault/04 - Environment Variables/TELEGRAM_API_BASE_URL.md
- [[Effect]] - document - docs/vault/04 - Environment Variables/TELEGRAM_API_BASE_URL.md
- [[OpenClaw Service]] - code - docker/docker-compose.yml
- [[Related Notes_34]] - document - docs/vault/04 - Environment Variables/TELEGRAM_API_BASE_URL.md
- [[SDK Patch_1]] - document - docs/vault/04 - Environment Variables/TELEGRAM_API_BASE_URL.md
- [[Set In_1]] - document - docs/vault/04 - Environment Variables/TELEGRAM_API_BASE_URL.md
- [[Stdin-Pipe Deploy Pattern (never docker cp)]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[TELEGRAM_API_BASE_URL_1]] - document - docs/vault/04 - Environment Variables/TELEGRAM_API_BASE_URL.md
- [[TELEGRAM_API_BASE_URL]] - document - docs/vault/04 - Environment Variables/TELEGRAM_API_BASE_URL.md
- [[Value_2]] - document - docs/vault/04 - Environment Variables/TELEGRAM_API_BASE_URL.md
- [[init-openclaw-config.sh bootstrap]] - code - docker/scripts/init-openclaw-config.sh
- [[patch-anthropic-sdk.sh]] - code - docker/scripts/patch-anthropic-sdk.sh
- [[patch-anthropic-sdk.sh script]] - code - docker/scripts/patch-anthropic-sdk.sh
- [[patch-telegram-sdk.sh]] - code - docker/scripts/patch-telegram-sdk.sh
- [[patch-telegram-sdk.sh script]] - code - docker/scripts/patch-telegram-sdk.sh
- [[start-agentshroud.sh (OpenClaw entrypoint)]] - code - docker/scripts/start-agentshroud.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TELEGRAM_API_BASE_URL
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_ANTHROPIC_BASE_URL]]
- 1 edge to [[_COMMUNITY_DOCKER-VPN-NETWORKING]]
- 1 edge to [[_COMMUNITY_OpenClaw Live Cron Job Index (11 jobs)]]

## Top bridge nodes
- [[init-openclaw-config.sh bootstrap]] - degree 4, connects to 1 community
- [[patch-telegram-sdk.sh]] - degree 4, connects to 1 community
- [[TELEGRAM_API_BASE_URL]] - degree 3, connects to 1 community
- [[patch-anthropic-sdk.sh]] - degree 3, connects to 1 community
- [[Stdin-Pipe Deploy Pattern (never docker cp)]] - degree 2, connects to 1 community