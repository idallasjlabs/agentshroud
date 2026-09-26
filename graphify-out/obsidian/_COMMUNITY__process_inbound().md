---
type: community
cohesion: 0.10
members: 20
---

# _process_inbound()

**Cohesion:** 0.10 - loosely connected
**Members:** 20 nodes

## Members
- [[1. Environment mapping]] - document - reports/upgrade-2026-09-06-dev.md
- [[7a. Image scan (Trivy, CRITICAL+HIGH, prod's currently-running tags)]] - document - reports/upgrade-2026-09-17.md
- [[7b. `npm audit` — browser-extension]] - document - reports/upgrade-2026-09-17.md
- [[7c. Python dependency audit — GAP, not silently skipped]] - document - reports/upgrade-2026-09-17.md
- [[7d. WazuhSOC alerts — partial]] - document - reports/upgrade-2026-09-17.md
- [[7e. Base images (Dockerfiles) — inventoried, not re-verified against registry]] - document - reports/upgrade-2026-09-17.md
- [[AgentShroud Weekly Upgrade — 2026-09-06]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[Application CVE registry (OpenClaw  Hermes agents, per `docssecuritycve-mitigation-matrix.md`)]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[Breaking changes  manual follow-ups]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[Fresh Trivy scans (run today, CRITICAL+HIGH only, `--scanners vuln`)]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[GitHub-hosted findings]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[Language dependencies]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[Preflight  Baseline]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[Rollback Instructions]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[SecurityFinding_1]] - document - docs/data/data-dictionary.md
- [[Summary_25]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[Time spent]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[Upgrade Table]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[Wazuh  SOC]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[upgrade-2026-09-06-20260906-0808]] - document - reports/upgrade-2026-09-06-20260906-0808.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_process_inbound
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_auth.py]]
- 1 edge to [[_COMMUNITY_Deploying AgentShroud on Raspberry Pi (aarch64)]]
- 1 edge to [[_COMMUNITY_2. Security Analysis]]

## Top bridge nodes
- [[SecurityFinding_1]] - degree 16, connects to 3 communities
- [[1. Environment mapping]] - degree 3, connects to 1 community