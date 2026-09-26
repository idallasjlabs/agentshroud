---
type: community
cohesion: 0.18
members: 14
---

# Slack Channel Setup

**Cohesion:** 0.18 - loosely connected
**Members:** 14 nodes

## Members
- [[Get Shit Done (GSD) Cadence]] - document - docs/architecture/agentic-os.md
- [[8. Governance Model]] - document - docs/architecture/agentic-os.md
- [[AgentShroud CLAUDE.md operating rules]] - document - CLAUDE.md
- [[Branch Protection (belt-and-suspenders)]] - document - docs/architecture/agentic-os.md
- [[Cron Daily CVE Triage & Remediation Scan]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[No Security Theater (Rule A-E)]] - rationale - CLAUDE.md
- [[Recurring Governance Rituals]] - document - docs/architecture/agentic-os.md
- [[Weekly Upgrades EVERYTHING Means Everything]] - rationale - CLAUDE.md
- [[curl_json()]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[cve_prefetch.py]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[gatewaysecurityagent_cve_registry.py GHSA registry]] - concept - docker/config/openclaw/cron/scripts/prefetch-ghsa-registry.sh
- [[known_ghsa_ids()]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[main()_7]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[prefetch-ghsa-registry.sh (known-GHSA-ID cache prefetch)]] - code - docker/config/openclaw/cron/scripts/prefetch-ghsa-registry.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Slack_Channel_Setup
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_AgentShroud Agentic OS]]
- 1 edge to [[_COMMUNITY_DraftEntry]]

## Top bridge nodes
- [[8. Governance Model]] - degree 5, connects to 1 community
- [[AgentShroud CLAUDE.md operating rules]] - degree 3, connects to 1 community