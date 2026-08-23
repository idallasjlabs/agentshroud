---
source_file: "docs/planning/v0.8/v0.8.0-wiring-audit.md"
type: "document"
community: "V0.8.0 Wiring Audit (v0.8)"
location: "L18"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/V080_Wiring_Audit_v08
---

# 🔴 CRITICAL — Not Wired (code exists, tests pass, but NOT running in production)

## Connections
- [[1. EgressTelegramNotifier — Little Snitch Inline Buttons]] - `contains` [EXTRACTED]
- [[2. Approval Queue — Missing Telegram Notifications]] - `contains` [EXTRACTED]
- [[3. OutputCanary — Not Passed to Pipeline]] - `contains` [EXTRACTED]
- [[4. EnhancedToolResultSanitizer — Not Passed to Pipeline]] - `contains` [EXTRACTED]
- [[5. LLMProxy — Never Instantiated]] - `contains` [EXTRACTED]
- [[AgentShroud v0.8.0 Watchtower — Comprehensive Wiring Audit]] - `contains` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/V080_Wiring_Audit_v08