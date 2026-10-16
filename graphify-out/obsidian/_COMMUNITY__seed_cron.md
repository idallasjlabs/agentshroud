---
type: community
cohesion: 0.07
members: 35
---

# _seed_cron

**Cohesion:** 0.07 - loosely connected
**Members:** 35 nodes

## Members
- [[Checksum-gated idempotent config re-seed pattern]] - rationale - docker/bots/hermes/init-config.sh
- [[Duplicateoverlapping Hermes cron jobs colliding at same minute — retired duplicate]] - rationale - CHANGELOG.md
- [[Env-split cron enabledisable pass (dev enables, prod disables)]] - code - docker/scripts/start-agentshroud.sh
- [[Env-split cron reconciliation (prod pause  dev resume)]] - code - docker/bots/hermes/init-config.sh
- [[Env-split cron reconciliation — dev resumes all jobs, prod pauses except keep-list]] - rationale - docker/bots/hermes/init-config.sh
- [[First-boot gateway-default auto-start fix]] - rationale - docker/bots/hermes/init-config.sh
- [[GitHub MCP server wiring — first-boot add from github_pat secret]] - code - docker/bots/hermes/init-config.sh
- [[Hermes MCP servers.json reconciliation (config.yaml mcp_servers)]] - code - docker/bots/hermes/init-config.sh
- [[Hermes cron garbled output — nemotron exhausted budget on monologue; pinned to gemma-4-26b-a4b-it]] - rationale - CHANGELOG.md
- [[Hermes cron Competitive Intelligence Email AMPM]] - code - docker/bots/hermes/init-config.sh
- [[Hermes cron Competitive Landscape Update AMPM (zero-hallucination sourcing)]] - code - docker/bots/hermes/init-config.sh
- [[Hermes cron Weekly Hermes Stability Report (restartexit-code analysis)]] - code - docker/bots/hermes/init-config.sh
- [[Hermes cron Weekly Kaizen Review (gemma-4-26b-a4b-it)]] - code - docker/bots/hermes/init-config.sh
- [[Hermes cron jira-weekly-review (SCRUM-81 keeps Atlassian bot non-idle)]] - code - docker/bots/hermes/init-config.sh
- [[MCP reconciliation must actively disable stale enabledtrue entries, not just add]] - rationale - docker/bots/hermes/init-config.sh
- [[MCP servers reconciliation — writes config.yaml mcp_servers from servers.json (not `hermes mcp add`, which is interactive)]] - rationale - docker/bots/hermes/init-config.sh
- [[Owner directive 2026-08-29 env-split cron scheduling (dev runs, prod idle)]] - rationale - docker/bots/hermes/init-config.sh
- [[Provider names the gateway can actually inject a credential for.      Derived fr]] - rationale - gateway/tests/test_hermes_cron_seed.py
- [[Runtime facts writer — AGENTS.md AgentShroud version line (fixes hallucinated version)]] - rationale - docker/bots/hermes/init-config.sh
- [[SOUL.md checksum-stamped re-seed logic]] - code - docker/bots/hermes/init-config.sh
- [[Seed Job Weekly Kaizen Review]] - document - docker/config/hermes/cron/jobs.yaml
- [[Skills sync — installs ~.llm_settingsskills into optdataskills every boot]] - code - docker/bots/hermes/init-config.sh
- [[Tirith trust seeding — competitorresearch TLD lookalike bypass]] - code - docker/bots/hermes/init-config.sh
- [[Weekly Kaizen Review (Hermes Prompt)]] - document - docker/config/hermes/cron/prompts/weekly-kaizen-review.txt
- [[_hermes_cron_ids_names()]] - code - docker/bots/hermes/init-config.sh
- [[_injectable_providers()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[_seed_cron()]] - code - docker/bots/hermes/init-config.sh
- [[_write_soul()]] - code - docker/bots/hermes/init-config.sh
- [[gateway-default first-boot auto-start fix (removes stale down sentinel)]] - rationale - docker/bots/hermes/init-config.sh
- [[init-config.sh]] - code - docker/bots/hermes/init-config.sh
- [[init-config.sh (Hermes first-boot config materialisation)]] - code - docker/bots/hermes/init-config.sh
- [[init-config.sh main body]] - code - docker/bots/hermes/init-config.sh
- [[init-config.sh script]] - code - docker/bots/hermes/init-config.sh
- [[qwen3-coder silently routed to LM Studio instead of oMLX — generic prefix matched first]] - rationale - CHANGELOG.md
- [[v1.5.2 Release — local-model routing and cron reliability]] - rationale - CHANGELOG.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_seed_cron
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Hermes Cron Jobs Reference & Recreation Guide]]
- 3 edges to [[_COMMUNITY_test_hermes_cron_seed.py]]
- 3 edges to [[_COMMUNITY_start.sh]]
- 2 edges to [[_COMMUNITY_OpenClaw cron AgentShroud Daily Check-in (disabled, calls agentshroud-ssh-exec.sh)]]
- 2 edges to [[_COMMUNITY_competitive-report-.md dated reports]]
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 1 edge to [[_COMMUNITY_Report Delivery Format Instructions]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]
- 1 edge to [[_COMMUNITY_test_hermes_model_resolver.py]]

## Top bridge nodes
- [[_seed_cron()]] - degree 18, connects to 5 communities
- [[init-config.sh (Hermes first-boot config materialisation)]] - degree 10, connects to 2 communities
- [[init-config.sh]] - degree 10, connects to 2 communities
- [[init-config.sh main body]] - degree 4, connects to 2 communities
- [[Seed Job Weekly Kaizen Review]] - degree 3, connects to 1 community
