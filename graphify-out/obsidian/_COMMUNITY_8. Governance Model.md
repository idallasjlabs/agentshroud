---
type: community
cohesion: 0.11
members: 20
---

# 8. Governance Model

**Cohesion:** 0.11 - loosely connected
**Members:** 20 nodes

## Members
- [[Get Shit Done (GSD) Cadence]] - document - docs/architecture/agentic-os.md
- [[8. Governance Model]] - document - docs/architecture/agentic-os.md
- [[AgentShroud CLAUDE.md operating rules]] - document - CLAUDE.md
- [[Branch Protection (belt-and-suspenders)]] - document - docs/architecture/agentic-os.md
- [[Cron Daily CVE Triage & Remediation Scan]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[No Security Theater (Rule A-E)]] - rationale - CLAUDE.md
- [[Recurring Governance Rituals]] - document - docs/architecture/agentic-os.md
- [[Weekly Upgrades EVERYTHING Means Everything]] - rationale - CLAUDE.md
- [[_inject_all]] - code - .llm_settings/scripts/session-prompt-setup.sh
- [[_inject_block]] - code - .llm_settings/scripts/session-prompt-setup.sh
- [[_parse_args]] - code - .llm_settings/scripts/session-prompt-setup.sh
- [[_remove_all]] - code - .llm_settings/scripts/session-prompt-setup.sh
- [[_resolve_prompt_file]] - code - .llm_settings/scripts/session-prompt-setup.sh
- [[_strip_block]] - code - .llm_settings/scripts/session-prompt-setup.sh
- [[curl_json]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[gatewaysecurityagent_cve_registry.py GHSA registry]] - concept - docker/config/openclaw/cron/scripts/prefetch-ghsa-registry.sh
- [[known_ghsa_ids]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[main_4]] - code - .llm_settings/scripts/session-prompt-setup.sh
- [[main (cve_prefetch.py)]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[prefetch-ghsa-registry.sh (known-GHSA-ID cache prefetch)]] - code - docker/config/openclaw/cron/scripts/prefetch-ghsa-registry.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/8_Governance_Model
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_AgentShroud Agentic OS]]
- 1 edge to [[_COMMUNITY_sunday-upgrade-apply.sh]]

## Top bridge nodes
- [[8. Governance Model]] - degree 5, connects to 1 community
- [[AgentShroud CLAUDE.md operating rules]] - degree 4, connects to 1 community