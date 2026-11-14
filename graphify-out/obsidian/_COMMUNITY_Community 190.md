---
type: community
members: 41
---

# Community 190

**Members:** 41 nodes

## Members
- [[Crash backoff escalation (rolling 10-minute start window)]] - rationale - docker/bots/hermes/start.sh
- [[Env-split cron reconciliation (AGENTSHROUD_PROD_CRON_KEEP)]] - rationale - docker/bots/hermes/init-config.sh
- [[First-boot gateway-default s6 service auto-start]] - rationale - docker/bots/hermes/init-config.sh
- [[MCP servers reconciliation from mcpservers.json into config.yaml]] - rationale - docker/bots/hermes/init-config.sh
- [[Map job name - the full '_seed_cron Name ...' call text (all lines,     since]] - rationale - gateway/tests/test_hermes_cron_seed.py
- [[Missing-secret visibility banner (expected secrets loop)]] - rationale - docker/bots/hermes/start.sh
- [[Post-migration model lock + sandboxed terminal + cron fleet default]] - rationale - docker/bots/hermes/start.sh
- [[S11 init-openclaw-config.sh seeds jira_dev_ticket.py into live OpenClaw workspace]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S12 Hermes init-config.sh seeds jira_dev_ticket.py into live Hermes workspace]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S13 Hermes start.sh expected-secrets banner accepts env vars in place of mounted files]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[SCRUM-81 weekly Jira review cron must exist in both sh and yaml, Sun 0900.]] - rationale - gateway/tests/test_hermes_cron_seed.py
- [[Stamp-file gating (v1v2v3) caused job triplication on every version bump.]] - rationale - gateway/tests/test_hermes_cron_seed.py
- [[The schedule must be '0 9   0' (Sunday 0900) in both files.]] - rationale - gateway/tests/test_hermes_cron_seed.py
- [[These jobs must target an upstream the gateway can inject credentials for.]] - rationale - gateway/tests/test_hermes_cron_seed.py
- [[Tirith trust seeding (lookalike_tld + internal gateway HTTP rule)]] - rationale - docker/bots/hermes/init-config.sh
- [[_email_owner]] - code - docker/bots/hermes/start.sh
- [[_hermes_cron_ids_names]] - code - docker/bots/hermes/init-config.sh
- [[_parse_cron_names_from_sh()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[_parse_job_names_from_yaml()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[_parse_seed_cron_calls_from_sh()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[_release_telegram_lock]] - code - docker/bots/hermes/start.sh
- [[_seed_cron must accept optional $5 (model)  $6 (provider) and forward     them]] - rationale - gateway/tests/test_hermes_cron_seed.py
- [[_telegram_bot_token]] - code - docker/bots/hermes/start.sh
- [[_telegram_get_me_ready]] - code - docker/bots/hermes/start.sh
- [[_telegram_send_photo]] - code - docker/bots/hermes/start.sh
- [[_write_soul]] - code - docker/bots/hermes/init-config.sh
- [[init-config.sh (Hermes first-boot config materialisation)]] - code - docker/bots/hermes/init-config.sh
- [[jira-weekly-review is pure script execution (near-zero free-form     generation)]] - rationale - gateway/tests/test_hermes_cron_seed.py
- [[start.sh (Hermes s6 main program  startup wrapper)]] - code - docker/bots/hermes/start.sh
- [[test_competitive_email_job_present()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[test_competitive_landscape_job_present()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[test_content_generating_jobs_pinned_to_injectable_upstream()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[test_cron_seed_is_stampless_and_idempotent()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[test_hermes_cron_seed.py]] - code - gateway/tests/test_hermes_cron_seed.py
- [[test_init_config_has_expected_cron_job_count()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[test_jira_weekly_review_job_present()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[test_jira_weekly_review_not_pinned_to_a_model()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[test_jira_weekly_review_schedule_is_sunday_9am()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[test_jobs_yaml_has_expected_job_count()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[test_seed_cron_supports_optional_model_and_provider_args()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[test_stability_report_job_present()]] - code - gateway/tests/test_hermes_cron_seed.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_190
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Community 129]]

## Top bridge nodes
- [[test_hermes_cron_seed.py]] - degree 17, connects to 1 community
- [[start.sh (Hermes s6 main program  startup wrapper)]] - degree 11, connects to 1 community
- [[init-config.sh (Hermes first-boot config materialisation)]] - degree 10, connects to 1 community
- [[_telegram_bot_token]] - degree 5, connects to 1 community