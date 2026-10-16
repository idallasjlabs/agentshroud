---
type: community
cohesion: 0.22
members: 18
---

# competitive-report-*.md dated reports

**Cohesion:** 0.22 - loosely connected
**Members:** 18 nodes

## Members
- [[Apply inline Markdown spans to plain text (no recursive nesting).]] - rationale - docker/bots/hermes/render_md_email.py
- [[Hermes Competitive Intelligence Email (AMPM)_1]] - document - docker/config/hermes/cron/prompts/hermes-competitive-intelligence-email-am-pm.txt
- [[Hermes Competitive Landscape Update (AMPM)_1]] - document - docker/config/hermes/cron/prompts/hermes-competitive-landscape-update-am-pm.txt
- [[OpenClaw cron Competitive Analysis Email (Afternoon)]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[OpenClaw cron Competitive Landscape Update (Afternoon)]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[OpenClaw cron Daily Competitive Analysis Email (AM)]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[OpenClaw cron Daily Competitive Landscape Update (zero-hallucination sourcing rules)]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[_esc()]] - code - docker/bots/hermes/render_md_email.py
- [[_inline()]] - code - docker/bots/hermes/render_md_email.py
- [[_render_table()]] - code - docker/bots/hermes/render_md_email.py
- [[agentshroud-email-send.sh]] - code - docker/config/hermes/cron/prompts/hermes-competitive-intelligence-email-am-pm.txt
- [[competitive-analysis.md artifact]] - concept - docker/config/hermes/cron/prompts/hermes-competitive-landscape-update-am-pm.txt
- [[competitive-report-.md dated reports]] - concept - docker/config/hermes/cron/prompts/hermes-competitive-intelligence-email-am-pm.txt
- [[cron-operations skill]] - concept - docker/config/hermes/cron/prompts/hermes-competitive-intelligence-email-am-pm.txt
- [[main()_3]] - code - docker/bots/hermes/render_md_email.py
- [[render()]] - code - docker/bots/hermes/render_md_email.py
- [[render_md_email.py]] - code - docker/bots/hermes/render_md_email.py
- [[trend-log.md artifact]] - concept - docker/config/hermes/cron/prompts/hermes-competitive-landscape-update-am-pm.txt

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/competitive-report-md_dated_reports
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY__seed_cron]]

## Top bridge nodes
- [[OpenClaw cron Daily Competitive Landscape Update (zero-hallucination sourcing rules)]] - degree 6, connects to 1 community
- [[OpenClaw cron Daily Competitive Analysis Email (AM)]] - degree 5, connects to 1 community
