---
type: community
members: 7
---

# scripts/tailscale-serve.sh

**Members:** 7 nodes

## Members
- [[4.1 Per-bot egress allowlist completeness]] - document - docs/planning/v1.2/blue-team-assessment-v1.2.0.md
- [[4.2 Per-bot trust seeding]] - document - docs/planning/v1.2/blue-team-assessment-v1.2.0.md
- [[4.3 Per-bot CVE triage cron health]] - document - docs/planning/v1.2/blue-team-assessment-v1.2.0.md
- [[4.4 Hermes SOUL.md information disclosure posture]] - document - docs/planning/v1.2/blue-team-assessment-v1.2.0.md
- [[4.5 Hermes dashboard TCP forwarder — binding address]] - document - docs/planning/v1.2/blue-team-assessment-v1.2.0.md
- [[4.6 Cross-bot session isolation (FINDING BT-H1 — FIXED IN THIS PR)]] - document - docs/planning/v1.2/blue-team-assessment-v1.2.0.md
- [[§4 — Hermes-Specific Section (NEW — first assessment)]] - document - docs/planning/v1.2/blue-team-assessment-v1.2.0.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scripts/tailscale-servesh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Docker Deploy Scripts]]

## Top bridge nodes
- [[§4 — Hermes-Specific Section (NEW — first assessment)]] - degree 7, connects to 1 community