---
type: community
members: 51
---

# upgrade-2026-10-12.md

**Members:** 51 nodes

## Members
- [[1. Summary line_3]] - document - reports/upgrade-2026-10-12.md
- [[1. Summary line_4]] - document - reports/upgrade-2026-10-18.md
- [[2. Environment mapping_2]] - document - reports/upgrade-2026-10-12.md
- [[2. Environment mapping_3]] - document - reports/upgrade-2026-10-18.md
- [[3. Upgrade table_1]] - document - reports/upgrade-2026-10-12.md
- [[3. Upgrade table_2]] - document - reports/upgrade-2026-10-18.md
- [[3a. Per-component change report_1]] - document - reports/upgrade-2026-10-18.md
- [[3b. Not updated this run — plan for the week_2]] - document - reports/upgrade-2026-10-18.md
- [[4. Security findings_1]] - document - reports/upgrade-2026-10-12.md
- [[4. Security findings_2]] - document - reports/upgrade-2026-10-18.md
- [[5. Verification evidence_1]] - document - reports/upgrade-2026-10-12.md
- [[5. Verification evidence_2]] - document - reports/upgrade-2026-10-18.md
- [[6. Breaking changes  needs human_1]] - document - reports/upgrade-2026-10-12.md
- [[6. Breaking changes  needs human_2]] - document - reports/upgrade-2026-10-18.md
- [[7. Rollback instructions_1]] - document - reports/upgrade-2026-10-12.md
- [[7. Rollback instructions_2]] - document - reports/upgrade-2026-10-18.md
- [[8. Time spent_1]] - document - reports/upgrade-2026-10-12.md
- [[8. Time spent_2]] - document - reports/upgrade-2026-10-18.md
- [[Base docker-compose stack]] - code - docker/docker-compose.yml
- [[Compose network version-label mismatch forces network recreate]] - concept - reports/upgrade-2026-10-12.md
- [[Coverage gateway-side mitigation (owner directive — vendor patch is not the finish line)]] - document - reports/upgrade-2026-10-12.md
- [[Features Prompt Injection Defense, PII Sanitization, Egress Filtering, Human-in-the-Loop, IEC 62443]] - concept - docs/index.html
- [[GitHub Actions version inventory (first time in scope)]] - concept - reports/upgrade-2026-10-12.md
- [[Hermes v0.22.2 held back (A2A 9900 unreachable)]] - concept - reports/upgrade-2026-10-18.md
- [[Hermes — stays on 0.21.5, wanted v0.22.2]] - document - reports/upgrade-2026-10-18.md
- [[Host trivy cannot reach registries]] - document - reports/upgrade-2026-10-18.md
- [[Host trivy cannot reach registries (scans_failed=3 root cause)]] - concept - reports/upgrade-2026-10-18.md
- [[Marvin dev compose override (agentshroud-bot)]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[Non-agent components not inventoried]] - concept - reports/upgrade-2026-10-18.md
- [[OpenClaw 2026.10.2 - 2026.10.4 upgrade (dev)]] - concept - reports/upgrade-2026-10-18.md
- [[OpenClaw — 2026.10.2 → 2026.10.4 (dev)]] - document - reports/upgrade-2026-10-18.md
- [[Presidio PII detection deps (analyzeranonymizerspacy)]] - code - gateway/requirements.txt
- [[Prod promotion BLOCKED (0800 window)]] - concept - reports/upgrade-2026-10-18.md
- [[Progress log (dev run, whoami=agentshroud-bot)]] - document - reports/upgrade-2026-10-18.md
- [[Rest of the inventory — not checked against upstream]] - document - reports/upgrade-2026-10-18.md
- [[S5 docker-compose.yml does not bind port 8080 to 0.0.0.0]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[Sunday Upgrade 2026-10-12 — DEV run (on-demand, owner-requested pipeline-hardening exercise)]] - document - reports/upgrade-2026-10-12.md
- [[Sunday Upgrade 2026-10-18 (DEV run, whoami=agentshroud-bot)]] - document - reports/upgrade-2026-10-18.md
- [[Tap-approval pipeline (PR 502)]] - concept - reports/upgrade-2026-10-12.md
- [[Transitive-dependency security floors (pip-audit gate)]] - rationale - gateway/requirements.txt
- [[Two-pass pip-audit (bump, re-audit, bump again)]] - rationale - reports/upgrade-2026-10-12.md
- [[gatewayrequirements.txt]] - code - gateway/requirements.txt
- [[python-jose removal (CVE-2024-3366333664)]] - rationale - gateway/requirements.txt
- [[sunday-rollback.sh]] - code - scripts/sunday-rollback.sh
- [[sunday-rollback.sh script]] - code - scripts/sunday-rollback.sh
- [[sunday-upgrade-approve.sh]] - code - scripts/sunday-upgrade-approve.sh
- [[sunday-upgrade-approve.sh script]] - code - scripts/sunday-upgrade-approve.sh
- [[sunday-upgrade]] - document - prompts/sunday-upgrade.md
- [[upgrade-2026-10-12]] - document - reports/upgrade-2026-10-12.md
- [[upgrade-2026-10-18]] - document - reports/upgrade-2026-10-18.md
- [[websockets 16.1.1 - 17.1 Sunday upgrade bump]] - rationale - gateway/requirements.txt

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/upgrade-2026-10-12md
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_upgrade-2026-09-21]]
- 2 edges to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 2 edges to [[_COMMUNITY_check-vendor-compat.sh]]
- 1 edge to [[_COMMUNITY_Procedure]]
- 1 edge to [[_COMMUNITY_plan_remediation]]
- 1 edge to [[_COMMUNITY_discover_upstream_versions.py]]

## Top bridge nodes
- [[sunday-upgrade]] - degree 7, connects to 3 communities
- [[upgrade-2026-10-18]] - degree 10, connects to 2 communities
- [[Base docker-compose stack]] - degree 6, connects to 2 communities
- [[upgrade-2026-10-12]] - degree 11, connects to 1 community
- [[OpenClaw 2026.10.2 - 2026.10.4 upgrade (dev)]] - degree 2, connects to 1 community
