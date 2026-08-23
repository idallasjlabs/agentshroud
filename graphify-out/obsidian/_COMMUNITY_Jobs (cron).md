---
type: community
cohesion: 0.08
members: 27
---

# Jobs (cron)

**Cohesion:** 0.08 - loosely connected
**Members:** 27 nodes

## Members
- [[AgentShroud Daily Check-in job]] - concept - docker/config/hermes/cron/jobs.yaml
- [[AgentShroud Weekly Summary job]] - concept - docker/config/hermes/cron/jobs.yaml
- [[Agentic AI CVE and Exploit Watch job]] - concept - docker/config/hermes/cron/jobs.yaml
- [[Cron AI Security Standards Watch]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[Cron AgentShroud Daily Check-in]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[Cron Agentic AI Threat Intelligence]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[Cron Collaborator Daily Digest]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[Cron Collaborator Report - Evening]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[Cron Collaborator Report - Morning]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[Cron Competitive Analysis Email (Afternoon)]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[Cron Competitive Landscape Update (Afternoon)]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[Cron Daily CVE Triage & Remediation Scan]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[Cron Daily Competitive Analysis Email]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[Cron Daily Competitive Landscape Update]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[Cron Monthly Chaos Engineering Drill]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[Daily Memory Journal job]] - concept - docker/config/hermes/cron/jobs.yaml
- [[Hermes Competitive Intelligence Email job]] - concept - docker/config/hermes/cron/jobs.yaml
- [[Hermes Competitive Landscape Update job]] - concept - docker/config/hermes/cron/jobs.yaml
- [[Hermes Cron Jobs Config]] - document - docker/config/hermes/cron/jobs.yaml
- [[Monthly Chaos Engineering Drill job]] - concept - docker/config/hermes/cron/jobs.yaml
- [[SCRUM-81 (Jira ticket)]] - concept - docker/config/hermes/cron/jobs.yaml
- [[Weekly Hermes Stability Report job]] - concept - docker/config/hermes/cron/jobs.yaml
- [[Weekly Kaizen Review job]] - concept - docker/config/hermes/cron/jobs.yaml
- [[agentshroud-email-send.sh]] - concept - docker/config/hermes/cron/jobs.yaml
- [[jira-weekly-review job]] - concept - docker/config/hermes/cron/jobs.yaml
- [[jira_weekly_review.py_1]] - concept - docker/config/hermes/cron/jobs.yaml
- [[render_md_email.py_1]] - concept - docker/config/hermes/cron/jobs.yaml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Jobs_cron
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Container Runtime (smoke.d)]]
- 1 edge to [[_COMMUNITY_Shutdown & recovery (01 - Architecture)]]

## Top bridge nodes
- [[Hermes Cron Jobs Config]] - degree 24, connects to 2 communities