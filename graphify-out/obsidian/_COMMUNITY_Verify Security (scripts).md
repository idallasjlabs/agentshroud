---
type: community
cohesion: 0.29
members: 12
---

# Verify Security (scripts)

**Cohesion:** 0.29 - loosely connected
**Members:** 12 nodes

## Members
- [[AgentShroud Seccomp Profile (default-deny syscall allowlist)]] - document - docker/seccomp/agentshroud-seccomp.json
- [[AgentShroud Security Verification (13-check driver)]] - code - docker/scripts/verify-security.sh
- [[OpenClaw Volume Architecture (persistent volumes vs tmpfs)]] - concept - docs/architecture/OPENCLAW_WRITE_REQUIREMENTS.md
- [[Phase 3 Container Security Hardening Baseline]] - concept - docs/architecture/PHASE3_REQUIREMENTS.md
- [[Phase 3 Success Criteria]] - concept - docs/architecture/PHASE3_REQUIREMENTS.md
- [[Read-Only Root FS Constraint — what breaks without proper mounts]] - rationale - docs/architecture/OPENCLAW_WRITE_REQUIREMENTS.md
- [[check_fail()_1]] - code - docker/scripts/verify-security.sh
- [[check_pass()_1]] - code - docker/scripts/verify-security.sh
- [[check_warn()]] - code - docker/scripts/verify-security.sh
- [[toggle-readonly.sh mode switcher]] - code - docker/scripts/toggle-readonly.sh
- [[verify-security.sh]] - code - docker/scripts/verify-security.sh
- [[verify-security.sh script]] - code - docker/scripts/verify-security.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Verify_Security_scripts
SORT file.name ASC
```
