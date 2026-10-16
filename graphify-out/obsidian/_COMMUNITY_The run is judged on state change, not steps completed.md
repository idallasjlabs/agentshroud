---
type: community
cohesion: 0.22
members: 11
---

# The run is judged on state change, not steps completed

**Cohesion:** 0.22 - loosely connected
**Members:** 11 nodes

## Members
- [[Image signing & provenance job (cosign keyless + syft SBOM attest)]] - code - .github/workflows/security-scan.yml
- [[Inventory EVERYTHING MEANS EVERYTHING — a component missing from the table is a failed run]] - rationale - prompts/sunday-upgrade.md
- [[Semgrep --baseline-commit gate (fail only on NEW findings)]] - rationale - .github/workflows/security-scan.yml
- [[Semgrep SAST job (IEC 62443 4-1 SDL)]] - code - .github/workflows/security-scan.yml
- [[The run is judged on state change, not steps completed]] - rationale - prompts/sunday-upgrade.md
- [[Trivy filesystem scan job (SHA-pinned action)]] - code - .github/workflows/security-scan.yml
- [[pre-commit as single owner of .githookspre-commit]] - rationale - .pre-commit-config.yaml
- [[pre-commit detect-secrets hook (v1.5.0, .secrets.baseline)]] - code - .pre-commit-config.yaml
- [[pre-commit git-secrets local hook (AWS credential patterns)]] - code - .pre-commit-config.yaml
- [[pre-commit semgrep local hook (new findings only, system semgrep)]] - code - .pre-commit-config.yaml
- [[sunday-upgrade-apply.sh no-op gate fixes (Hermes feeds UPGRADE_AVAILABLE, unknown != current, merge-base 'before' pins)]] - concept - INCIDENT_2026-10-16_conduit-outage.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/The_run_is_judged_on_state_change_not_steps_completed
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 2 edges to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 1 edge to [[_COMMUNITY_discover_upstream_versions.py]]
- 1 edge to [[_COMMUNITY_Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)]]

## Top bridge nodes
- [[The run is judged on state change, not steps completed]] - degree 7, connects to 3 communities
- [[Inventory EVERYTHING MEANS EVERYTHING — a component missing from the table is a failed run]] - degree 3, connects to 1 community
- [[Image signing & provenance job (cosign keyless + syft SBOM attest)]] - degree 2, connects to 1 community
- [[sunday-upgrade-apply.sh no-op gate fixes (Hermes feeds UPGRADE_AVAILABLE, unknown != current, merge-base 'before' pins)]] - degree 2, connects to 1 community
