---
type: community
cohesion: 0.12
members: 17
---

# format_upstream_cve_alert()

**Cohesion:** 0.12 - loosely connected
**Members:** 17 nodes

## Members
- [[Base-Image Change Flagged For Decision, Not Attempted]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Currently Unmitigable Residual Class]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Dev-Side Copy of the 2026-09-06 Report]] - document - reports/upgrade-2026-09-06-dev.md
- [[DevProd Mapping Keyed Off $USER via scriptsasb]] - rationale - reports/upgrade-2026-09-06.md
- [[Governed Voice Path (device to gateway to Hermes)]] - concept - firmware/voice-terminal/SETUP.md
- [[Hermes Vendored-Base Residual (upstream-owned)]] - rationale - docs/security/cve-mitigation-matrix.md
- [[One-Cause-Per-Failure Bring-Up Order]] - rationale - firmware/voice-terminal/SETUP.md
- [[OpenClaw BLOCKED — nodesqlite NUL Truncation]] - rationale - reports/upgrade-2026-09-14.md
- [[Post-Rebuild CVE Rescan Delta (40 to 22 CRITICAL)]] - concept - reports/upgrade-2026-09-14.md
- [[Reachability Context (cap_drop ALL, isolated network)]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Spoken High-Risk Command Approval Pause]] - rationale - firmware/voice-terminal/SETUP.md
- [[Sunday Upgrade 2026-09-06 (dev-only scoped run)]] - document - reports/upgrade-2026-09-06.md
- [[Tailscale Funnel Exposure (supersedes on-device client)]] - rationale - firmware/voice-terminal/SETUP.md
- [[Two-Terminal-State Finding Taxonomy]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Voice Gateway Service (STTTTS on marvin)]] - concept - firmware/voice-terminal/SETUP.md
- [[Voice-Gateway Bookworm Rebase Measured And Reverted]] - rationale - reports/upgrade-2026-09-06.md
- [[Zeroed .trivyignore (no suppressions)]] - rationale - docs/security/cve-mitigation-matrix.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/format_upstream_cve_alert
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_AgentShroud™ CVE Mitigation Matrix]]
- 1 edge to [[_COMMUNITY_Slack Channel Setup (2)]]
- 1 edge to [[_COMMUNITY_hermesskillsi-icloudscriptscalendar.js]]
- 1 edge to [[_COMMUNITY_test_prompt_guard.py (2)]]

## Top bridge nodes
- [[Currently Unmitigable Residual Class]] - degree 6, connects to 1 community
- [[Governed Voice Path (device to gateway to Hermes)]] - degree 4, connects to 1 community
- [[OpenClaw BLOCKED — nodesqlite NUL Truncation]] - degree 3, connects to 1 community
- [[Post-Rebuild CVE Rescan Delta (40 to 22 CRITICAL)]] - degree 2, connects to 1 community
