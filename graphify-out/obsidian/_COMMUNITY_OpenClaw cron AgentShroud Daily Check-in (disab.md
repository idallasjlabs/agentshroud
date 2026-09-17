---
type: community
cohesion: 0.11
members: 18
---

# OpenClaw cron: AgentShroud Daily Check-in (disab

**Cohesion:** 0.11 - loosely connected
**Members:** 18 nodes

## Members
- [[CI job gitleaks (full-history secret scan)]] - code - .github/workflows/ci.yml
- [[Cron Telegram delivery bypassed v1.5.2 base_url patch — fixed via third patch anchor on _send_to_platform]] - rationale - CHANGELOG.md
- [[Daily Check-in dumped raw ssh-exec JSON verbatim — rewritten to parse stdoutstderr]] - rationale - CHANGELOG.md
- [[Hermes cron AgentShroud Daily Check-in (gemma-4-26b-a4b-it)]] - code - docker/bots/hermes/init-config.sh
- [[OpenClaw cron AgentShroud Daily Check-in (disabled, calls agentshroud-ssh-exec.sh)]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[Patch 1 — _send_telegram signature + Bot() construction (version-tolerant anchors)]] - code - docker/bots/hermes/patch_telegram_send_base_url.py
- [[Patch 1b — _send_to_platform Telegram call site (fixes cron Delivertelegram bypass)]] - code - docker/bots/hermes/patch_telegram_send_base_url.py
- [[Patch 2 — adapter.py _standalone_send passthrough]] - code - docker/bots/hermes/patch_telegram_send_base_url.py
- [[Vendor target _send_telegram (toolssend_message_tool.py or send_message_senders.py)]] - code - docker/bots/hermes/patch_telegram_send_base_url.py
- [[Vendor target _send_to_platform (toolssend_message_tool.py, cron delivery call site)]] - code - docker/bots/hermes/patch_telegram_send_base_url.py
- [[Vendor target _standalone_send (pluginsplatformstelegramadapter.py)]] - code - docker/bots/hermes/patch_telegram_send_base_url.py
- [[_read]] - code - docker/bots/hermes/patch_telegram_send_base_url.py
- [[config.yaml seedupgrade — adds telegram.extra.base_url for gateway routing]] - code - docker/bots/hermes/init-config.sh
- [[dash echo XSI backslash-escape bug — fixed with printf '%sn']] - rationale - CHANGELOG.md
- [[patch_telegram_send_base_url.py_1]] - code - docker/bots/hermes/patch_telegram_send_base_url.py
- [[patch_telegram_send_base_url.py patch driver]] - code - docker/bots/hermes/patch_telegram_send_base_url.py
- [[ssh-exec.sh  ssh-write-file.sh fixed-filename race — moved to PID-suffixed files]] - rationale - CHANGELOG.md
- [[v1.5.3 Release — Telegramcron delivery fixes]] - rationale - CHANGELOG.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OpenClaw_cron_AgentShroud_Daily_Check-in_disab
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY__seed_cron]]

## Top bridge nodes
- [[Hermes cron AgentShroud Daily Check-in (gemma-4-26b-a4b-it)]] - degree 2, connects to 1 community
- [[config.yaml seedupgrade — adds telegram.extra.base_url for gateway routing]] - degree 2, connects to 1 community