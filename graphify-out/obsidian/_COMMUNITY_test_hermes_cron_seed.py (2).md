---
type: community
members: 16
---

# test_hermes_cron_seed.py (2)

**Members:** 16 nodes

## Members
- [[Duplicateoverlapping Hermes cron jobs colliding at same minute — retired duplicate]] - rationale - CHANGELOG.md
- [[Env-split cron reconciliation (AGENTSHROUD_PROD_CRON_KEEP)]] - rationale - docker/bots/hermes/init-config.sh
- [[First-boot gateway-default s6 service auto-start]] - rationale - docker/bots/hermes/init-config.sh
- [[Hermes cron garbled output — nemotron exhausted budget on monologue; pinned to gemma-4-26b-a4b-it]] - rationale - CHANGELOG.md
- [[MCP servers reconciliation from mcpservers.json into config.yaml]] - rationale - docker/bots/hermes/init-config.sh
- [[Missing-secret visibility banner (expected secrets loop)]] - rationale - docker/bots/hermes/start.sh
- [[Provider names the gateway can actually inject a credential for.      Derived fr]] - rationale - gateway/tests/test_hermes_cron_seed.py
- [[Tirith trust seeding (lookalike_tld + internal gateway HTTP rule)]] - rationale - docker/bots/hermes/init-config.sh
- [[_hermes_cron_ids_names]] - code - docker/bots/hermes/init-config.sh
- [[_injectable_providers()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[_seed_cron]] - code - docker/bots/hermes/init-config.sh
- [[_write_soul]] - code - docker/bots/hermes/init-config.sh
- [[init-config.sh (Hermes first-boot config materialisation)]] - code - docker/bots/hermes/init-config.sh
- [[init-config.sh script]] - code - docker/bots/hermes/init-config.sh
- [[qwen3-coder silently routed to LM Studio instead of oMLX — generic prefix matched first]] - rationale - CHANGELOG.md
- [[v1.5.2 Release — local-model routing and cron reliability]] - rationale - CHANGELOG.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_hermes_cron_seedpy_2
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_hermes_cron_seed.py]]
- 2 edges to [[_COMMUNITY_run-standalone.sh (Hermes docker run launcher)]]
- 2 edges to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 2 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 1 edge to [[_COMMUNITY_run-standalone.sh (Hermes docker run launcher) (2)]]

## Top bridge nodes
- [[init-config.sh (Hermes first-boot config materialisation)]] - degree 11, connects to 3 communities
- [[_seed_cron]] - degree 8, connects to 2 communities
- [[Missing-secret visibility banner (expected secrets loop)]] - degree 4, connects to 2 communities
- [[_injectable_providers()]] - degree 3, connects to 1 community
