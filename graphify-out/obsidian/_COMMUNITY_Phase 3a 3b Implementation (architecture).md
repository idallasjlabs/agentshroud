---
type: community
cohesion: 0.06
members: 32
---

# Phase 3a 3b Implementation (architecture)

**Cohesion:** 0.06 - loosely connected
**Members:** 32 nodes

## Members
- [[3A.1 Re-enable seccomp profiles ✅]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[3A.2 Make OpenClaw container read-only ✅]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[3A.3 Remove NET_RAW capability ✅]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[3A.4 Add mDNSBonjour disable ✅]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[3A.5 Move gateway password to Docker secrets ✅]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[3A.6 Create verify-security.sh ✅]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[3A.7 Create scan.sh (OpenSCAP) ✅]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[3A.8 Change DM policy to allowlist ✅]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[3B.1 Create killswitch.sh ✅]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[Created]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[DM Policy Allowlist Configuration]] - concept - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[Disable seccomp (if causing startup failures)]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[Emergency container access]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[Files Changed]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[Gateway Password Moved to Docker Secrets]] - rationale - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[Kill Switch (freeze  shutdown  disconnect)]] - concept - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[Modified]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[NET_RAW Capability Removal]] - rationale - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[Next Steps_2]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[No Changes (Already Correct)]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[PHASE_3A_3B_IMPLEMENTATION]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[Phase 3A Testing]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[Phase 3A Security Completion (COMPLETE)]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[Phase 3B.1 Testing]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[Phase 3B.1 Kill Switch (COMPLETE)]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[Pre-Test Preparation]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[Re-enable Seccomp Profiles (ARM64 syscalls)]] - rationale - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[Restore hardcoded gateway password (if secret mounting fails)]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[Rollback Plan]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[Security Improvements Summary]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[Testing Checklist]] - document - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md
- [[verify-security.sh (13 Security Checks)]] - concept - docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Phase_3a_3b_Implementation_architecture
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_06 Operations (diagrams)]]
- 1 edge to [[_COMMUNITY_07 Team Planning (diagrams)]]
- 1 edge to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 1 edge to [[_COMMUNITY_Per Agent Isolation (architecture)]]
- 1 edge to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 1 edge to [[_COMMUNITY_Killswitch Monitor & Observatory Mode]]

## Top bridge nodes
- [[Kill Switch (freeze  shutdown  disconnect)]] - degree 3, connects to 2 communities
- [[PHASE_3A_3B_IMPLEMENTATION]] - degree 14, connects to 1 community
- [[DM Policy Allowlist Configuration]] - degree 2, connects to 1 community
- [[Gateway Password Moved to Docker Secrets]] - degree 2, connects to 1 community
- [[NET_RAW Capability Removal]] - degree 2, connects to 1 community