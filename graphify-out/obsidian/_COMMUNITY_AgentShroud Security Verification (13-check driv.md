---
type: community
cohesion: 0.23
members: 14
---

# AgentShroud Security Verification (13-check driv

**Cohesion:** 0.23 - loosely connected
**Members:** 14 nodes

## Members
- [[AgentShroud Seccomp Profile (default-deny syscall allowlist)]] - document - docker/seccomp/agentshroud-seccomp.json
- [[AgentShroud Security Verification (13-check driver)]] - code - docker/scripts/verify-security.sh
- [[OpenClaw Volume Architecture (persistent volumes vs tmpfs)]] - concept - docs/architecture/OPENCLAW_WRITE_REQUIREMENTS.md
- [[Phase 3 Container Security Hardening Baseline]] - concept - docs/architecture/PHASE3_REQUIREMENTS.md
- [[Phase 3 Success Criteria]] - concept - docs/architecture/PHASE3_REQUIREMENTS.md
- [[Read-Only Root FS Constraint — what breaks without proper mounts]] - rationale - docs/architecture/OPENCLAW_WRITE_REQUIREMENTS.md
- [[SecureClaw Security Review (SEC)]] - document - .agents/skills/i-sec/SKILL.md
- [[Security Review (SEC) README]] - document - .agents/skills/i-sec/README.md
- [[check_fail()_1]] - code - docker/scripts/verify-security.sh
- [[check_pass()_1]] - code - docker/scripts/verify-security.sh
- [[check_warn()]] - code - docker/scripts/verify-security.sh
- [[toggle-readonly.sh mode switcher]] - code - docker/scripts/toggle-readonly.sh
- [[verify-security.sh_1]] - code - docker/scripts/verify-security.sh
- [[verify-security.sh script]] - code - docker/scripts/verify-security.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Security_Verification_13-check_driv
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_redteam_probes.py]]

## Top bridge nodes
- [[SecureClaw Security Review (SEC)]] - degree 3, connects to 1 community