---
type: community
cohesion: 0.40
members: 5
---

# V0.8.0 Wiring Audit (v0.8)

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[Inbound Request Path (middleware.py → process_request)]] - document - docs/planning/v0.8/v0.8.0-wiring-audit.md
- [[Infrastructure (lifespan.py — initialized at startup)]] - document - docs/planning/v0.8/v0.8.0-wiring-audit.md
- [[Outbound Path (middleware.py)]] - document - docs/planning/v0.8/v0.8.0-wiring-audit.md
- [[Pipeline (pipeline.py → process_inbound  process_outbound)]] - document - docs/planning/v0.8/v0.8.0-wiring-audit.md
- [[✅ CONFIRMED WIRED AND WORKING]] - document - docs/planning/v0.8/v0.8.0-wiring-audit.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/V080_Wiring_Audit_v08
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_V0.8.0 Wiring Audit (v0.8)]]

## Top bridge nodes
- [[✅ CONFIRMED WIRED AND WORKING]] - degree 5, connects to 1 community