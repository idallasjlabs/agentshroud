---
type: community
cohesion: 0.12
members: 16
---

# pick_latest_hermes_tag()

**Cohesion:** 0.12 - loosely connected
**Members:** 16 nodes

## Members
- [[Container-Image CVE Domain (our own images)]] - concept - docs/security/cve-mitigation-matrix.md
- [[Currently Unmitigable Residual Class]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Fresh-DB vs Cached-DB Trivy Verification]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Governed Voice Path (device to gateway to Hermes)]] - concept - firmware/voice-terminal/SETUP.md
- [[Hermes Vendored-Base Residual (upstream-owned)]] - rationale - docs/security/cve-mitigation-matrix.md
- [[One-Cause-Per-Failure Bring-Up Order]] - rationale - firmware/voice-terminal/SETUP.md
- [[Post-Rebuild CVE Rescan Delta (40 to 22 CRITICAL)]] - concept - reports/upgrade-2026-09-14.md
- [[Reachability Context (cap_drop ALL, isolated network)]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Spoken High-Risk Command Approval Pause]] - rationale - firmware/voice-terminal/SETUP.md
- [[Tailscale Funnel Exposure (supersedes on-device client)]] - rationale - firmware/voice-terminal/SETUP.md
- [[Transitive-Dependency Security Floors]] - rationale - gateway/requirements.txt
- [[Two-Terminal-State Finding Taxonomy]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Voice Gateway Service (STTTTS on marvin)]] - concept - firmware/voice-terminal/SETUP.md
- [[Zeroed .trivyignore (no suppressions)]] - rationale - docs/security/cve-mitigation-matrix.md
- [[python-jose Removal (CVE-2024-3366333664)]] - rationale - gateway/requirements.txt
- [[slsa-verifier From-Source Dependency Override]] - concept - docs/security/cve-mitigation-matrix.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/pick_latest_hermes_tag
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_TestCheckCommandExecution]]
- 1 edge to [[_COMMUNITY_mcp-proxy-wrapper.js]]
- 1 edge to [[_COMMUNITY_start.sh]]
- 1 edge to [[_COMMUNITY_Container Security Policy — AgentShroud]]

## Top bridge nodes
- [[Currently Unmitigable Residual Class]] - degree 7, connects to 2 communities
- [[Container-Image CVE Domain (our own images)]] - degree 4, connects to 1 community
- [[Governed Voice Path (device to gateway to Hermes)]] - degree 4, connects to 1 community
- [[Post-Rebuild CVE Rescan Delta (40 to 22 CRITICAL)]] - degree 2, connects to 1 community