---
type: community
cohesion: 0.04
members: 62
---

# chatbot/main.py

**Cohesion:** 0.04 - loosely connected
**Members:** 62 nodes

## Members
- [[NOTE api.telegram.org is intentionally NOT listed here.  The bot is]] - rationale - gateway/proxy/http_proxy.py
- [[AGENTSHROUD_MODE_1]] - document - docs/vault/04 - Environment Variables/AGENTSHROUD_MODE.md
- [[AGENTSHROUD_MODE]] - document - docs/vault/04 - Environment Variables/AGENTSHROUD_MODE.md
- [[Affected Modules]] - document - docs/vault/04 - Environment Variables/AGENTSHROUD_MODE.md
- [[AgentShroud App Icon (64x64)]] - image - branding/icons/app/icon-64x64.png
- [[AgentShroud BadgeAvatar Logo Variant (120x120)]] - image - branding/logos/variants/badge-120x120.png
- [[AgentShroud Brand Collateral Mockup]] - image - branding/logos/png/logo-mockup.png
- [[AgentShroud Logo (SVG Wrapper, Embedded Raster)]] - image - branding/logos/svg/logo.svg
- [[AgentShroud Logo - GlowTransparent Variant]] - image - branding/logos/png/logo-transparent.png
- [[AgentShroud Primary Logo Lockup]] - image - branding/logos/png/logo.png
- [[AgentShroud Semgrep SAST Configuration]] - document - .semgrep.yml
- [[AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]] - image - branding/icons/app/icon-macos-rounded-1024x1024.png
- [[Audit Ledger Module Badge Icon]] - image - branding/icons/modules/audit-ledger-256x256.png
- [[Behavior_1]] - document - docs/vault/04 - Environment Variables/AGENTSHROUD_MODE.md
- [[Checklist]] - document - .github/PULL_REQUEST_TEMPLATE.md
- [[Credential Isolation Module Badge Icon]] - image - branding/icons/modules/credential-iso-256x256.png
- [[Description_1]] - document - docs/vault/04 - Environment Variables/AGENTSHROUD_MODE.md
- [[Drift Detector Module Badge Icon]] - image - branding/icons/modules/drift-detector-256x256.png
- [[Egress Filter Module Badge Icon]] - image - branding/icons/modules/egress-filter-256x256.png
- [[Encrypted Store Module Badge Icon]] - image - branding/icons/modules/encrypted-store-256x256.png
- [[FR1 Identification and Authentication Control]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR3 System Integrity]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR5 Restricted Data Flow]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR6 Timely Response to Events]] - concept - docs/compliance/iec-62443-matrix.md
- [[HTTP Proxy Module Badge Icon]] - image - branding/icons/modules/http-proxy-256x256.png
- [[IEC 62443 Reference]] - document - .github/PULL_REQUEST_TEMPLATE.md
- [[PII Sanitizer Module Badge Icon]] - image - branding/icons/modules/pii-sanitizer-256x256.png
- [[PULL_REQUEST_TEMPLATE]] - document - .github/PULL_REQUEST_TEMPLATE.md
- [[Prompt Guard Module Badge Icon]] - image - branding/icons/modules/prompt-guard-256x256.png
- [[Related Notes_29]] - document - docs/vault/04 - Environment Variables/AGENTSHROUD_MODE.md
- [[Rule agentshroud-assert-security-check]] - concept - .semgrep.yml
- [[Rule agentshroud-hardcoded-password]] - concept - .semgrep.yml
- [[Rule agentshroud-log-sensitive-key]] - concept - .semgrep.yml
- [[Rule agentshroud-pickle-load]] - concept - .semgrep.yml
- [[Rule agentshroud-sql-injection]] - concept - .semgrep.yml
- [[Rule agentshroud-ssrf-httpx]] - concept - .semgrep.yml
- [[Rule agentshroud-ssrf-requests]] - concept - .semgrep.yml
- [[Rule agentshroud-subprocess-shell-true]] - concept - .semgrep.yml
- [[Rule agentshroud-subprocess-unvalidated-input]] - concept - .semgrep.yml
- [[SSH Proxy Module Badge Icon]] - image - branding/icons/modules/ssh-proxy-256x256.png
- [[Startup Warnings]] - document - docs/vault/04 - Environment Variables/AGENTSHROUD_MODE.md
- [[Summary]] - document - .github/PULL_REQUEST_TEMPLATE.md
- [[Trust Manager Module Badge Icon]] - image - branding/icons/modules/trust-manager-256x256.png
- [[Type of Change]] - document - .github/PULL_REQUEST_TEMPLATE.md
- [[Usage_126]] - document - docs/vault/04 - Environment Variables/AGENTSHROUD_MODE.md
- [[Values_2]] - document - docs/vault/04 - Environment Variables/AGENTSHROUD_MODE.md
- [[assert-security-check rule (CWE-617)]] - rationale - .semgrep.yml
- [[config_integrity.py]] - code - gateway/security/config_integrity.py
- [[egress_filter.py]] - code - gateway/security/egress_filter.py
- [[hardcoded-password rule (CWE-798)]] - rationale - .semgrep.yml
- [[heuristic_classifier.py]] - code - gateway/security/heuristic_classifier.py
- [[http_proxy.py]] - code - gateway/proxy/http_proxy.py
- [[iec-62443-matrix]] - document - docs/compliance/iec-62443-matrix.md
- [[log-sensitive-key rule (CWE-532)]] - rationale - .semgrep.yml
- [[path-traversal-open rule (CWE-22)]] - rationale - .semgrep.yml
- [[pickle-load rule (CWE-502)]] - rationale - .semgrep.yml
- [[prompt_guard.py]] - code - gateway/security/prompt_guard.py
- [[sql-injection rule (CWE-89)]] - rationale - .semgrep.yml
- [[ssrf-httpx rule (CWE-918)]] - rationale - .semgrep.yml
- [[ssrf-requests rule (CWE-918)]] - rationale - .semgrep.yml
- [[subprocess-shell-true rule (CWE-78)]] - rationale - .semgrep.yml
- [[subprocess-unvalidated-input rule (CWE-78)]] - rationale - .semgrep.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/chatbot/mainpy
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_EncryptedStore]]
- 4 edges to [[_COMMUNITY_AuditStore]]
- 4 edges to [[_COMMUNITY_ConsentFramework]]
- 3 edges to [[_COMMUNITY__wrap_response()]]
- 3 edges to [[_COMMUNITY_EgressPolicy]]
- 3 edges to [[_COMMUNITY_SkillGuard]]
- 3 edges to [[_COMMUNITY_Production Safety Checklist (SKILL)]]
- 3 edges to [[_COMMUNITY_GroupApprovalRouter]]
- 3 edges to [[_COMMUNITY_ServiceManager]]
- 2 edges to [[_COMMUNITY_SOCWebSocketHandler]]
- 2 edges to [[_COMMUNITY_test_runtime_engines.py]]
- 2 edges to [[_COMMUNITY_load_config()]]
- 2 edges to [[_COMMUNITY_URLAnalyzer]]
- 2 edges to [[_COMMUNITY_BotConfig]]
- 2 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_lvgl_kawaii_face.c]]
- 1 edge to [[_COMMUNITY_TestCollaboratorPromptClassifiers]]
- 1 edge to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]
- 1 edge to [[_COMMUNITY_StdioConnection]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_GitGuard]]
- 1 edge to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_AgentShroud Access Control Matrix]]
- 1 edge to [[_COMMUNITY_test_soc_router_coverage.py]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_ReportStore]]
- 1 edge to [[_COMMUNITY_EgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_test_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_FileSandbox]]
- 1 edge to [[_COMMUNITY_3. Security Controls]]
- 1 edge to [[_COMMUNITY_archive_old_events()]]
- 1 edge to [[_COMMUNITY_TestApprovalHardening]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_GSDE&G Development Master Checklist]]
- 1 edge to [[_COMMUNITY_IntelReportStore]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_CollaboratorGreeter]]
- 1 edge to [[_COMMUNITY_CredentialInjector]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_gateway.security.agent_cve_registry]]
- 1 edge to [[_COMMUNITY_TestAuth]]
- 1 edge to [[_COMMUNITY_format_upstream_cve_alert()]]
- 1 edge to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_RuntimeConfig]]
- 1 edge to [[_COMMUNITY_Function Details]]

## Top bridge nodes
- [[egress_filter.py]] - degree 27, connects to 14 communities
- [[http_proxy.py]] - degree 16, connects to 12 communities
- [[prompt_guard.py]] - degree 18, connects to 10 communities
- [[AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]] - degree 16, connects to 4 communities
- [[FR3 System Integrity]] - degree 9, connects to 4 communities