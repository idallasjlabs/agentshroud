---
type: community
cohesion: 0.11
members: 25
---

# DockerEngine

**Cohesion:** 0.11 - loosely connected
**Members:** 25 nodes

## Members
- [[AgentShroud Blue Team Security Auditor (SEC-DEFENSE)]] - document - .agents/skills/i-sec-defense/SKILL.md
- [[AgentShroud Red Team Adversarial Tester (SEC-OFFENSE)]] - document - .agents/skills/i-sec-offense/SKILL.md
- [[AgentShroud Seccomp Profile (default-deny syscall allowlist)]] - document - docker/seccomp/agentshroud-seccomp.json
- [[AgentShroud Security Verification (13-check driver)]] - code - docker/scripts/verify-security.sh
- [[Blue Team Security Auditor README]] - document - .agents/skills/i-sec-defense/README.md
- [[OpenClaw Volume Architecture (persistent volumes vs tmpfs)]] - concept - docs/architecture/OPENCLAW_WRITE_REQUIREMENTS.md
- [[Phase 3 Container Security Hardening Baseline]] - concept - docs/architecture/PHASE3_REQUIREMENTS.md
- [[Phase 3 Success Criteria]] - concept - docs/architecture/PHASE3_REQUIREMENTS.md
- [[Read-Only Root FS Constraint — what breaks without proper mounts]] - rationale - docs/architecture/OPENCLAW_WRITE_REQUIREMENTS.md
- [[Red Team Adversarial Tester README]] - document - .agents/skills/i-sec-offense/README.md
- [[RedactionResult_2]] - code - gateway/security/prompt_protection.py
- [[Result of scanning and redacting content.]] - rationale - gateway/security/prompt_protection.py
- [[STPA-Sec Methodology]] - concept - .agents/skills/i-sec-defense/SKILL.md
- [[SecureClaw Security Review (SEC)]] - document - .agents/skills/i-sec/SKILL.md
- [[Security Review (SEC) README]] - document - .agents/skills/i-sec/README.md
- [[Steve Hay Adversary Model]] - concept - .agents/skills/i-sec-offense/SKILL.md
- [[check_fail()_1]] - code - docker/scripts/verify-security.sh
- [[check_pass()_1]] - code - docker/scripts/verify-security.sh
- [[check_warn()]] - code - docker/scripts/verify-security.sh
- [[docsreviewsblue-team-audit-v0.7.0]] - concept - docs/reviews/blue-team-audit-v0.7.0.md
- [[docsreviewsred-team-report-v0.7.0]] - concept - docs/reviews/red-team-report-v0.7.0.md
- [[prompt_protection.py]] - code - gateway/security/prompt_protection.py
- [[toggle-readonly.sh mode switcher]] - code - docker/scripts/toggle-readonly.sh
- [[verify-security.sh]] - code - docker/scripts/verify-security.sh
- [[verify-security.sh script]] - code - docker/scripts/verify-security.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DockerEngine
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_TrustManager]]
- 3 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 2 edges to [[_COMMUNITY_SSHProxy]]
- 2 edges to [[_COMMUNITY_EncryptedStore]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_load_config()]]
- 1 edge to [[_COMMUNITY_WebProxyConfig]]
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_3. Security Controls]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_ContainerEngine]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_test_jira_weekly_review.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_test_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_version_routes.py]]
- 1 edge to [[_COMMUNITY_Skill UI Expert (UI)]]
- 1 edge to [[_COMMUNITY_test_approval_queue.py]]

## Top bridge nodes
- [[AgentShroud Blue Team Security Auditor (SEC-DEFENSE)]] - degree 27, connects to 17 communities
- [[AgentShroud Red Team Adversarial Tester (SEC-OFFENSE)]] - degree 7, connects to 2 communities
- [[prompt_protection.py]] - degree 5, connects to 2 communities
- [[RedactionResult_2]] - degree 3, connects to 1 community