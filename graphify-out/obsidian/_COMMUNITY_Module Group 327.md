---
type: community
cohesion: 0.18
members: 12
---

# Module Group 327

**Cohesion:** 0.18 - loosely connected
**Members:** 12 nodes

## Members
- [[Container Hardening Controls (cap_drop ALL, seccomp, read-only FS, non-root, resource limits)]] - concept - docs/security/container-policy.md
- [[Incident Severity Levels (P1 Critical 15min, P2 High 1hr, P3 Medium 4hr, P4 Low 24hr)]] - concept - docs/security/incident-response.md
- [[Kill Switch Decision Tree (Freeze → Shutdown → Disconnect based on breach severity)]] - concept - docs/security/incident-response.md
- [[Phase 3A3B Completion Status (seccomp enabled, NET_RAW removed, kill switch implemented)]] - document - docs/security/VERIFICATION_RESULTS.md
- [[SECURITY_SCRIPTS_REFERENCE]] - document - docs/security/SECURITY_SCRIPTS_REFERENCE.md
- [[Secret Management Hierarchy (1Password → Docker Secrets → env vars for non-sensitive only)]] - concept - docs/security/container-policy.md
- [[VERIFICATION_RESULTS.md (Phase 3A3B implementation verification)]] - document - docs/security/VERIFICATION_RESULTS.md
- [[container-policy]] - document - docs/security/container-policy.md
- [[incident-response.md (Incident Response Playbook)]] - document - docs/security/incident-response.md
- [[killswitch.sh (freezeshutdowndisconnect emergency response)]] - document - docs/security/SECURITY_SCRIPTS_REFERENCE.md
- [[scan.sh (OpenSCAP + Docker Bench compliance scan)]] - document - docs/security/SECURITY_SCRIPTS_REFERENCE.md
- [[verify-security.sh (13-check security script)]] - document - docs/security/SECURITY_SCRIPTS_REFERENCE.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_327
SORT file.name ASC
```
