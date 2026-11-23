---
type: community
members: 7
---

# AgentShroud Security Verification (13-check driver)

**Members:** 7 nodes

## Members
- [[AgentShroud Seccomp Profile (default-deny syscall allowlist)]] - document - docker/seccomp/agentshroud-seccomp.json
- [[AgentShroud Security Verification (13-check driver)]] - code - docker/scripts/verify-security.sh
- [[OpenClaw Volume Architecture (persistent volumes vs tmpfs)]] - concept - docs/architecture/OPENCLAW_WRITE_REQUIREMENTS.md
- [[Phase 3 Container Security Hardening Baseline]] - concept - docs/architecture/PHASE3_REQUIREMENTS.md
- [[Phase 3 Success Criteria]] - concept - docs/architecture/PHASE3_REQUIREMENTS.md
- [[Read-Only Root FS Constraint — what breaks without proper mounts]] - rationale - docs/architecture/OPENCLAW_WRITE_REQUIREMENTS.md
- [[toggle-readonly.sh mode switcher]] - code - docker/scripts/toggle-readonly.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Security_Verification_13-check_driver
SORT file.name ASC
```
