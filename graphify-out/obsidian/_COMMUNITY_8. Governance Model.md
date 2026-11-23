---
type: community
members: 10
---

# 8. Governance Model

**Members:** 10 nodes

## Members
- [[Get Shit Done (GSD) Cadence]] - document - docs/architecture/agentic-os.md
- [[8. Governance Model]] - document - docs/architecture/agentic-os.md
- [[AgentShroud CLAUDE.md operating rules]] - document - CLAUDE.md
- [[Branch Protection (belt-and-suspenders)]] - document - docs/architecture/agentic-os.md
- [[No Security Theater (Rule A-E)]] - rationale - CLAUDE.md
- [[No Security Theater Rules]] - document - docs/architecture/agentic-os.md
- [[Prove the Outcome, Never the Steps]] - rationale - CLAUDE.md
- [[Recurring Governance Rituals]] - document - docs/architecture/agentic-os.md
- [[Weekly Upgrades EVERYTHING Means Everything]] - rationale - CLAUDE.md
- [[gatewaysecurityagent_cve_registry.py GHSA registry]] - concept - docker/config/openclaw/cron/scripts/prefetch-ghsa-registry.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/8_Governance_Model
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_sync-cve-registry.py]]
- 1 edge to [[_COMMUNITY_AgentShroud Agentic OS]]

## Top bridge nodes
- [[8. Governance Model]] - degree 6, connects to 1 community
- [[Prove the Outcome, Never the Steps]] - degree 2, connects to 1 community
