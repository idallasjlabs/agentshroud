---
type: community
members: 8
---

# docs/governance

**Members:** 8 nodes

## Members
- [[ApprovalQueue Missing Telegram Notifications (Critical Gap)]] - rationale - docs/security/v0.8.0-wiring-audit.md
- [[Confirmed Wired Inbound Pipeline Modules (RBAC, SessionIsolation, PromptGuard, etc.)]] - document - docs/security/v0.8.0-wiring-audit.md
- [[EgressTelegramNotifier — Not Instantiated (Critical Gap)]] - rationale - docs/security/v0.8.0-wiring-audit.md
- [[EnhancedToolResultSanitizer Not Passed to Pipeline (Critical Gap)]] - rationale - docs/security/v0.8.0-wiring-audit.md
- [[LLMProxy Never Instantiated (Critical Gap)]] - rationale - docs/security/v0.8.0-wiring-audit.md
- [[OutputCanary Not Passed to Pipeline (Critical Gap)]] - rationale - docs/security/v0.8.0-wiring-audit.md
- [[v0.8.0 Fix Priority List (P0–P3)]] - rationale - docs/security/v0.8.0-wiring-audit.md
- [[v0.8.0 Wiring Audit (Watchtower)]] - document - docs/security/v0.8.0-wiring-audit.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/docs/governance
SORT file.name ASC
```
