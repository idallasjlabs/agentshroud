---
type: community
cohesion: 0.10
members: 32
---

# OutputSchemaEnforcer

**Cohesion:** 0.10 - loosely connected
**Members:** 32 nodes

## Members
- [[AgentShroud-Side Remediation (Arm 2)]] - concept - prompts/sunday-upgrade.md
- [[ColimaDocker VM Storage Exhaustion]] - concept - reports/upgrade-2026-09-06-prod.md
- [[Dev-to-Prod Handoff Contract]] - concept - scripts/sunday-upgrade-apply.sh
- [[Phantom Tag Bug Class (scanningbuilding a version tag that is not the one actually running)]] - rationale - prompts/sunday-upgrade.md
- [[Seven-Week No-Op Upgrade Failure (PASS reported while upgrading nothing)]] - rationale - prompts/sunday-upgrade.md
- [[State-Change-Not-Steps Mandate]] - concept - prompts/sunday-upgrade.md
- [[Sunday Run Jira Tracking Procedure]] - concept - prompts/sunday-upgrade.md
- [[Sunday Upgrade Report 2026-08-30 (0734 first-pass abort)]] - document - reports/upgrade-2026-08-30-20260830-2009.md
- [[Sunday Upgrade Report 2026-08-30 (final)]] - document - reports/upgrade-2026-08-30.md
- [[Sunday Upgrade Report 2026-08-30 (local-llms upgrade requested)]] - document - reports/upgrade-2026-08-30-20260830-2010.md
- [[Sunday Upgrade Report 2026-09-06 (dev-only scoped run)]] - document - reports/upgrade-2026-09-06-dev.md
- [[Sunday Upgrade Report 2026-09-06 (dev-only, duplicate)]] - document - reports/upgrade-2026-09-06.md
- [[Sunday Upgrade Report 2026-09-06 (prod read-only, pre-crisis)]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[Sunday Upgrade Report 2026-09-06 (prod, disk-exhaustion incident)]] - document - reports/upgrade-2026-09-06-prod.md
- [[Sunday Upgrade Report 2026-09-14 (dev account)]] - document - reports/upgrade-2026-09-14.md
- [[Sunday Upgrade Report Hermes-cron Delivery]] - code - scripts/hermes-cron/sunday-upgrade-report.sh
- [[Wazuh-Agent Sidecar Split (SIDECAR-GAP-001 resolution)]] - concept - reports/upgrade-2026-09-06-prod.md
- [[_run_cleanup()]] - code - scripts/check-vendor-compat.sh
- [[check-vendor-compat.sh]] - code - scripts/check-vendor-compat.sh
- [[check-vendor-compat.sh script]] - code - scripts/check-vendor-compat.sh
- [[check_hermes()]] - code - scripts/check-vendor-compat.sh
- [[check_openclaw()]] - code - scripts/check-vendor-compat.sh
- [[fail()_3]] - code - scripts/check-vendor-compat.sh
- [[op-to-keychain.sh]] - code - scripts/op-to-keychain.sh
- [[op-to-keychain.sh script]] - code - scripts/op-to-keychain.sh
- [[pass()_2]] - code - scripts/check-vendor-compat.sh
- [[scriptsdiscover_upstream_versions.py]] - concept - prompts/sunday-upgrade.md
- [[scriptssunday-upgrade-apply.sh]] - concept - prompts/sunday-upgrade.md
- [[scriptstriage-cve-mitigations.py]] - concept - prompts/sunday-upgrade.md
- [[sunday-upgrade]] - document - prompts/sunday-upgrade.md
- [[sunday-upgrade.sh (remote-control launcher)]] - code - scripts/sunday-upgrade.sh
- [[warn()_2]] - code - scripts/check-vendor-compat.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OutputSchemaEnforcer
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_DraftEntry]]
- 4 edges to [[_COMMUNITY_AgentShroud v0.7.0 Enforcement Audit Results]]
- 2 edges to [[_COMMUNITY__seed_cron]]
- 1 edge to [[_COMMUNITY_MCPServerConfig]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_Recommendations for Production Deployment]]
- 1 edge to [[_COMMUNITY_2. Security Analysis]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]

## Top bridge nodes
- [[check-vendor-compat.sh]] - degree 12, connects to 3 communities
- [[sunday-upgrade]] - degree 10, connects to 2 communities
- [[Sunday Upgrade Report 2026-09-14 (dev account)]] - degree 5, connects to 2 communities
- [[check_openclaw()]] - degree 8, connects to 1 community
- [[Sunday Upgrade Report 2026-09-06 (prod, disk-exhaustion incident)]] - degree 7, connects to 1 community