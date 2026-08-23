---
type: community
cohesion: 0.11
members: 18
---

# Container Security Audit V0.8.0 (v0.8)

**Cohesion:** 0.11 - loosely connected
**Members:** 18 nodes

## Members
- [[Architecture_7]] - document - docs/planning/v0.8/container-security-audit-v0.8.0.md
- [[Audit Methodology]] - document - docs/planning/v0.8/container-security-audit-v0.8.0.md
- [[Colima VM Networking]] - document - docs/planning/v0.8/container-security-audit-v0.8.0.md
- [[Container Security Audit — AgentShroud v0.8.0]] - document - docs/planning/v0.8/container-security-audit-v0.8.0.md
- [[Controls Summary]] - document - docs/planning/v0.8/container-security-audit-v0.8.0.md
- [[Findings & Mitigations]] - document - docs/planning/v0.8/container-security-audit-v0.8.0.md
- [[Items Pending Image Rebuild]] - document - docs/planning/v0.8/container-security-audit-v0.8.0.md
- [[container-security-audit-v0.8.0]] - document - docs/planning/v0.8/container-security-audit-v0.8.0.md
- [[🔴 C1 SSH Config Bypass (`-F devnull`)]] - document - docs/planning/v0.8/container-security-audit-v0.8.0.md
- [[🔴 C2 Raw TCP to Host Port 22]] - document - docs/planning/v0.8/container-security-audit-v0.8.0.md
- [[🔴 C3 PID1 Environment Readable (`proc1environ`)]] - document - docs/planning/v0.8/container-security-audit-v0.8.0.md
- [[🟠 H1 Writable `~.ssh` Directory]] - document - docs/planning/v0.8/container-security-audit-v0.8.0.md
- [[🟠 H2 Secrets in Environment Variables]] - document - docs/planning/v0.8/container-security-audit-v0.8.0.md
- [[🟠 H3 `resolv.conf` Leaks DNS Architecture]] - document - docs/planning/v0.8/container-security-audit-v0.8.0.md
- [[🟠 H4 All Internal Container Ports Reachable]] - document - docs/planning/v0.8/container-security-audit-v0.8.0.md
- [[🟡 M1 `apt` Available (Permissions Blocked)]] - document - docs/planning/v0.8/container-security-audit-v0.8.0.md
- [[🟡 M2 `perl` and `bash` Available as Interpreters]] - document - docs/planning/v0.8/container-security-audit-v0.8.0.md
- [[🟡 M3 `proc1ns` Namespace Files Visible]] - document - docs/planning/v0.8/container-security-audit-v0.8.0.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Container_Security_Audit_V080_v08
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Blue Team Assessment V0.8.0 (v0.8)]]
- 1 edge to [[_COMMUNITY_Enforcement Audit V0.7.0 (reviews)]]

## Top bridge nodes
- [[Container Security Audit — AgentShroud v0.8.0]] - degree 9, connects to 2 communities