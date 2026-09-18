---
type: community
cohesion: 0.06
members: 42
---

# _seed_cron

**Cohesion:** 0.06 - loosely connected
**Members:** 42 nodes

## Members
- [[CI job soul-freshness (SOUL.md 90-day staleness check)]] - code - .github/workflows/ci.yml
- [[Crash backoff escalation — 5 restarts600s pauses 300s (raw curl, helpers not yet defined)]] - rationale - docker/bots/hermes/start.sh
- [[Daily Memory Journal (Hermes Prompt)]] - document - docker/config/hermes/cron/prompts/daily-memory-journal.txt
- [[Duplicateoverlapping Hermes cron jobs colliding at same minute — retired duplicate]] - rationale - CHANGELOG.md
- [[Env-split cron reconciliation — dev resumes all jobs, prod pauses except keep-list]] - rationale - docker/bots/hermes/init-config.sh
- [[GitHub MCP server wiring — first-boot add from github_pat secret]] - code - docker/bots/hermes/init-config.sh
- [[Hermes cron garbled output — nemotron exhausted budget on monologue; pinned to gemma-4-26b-a4b-it]] - rationale - CHANGELOG.md
- [[Hermes cron AgentShroud Weekly Summary (gemma-4-26b-a4b-it)]] - code - docker/bots/hermes/init-config.sh
- [[Hermes cron Competitive Intelligence Email AMPM]] - code - docker/bots/hermes/init-config.sh
- [[Hermes cron Competitive Landscape Update AMPM (zero-hallucination sourcing)]] - code - docker/bots/hermes/init-config.sh
- [[Hermes cron Daily Memory Journal (silent, local delivery)]] - code - docker/bots/hermes/init-config.sh
- [[Hermes cron Weekly Hermes Stability Report (restartexit-code analysis)]] - code - docker/bots/hermes/init-config.sh
- [[Hermes cron jira-weekly-review (SCRUM-81 keeps Atlassian bot non-idle)]] - code - docker/bots/hermes/init-config.sh
- [[MCP servers reconciliation — writes config.yaml mcp_servers from servers.json (not `hermes mcp add`, which is interactive)]] - rationale - docker/bots/hermes/init-config.sh
- [[OpenClaw cron AgentShroud Weekly Summary]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[Post-migration model lock — resolve_model.py sets model.defaultprovider + cron.model after readiness]] - rationale - docker/bots/hermes/start.sh
- [[Referenced resolve_model.py (usrlocallibagentshroudresolve_model.py)]] - code - docker/bots/hermes/start.sh
- [[Runtime facts writer — AGENTS.md AgentShroud version line (fixes hallucinated version)]] - rationale - docker/bots/hermes/init-config.sh
- [[Sandboxed terminal config — terminal.docker_ keys set via `hermes config set`, not env vars]] - rationale - docker/bots/hermes/start.sh
- [[Seed Job Daily Memory Journal]] - document - docker/config/hermes/cron/jobs.yaml
- [[Skills sync — installs ~.llm_settingsskills into optdataskills every boot]] - code - docker/bots/hermes/init-config.sh
- [[Tirith trust seeding — competitorresearch TLD lookalike bypass]] - code - docker/bots/hermes/init-config.sh
- [[_apply_stale_alias_correction]] - code - docker/bots/hermes/resolve_model.py
- [[_hermes_cron_ids_names()_1]] - code - docker/bots/hermes/init-config.sh
- [[_resolve_from_env]] - code - docker/bots/hermes/resolve_model.py
- [[_seed_cron]] - code - docker/bots/hermes/init-config.sh
- [[_write_soul]] - code - docker/bots/hermes/init-config.sh
- [[gateway LLM proxy local-model routing (llm_proxy.py)]] - concept - docker/bots/hermes/resolve_model.py
- [[gateway-default first-boot auto-start fix (removes stale down sentinel)]] - rationale - docker/bots/hermes/init-config.sh
- [[init-config.sh]] - code - docker/bots/hermes/init-config.sh
- [[init-config.sh (Hermes first-boot config materialisation)]] - code - docker/bots/hermes/init-config.sh
- [[init-config.sh main body]] - code - docker/bots/hermes/init-config.sh
- [[init-config.sh script_1]] - code - docker/bots/hermes/init-config.sh
- [[inject (Docker secret - s6 env)]] - code - docker/bots/hermes/agentshroud-secrets.sh
- [[main (resolve_model.py CLI)]] - code - docker/bots/hermes/resolve_model.py
- [[provider_for_model]] - code - docker/bots/hermes/resolve_model.py
- [[qwen3-coder silently routed to LM Studio instead of oMLX — generic prefix matched first]] - rationale - CHANGELOG.md
- [[resolve_model]] - code - docker/bots/hermes/resolve_model.py
- [[start.sh (Hermes s6 main program)]] - code - docker/bots/hermes/start.sh
- [[start.sh — Hermes s6-overlay startup wrapper (main program)]] - code - docker/bots/hermes/start.sh
- [[strip_provider_prefix]] - code - docker/bots/hermes/resolve_model.py
- [[v1.5.2 Release — local-model routing and cron reliability]] - rationale - CHANGELOG.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_seed_cron
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_OpenClaw cron AgentShroud Daily Check-in (disab]]
- 2 edges to [[_COMMUNITY_Telegram Formatting Rule (bold only, no headers]]
- 2 edges to [[_COMMUNITY_gateway service (prod, sole egress point, 75-mod]]
- 2 edges to [[_COMMUNITY_competitive-report-.md dated reports]]
- 1 edge to [[_COMMUNITY_OpenClaw Live Cron Job Index (11 jobs)]]
- 1 edge to [[_COMMUNITY_apply-patches.js]]
- 1 edge to [[_COMMUNITY_start.sh]]

## Top bridge nodes
- [[_seed_cron]] - degree 15, connects to 2 communities
- [[init-config.sh (Hermes first-boot config materialisation)]] - degree 11, connects to 2 communities
- [[gateway LLM proxy local-model routing (llm_proxy.py)]] - degree 3, connects to 1 community
- [[Seed Job Daily Memory Journal]] - degree 3, connects to 1 community
- [[qwen3-coder silently routed to LM Studio instead of oMLX — generic prefix matched first]] - degree 2, connects to 1 community