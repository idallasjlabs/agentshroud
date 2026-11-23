---
type: community
members: 32
---

# start.sh

**Members:** 32 nodes

## Members
- [[Crash backoff escalation (rolling 10-minute start window)]] - rationale - docker/bots/hermes/start.sh
- [[Duplicateoverlapping Hermes cron jobs colliding at same minute — retired duplicate]] - rationale - CHANGELOG.md
- [[Env-split cron reconciliation (AGENTSHROUD_PROD_CRON_KEEP)]] - rationale - docker/bots/hermes/init-config.sh
- [[First-boot gateway-default s6 service auto-start]] - rationale - docker/bots/hermes/init-config.sh
- [[HERMES_HOME]] - code - docker/bots/hermes/start.sh
- [[HOME_1]] - code - docker/bots/hermes/start.sh
- [[Hermes cron garbled output — nemotron exhausted budget on monologue; pinned to gemma-4-26b-a4b-it]] - rationale - CHANGELOG.md
- [[MCP servers reconciliation from mcpservers.json into config.yaml]] - rationale - docker/bots/hermes/init-config.sh
- [[Missing-secret visibility banner (expected secrets loop)]] - rationale - docker/bots/hermes/start.sh
- [[Post-migration model lock + sandboxed terminal + cron fleet default]] - rationale - docker/bots/hermes/start.sh
- [[S11 init-openclaw-config.sh seeds jira_dev_ticket.py into live OpenClaw workspace]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S12 Hermes init-config.sh seeds jira_dev_ticket.py into live Hermes workspace]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S13 Hermes start.sh expected-secrets banner accepts env vars in place of mounted files]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[Tirith trust seeding (lookalike_tld + internal gateway HTTP rule)]] - rationale - docker/bots/hermes/init-config.sh
- [[XDG_CACHE_HOME]] - code - docker/bots/hermes/start.sh
- [[XDG_DATA_HOME]] - code - docker/bots/hermes/start.sh
- [[XDG_STATE_HOME]] - code - docker/bots/hermes/start.sh
- [[_email_owner()]] - code - docker/bots/hermes/start.sh
- [[_hermes_cron_ids_names()]] - code - docker/bots/hermes/init-config.sh
- [[_release_telegram_lock()]] - code - docker/bots/hermes/start.sh
- [[_seed_cron()]] - code - docker/bots/hermes/init-config.sh
- [[_telegram_bot_token()]] - code - docker/bots/hermes/start.sh
- [[_telegram_get_me_ready()]] - code - docker/bots/hermes/start.sh
- [[_telegram_send()_1]] - code - docker/bots/hermes/start.sh
- [[_telegram_send_photo()]] - code - docker/bots/hermes/start.sh
- [[_write_soul()]] - code - docker/bots/hermes/init-config.sh
- [[init-config.sh]] - code - docker/bots/hermes/init-config.sh
- [[init-config.sh script]] - code - docker/bots/hermes/init-config.sh
- [[qwen3-coder silently routed to LM Studio instead of oMLX — generic prefix matched first]] - rationale - CHANGELOG.md
- [[start.sh]] - code - docker/bots/hermes/start.sh
- [[start.sh script]] - code - docker/bots/hermes/start.sh
- [[v1.5.2 Release — local-model routing and cron reliability]] - rationale - CHANGELOG.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/startsh
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]

## Top bridge nodes
- [[_seed_cron()]] - degree 6, connects to 1 community
- [[_telegram_send()_1]] - degree 4, connects to 1 community
