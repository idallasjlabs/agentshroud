---
type: community
members: 36
---

# test_hermes_cron_seed.py

**Members:** 36 nodes

## Members
- [[Duplicateoverlapping Hermes cron jobs colliding at same minute — retired duplicate]] - rationale - CHANGELOG.md
- [[First-boot gateway-default s6 service auto-start]] - rationale - docker/bots/hermes/init-config.sh
- [[Hermes cron garbled output — nemotron exhausted budget on monologue; pinned to gemma-4-26b-a4b-it]] - rationale - CHANGELOG.md
- [[MCP servers reconciliation from mcpservers.json into config.yaml]] - rationale - docker/bots/hermes/init-config.sh
- [[Map job name - the full '_seed_cron Name ...' call text (all lines,     since]] - rationale - gateway/tests/test_hermes_cron_seed.py
- [[Provider names the gateway can actually inject a credential for.      Derived fr]] - rationale - gateway/tests/test_hermes_cron_seed.py
- [[SCRUM-81 weekly Jira review cron must exist in both sh and yaml, Sun 0900.]] - rationale - gateway/tests/test_hermes_cron_seed.py
- [[Stamp-file gating (v1v2v3) caused job triplication on every version bump.]] - rationale - gateway/tests/test_hermes_cron_seed.py
- [[The schedule must be '0 9   0' (Sunday 0900) in both files.]] - rationale - gateway/tests/test_hermes_cron_seed.py
- [[These jobs must target an upstream the gateway can inject credentials for.]] - rationale - gateway/tests/test_hermes_cron_seed.py
- [[Tirith trust seeding (lookalike_tld + internal gateway HTTP rule)]] - rationale - docker/bots/hermes/init-config.sh
- [[_injectable_providers()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[_parse_cron_names_from_sh()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[_parse_job_names_from_yaml()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[_parse_seed_cron_calls_from_sh()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[_seed_cron]] - code - docker/bots/hermes/init-config.sh
- [[_seed_cron must accept optional $5 (model)  $6 (provider) and forward     them]] - rationale - gateway/tests/test_hermes_cron_seed.py
- [[_write_soul]] - code - docker/bots/hermes/init-config.sh
- [[init-config.sh (Hermes first-boot config materialisation)]] - code - docker/bots/hermes/init-config.sh
- [[init-config.sh script]] - code - docker/bots/hermes/init-config.sh
- [[jira-weekly-review is pure script execution (near-zero free-form     generation)]] - rationale - gateway/tests/test_hermes_cron_seed.py
- [[qwen3-coder silently routed to LM Studio instead of oMLX — generic prefix matched first]] - rationale - CHANGELOG.md
- [[test_competitive_email_job_present()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[test_competitive_landscape_job_present()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[test_content_generating_jobs_pinned_to_evidence_backed_model()]] - code - gateway/tests/test_hermes_cron_seed.py
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
- [[v1.5.2 Release — local-model routing and cron reliability]] - rationale - CHANGELOG.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_hermes_cron_seedpy
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 2 edges to [[_COMMUNITY_run-standalone.sh (Hermes docker run launcher)]]
- 1 edge to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes) (2)]]

## Top bridge nodes
- [[init-config.sh (Hermes first-boot config materialisation)]] - degree 11, connects to 3 communities
- [[_seed_cron]] - degree 8, connects to 1 community
