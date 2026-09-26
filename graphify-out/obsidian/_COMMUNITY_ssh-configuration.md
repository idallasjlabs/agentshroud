---
type: community
cohesion: 0.11
members: 19
---

# ssh-configuration.md

**Cohesion:** 0.11 - loosely connected
**Members:** 19 nodes

## Members
- [[Duplicateoverlapping Hermes cron jobs colliding at same minute — retired duplicate]] - rationale - CHANGELOG.md
- [[Env-split cron enabledisable pass (dev enables, prod disables)]] - code - docker/scripts/start-agentshroud.sh
- [[Env-split cron reconciliation (prod pause  dev resume)]] - code - docker/bots/hermes/init-config.sh
- [[Hermes cron garbled output — nemotron exhausted budget on monologue; pinned to gemma-4-26b-a4b-it]] - rationale - CHANGELOG.md
- [[Hermes cron AgentShroud Weekly Summary (gemma-4-26b-a4b-it)]] - code - docker/bots/hermes/init-config.sh
- [[Hermes cron Competitive Intelligence Email AMPM]] - code - docker/bots/hermes/init-config.sh
- [[Hermes cron Competitive Landscape Update AMPM (zero-hallucination sourcing)]] - code - docker/bots/hermes/init-config.sh
- [[Hermes cron Weekly Hermes Stability Report (restartexit-code analysis)]] - code - docker/bots/hermes/init-config.sh
- [[Hermes cron Weekly Kaizen Review (gemma-4-26b-a4b-it)]] - code - docker/bots/hermes/init-config.sh
- [[Hermes cron jira-weekly-review (SCRUM-81 keeps Atlassian bot non-idle)]] - code - docker/bots/hermes/init-config.sh
- [[OpenClaw cron AgentShroud Weekly Summary]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[Owner directive 2026-08-29 env-split cron scheduling (dev runs, prod idle)]] - rationale - docker/bots/hermes/init-config.sh
- [[Provider names the gateway can actually inject a credential for.      Derived fr]] - rationale - gateway/tests/test_hermes_cron_seed.py
- [[Seed Job Weekly Kaizen Review]] - document - docker/config/hermes/cron/jobs.yaml
- [[Weekly Kaizen Review (Hermes Prompt)]] - document - docker/config/hermes/cron/prompts/weekly-kaizen-review.txt
- [[_injectable_providers()]] - code - gateway/tests/test_hermes_cron_seed.py
- [[_seed_cron()]] - code - docker/bots/hermes/init-config.sh
- [[qwen3-coder silently routed to LM Studio instead of oMLX — generic prefix matched first]] - rationale - CHANGELOG.md
- [[v1.5.2 Release — local-model routing and cron reliability]] - rationale - CHANGELOG.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ssh-configurationmd
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Skill UX Expert (UX)]]
- 2 edges to [[_COMMUNITY_GroupRegistry]]
- 2 edges to [[_COMMUNITY_Currently Unmitigable Residual Class]]
- 2 edges to [[_COMMUNITY_Skill Test-Driven Development (TDD)]]
- 1 edge to [[_COMMUNITY__t()]]
- 1 edge to [[_COMMUNITY_MCPToolResult]]
- 1 edge to [[_COMMUNITY_TELEGRAM_ISSUES]]
- 1 edge to [[_COMMUNITY_What You Must Do When Invoked]]
- 1 edge to [[_COMMUNITY_Skills by Category]]

## Top bridge nodes
- [[_seed_cron()]] - degree 18, connects to 6 communities
- [[Seed Job Weekly Kaizen Review]] - degree 3, connects to 1 community
- [[Env-split cron reconciliation (prod pause  dev resume)]] - degree 3, connects to 1 community
- [[_injectable_providers()]] - degree 3, connects to 1 community
- [[qwen3-coder silently routed to LM Studio instead of oMLX — generic prefix matched first]] - degree 2, connects to 1 community