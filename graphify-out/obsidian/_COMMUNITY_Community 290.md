---
type: community
members: 19
---

# Community 290

**Members:** 19 nodes

## Members
- [[Crash backoff escalation (rolling 10-minute start window)]] - rationale - docker/bots/hermes/start.sh
- [[Env-split cron reconciliation (AGENTSHROUD_PROD_CRON_KEEP)]] - rationale - docker/bots/hermes/init-config.sh
- [[First-boot gateway-default s6 service auto-start]] - rationale - docker/bots/hermes/init-config.sh
- [[MCP servers reconciliation from mcpservers.json into config.yaml]] - rationale - docker/bots/hermes/init-config.sh
- [[Missing-secret visibility banner (expected secrets loop)]] - rationale - docker/bots/hermes/start.sh
- [[Post-migration model lock + sandboxed terminal + cron fleet default]] - rationale - docker/bots/hermes/start.sh
- [[S11 init-openclaw-config.sh seeds jira_dev_ticket.py into live OpenClaw workspace]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S12 Hermes init-config.sh seeds jira_dev_ticket.py into live Hermes workspace]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S13 Hermes start.sh expected-secrets banner accepts env vars in place of mounted files]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[Tirith trust seeding (lookalike_tld + internal gateway HTTP rule)]] - rationale - docker/bots/hermes/init-config.sh
- [[_email_owner]] - code - docker/bots/hermes/start.sh
- [[_hermes_cron_ids_names]] - code - docker/bots/hermes/init-config.sh
- [[_release_telegram_lock]] - code - docker/bots/hermes/start.sh
- [[_telegram_bot_token]] - code - docker/bots/hermes/start.sh
- [[_telegram_get_me_ready]] - code - docker/bots/hermes/start.sh
- [[_telegram_send_photo]] - code - docker/bots/hermes/start.sh
- [[_write_soul]] - code - docker/bots/hermes/init-config.sh
- [[init-config.sh (Hermes first-boot config materialisation)]] - code - docker/bots/hermes/init-config.sh
- [[start.sh (Hermes s6 main program  startup wrapper)]] - code - docker/bots/hermes/start.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_290
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Community 190]]
- 2 edges to [[_COMMUNITY_Community 129]]

## Top bridge nodes
- [[start.sh (Hermes s6 main program  startup wrapper)]] - degree 11, connects to 1 community
- [[init-config.sh (Hermes first-boot config materialisation)]] - degree 10, connects to 1 community
- [[_telegram_bot_token]] - degree 5, connects to 1 community