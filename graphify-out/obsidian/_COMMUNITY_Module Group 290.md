---
type: community
cohesion: 0.14
members: 15
---

# Module Group 290

**Cohesion:** 0.14 - loosely connected
**Members:** 15 nodes

## Members
- [[ApprovalQueue Missing Telegram Notifications (Critical Gap)]] - rationale - docs/security/v0.8.0-wiring-audit.md
- [[Confirmed Wired Inbound Pipeline Modules (RBAC, SessionIsolation, PromptGuard, etc.)]] - document - docs/security/v0.8.0-wiring-audit.md
- [[Denial of Service Threats (Resource Exhaustion  Context Window Stuffing)]] - document - docs/security/threat-model.md
- [[EgressTelegramNotifier — Not Instantiated (Critical Gap)]] - rationale - docs/security/v0.8.0-wiring-audit.md
- [[Elevation of Privilege Threats (Prompt Injection  Container Escape  Docker Socket)]] - document - docs/security/threat-model.md
- [[EnhancedToolResultSanitizer Not Passed to Pipeline (Critical Gap)]] - rationale - docs/security/v0.8.0-wiring-audit.md
- [[Information Disclosure Threats (PII  SSRF  DNS Exfil)]] - document - docs/security/threat-model.md
- [[LLMProxy Never Instantiated (Critical Gap)]] - rationale - docs/security/v0.8.0-wiring-audit.md
- [[OutputCanary Not Passed to Pipeline (Critical Gap)]] - rationale - docs/security/v0.8.0-wiring-audit.md
- [[STRIDE Threat Model]] - document - docs/security/threat-model.md
- [[Spoofing Threats (Agent Identity  API Key)]] - document - docs/security/threat-model.md
- [[Tampering Threats (Audit Log  Config Drift)]] - document - docs/security/threat-model.md
- [[Threat Scoring Matrix]] - concept - docs/security/threat-model.md
- [[v0.8.0 Fix Priority List (P0–P3)]] - rationale - docs/security/v0.8.0-wiring-audit.md
- [[v0.8.0 Wiring Audit (Watchtower)]] - document - docs/security/v0.8.0-wiring-audit.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_290
SORT file.name ASC
```
