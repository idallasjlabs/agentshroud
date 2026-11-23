---
type: community
members: 20
---

# Prompt: Daily Component Health Digest

**Members:** 20 nodes

## Members
- [[Dated Competitive Report Artifact (competitive-report-YYYY-MM-DD.md)]] - concept - docker/config/hermes/cron/prompts/hermes-competitive-landscape-update-am-pm.txt
- [[Gateway op-proxy Credential Broker]] - concept - docker/config/hermes/cron/prompts/jira-weekly-review.txt
- [[Keep Atlassian Account Non-Idle]] - rationale - docker/config/hermes/cron/prompts/jira-weekly-review.txt
- [[Mandatory --html Flag Rule]] - rationale - docker/config/hermes/cron/prompts/hermes-competitive-intelligence-email-am-pm.txt
- [[Mandatory Daily Delivery (never SILENT)]] - rationale - docker/config/hermes/cron/prompts/daily-component-health-digest.txt
- [[No .py Writes to tmp (workspace-only renderer scripts)]] - rationale - docker/config/hermes/cron/prompts/hermes-competitive-intelligence-email-am-pm.txt
- [[No execute_code  python3 -c  pip install in Cron Mode]] - rationale - docker/config/hermes/cron/prompts/newsletter-coding-agent-clis.txt
- [[Prompt Daily Component Health Digest]] - document - docker/config/hermes/cron/prompts/daily-component-health-digest.txt
- [[Prompt Hermes Competitive Intelligence Email (AMPM)]] - document - docker/config/hermes/cron/prompts/hermes-competitive-intelligence-email-am-pm.txt
- [[Prompt Hermes Competitive Landscape Update (AMPM)]] - document - docker/config/hermes/cron/prompts/hermes-competitive-landscape-update-am-pm.txt
- [[Prompt jira-weekly-review]] - document - docker/config/hermes/cron/prompts/jira-weekly-review.txt
- [[SCRUM-81 Weekly Review Ticket]] - concept - docker/config/hermes/cron/prompts/jira-weekly-review.txt
- [[Script-Output-Only Constraint (no tools, no recomputation)]] - rationale - docker/config/hermes/cron/prompts/daily-component-health-digest.txt
- [[Silence-Over-Hallucination Principle]] - rationale - docker/config/hermes/cron/prompts/hermes-competitive-landscape-update-am-pm.txt
- [[Stale Trivy Scan Disclosure Requirement]] - rationale - docker/config/hermes/cron/prompts/daily-component-health-digest.txt
- [[Zero-Hallucination Primary-Source Rule (30-day recency)]] - rationale - docker/config/hermes/cron/prompts/newsletter-coding-agent-clis.txt
- [[agentshroud-email-send.sh Gateway Email Sender]] - concept - docker/config/hermes/cron/prompts/hermes-competitive-intelligence-email-am-pm.txt
- [[competitive-analysis.md 4-Section Research Spec]] - concept - docker/config/hermes/cron/prompts/hermes-competitive-landscape-update-am-pm.txt
- [[jira_weekly_review.py Pre-Committed Posting Script]] - concept - docker/config/hermes/cron/prompts/jira-weekly-review.txt
- [[render_md_email.py Markdown-to-Inline-CSS Email Renderer]] - concept - docker/config/hermes/cron/prompts/hermes-competitive-intelligence-email-am-pm.txt

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Prompt_Daily_Component_Health_Digest
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Hermes Cron Jobs Reference & Recreation Guide]]
- 1 edge to [[_COMMUNITY_AgentShroud Changelog]]
- 1 edge to [[_COMMUNITY_Telegram Formatting Rule (bold only, no headers or tables)]]

## Top bridge nodes
- [[Prompt Daily Component Health Digest]] - degree 7, connects to 3 communities
- [[Prompt Hermes Competitive Landscape Update (AMPM)]] - degree 4, connects to 1 community
- [[Prompt jira-weekly-review]] - degree 4, connects to 1 community
- [[Zero-Hallucination Primary-Source Rule (30-day recency)]] - degree 2, connects to 1 community
