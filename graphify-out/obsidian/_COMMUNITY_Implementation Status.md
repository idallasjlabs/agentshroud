---
type: community
cohesion: 0.09
members: 23
---

# Implementation Status

**Cohesion:** 0.09 - loosely connected
**Members:** 23 nodes

## Members
- [[1. Summary line_1]] - document - reports/upgrade-2026-09-20.md
- [[10. Jira tracking]] - document - reports/upgrade-2026-09-20.md
- [[11. Verification evidence_1]] - document - reports/upgrade-2026-09-20.md
- [[12. Breaking changes  manual follow-ups_1]] - document - reports/upgrade-2026-09-20.md
- [[13. Rollback instructions_1]] - document - reports/upgrade-2026-09-20.md
- [[14. Time spent_1]] - document - reports/upgrade-2026-09-20.md
- [[2. Environment mapping (discovered, not assumed)_1]] - document - reports/upgrade-2026-09-20.md
- [[3. Dev handoff check (gating decision)_1]] - document - reports/upgrade-2026-09-20.md
- [[3b. New finding — dev's run appears hung, not merely absent]] - document - reports/upgrade-2026-09-20.md
- [[4. Preflight (prod, read-only)_1]] - document - reports/upgrade-2026-09-20.md
- [[5. Inventory — wrapped agents (mandatory script, cited)_1]] - document - reports/upgrade-2026-09-20.md
- [[6. Prod stack current health (read-only, unchanged by this run)]] - document - reports/upgrade-2026-09-20.md
- [[7. Security findings]] - document - reports/upgrade-2026-09-20.md
- [[7a. Image scan (Trivy, CRITICAL+HIGH, prod's currently-running tags)_1]] - document - reports/upgrade-2026-09-20.md
- [[7b. `npm audit` — browser-extension_1]] - document - reports/upgrade-2026-09-20.md
- [[7c. AgentShroud CVE-mitigation triage — NEW FINDING 98-advisory scope gap]] - document - reports/upgrade-2026-09-20.md
- [[7d. Python dependency audit]] - document - reports/upgrade-2026-09-20.md
- [[7e. WazuhSOC alerts]] - document - reports/upgrade-2026-09-20.md
- [[7f. Base images  other pinned components — inventoried, not re-verified against registry this run]] - document - reports/upgrade-2026-09-20.md
- [[7g. Untracked host services — confirmed still out of repo scope]] - document - reports/upgrade-2026-09-20.md
- [[8. Security findings table_1]] - document - reports/upgrade-2026-09-20.md
- [[9. Upgrade table_1]] - document - reports/upgrade-2026-09-20.md
- [[AgentShroud Sunday Upgrade Report — 2026-09-20 (PROD run)]] - document - reports/upgrade-2026-09-20.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Implementation_Status
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_web_config.py]]

## Top bridge nodes
- [[AgentShroud Sunday Upgrade Report — 2026-09-20 (PROD run)]] - degree 15, connects to 1 community