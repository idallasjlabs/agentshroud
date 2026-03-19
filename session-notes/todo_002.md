# AgentShroud™ Telegram-Reported Issues
**Generated:** 2026-03-09
**Source:** `telegram_history.jsonl`

This document captures issues, bugs, and blockers identified during live interactions between Isaiah Jefferson (@therealidallasj) and the AgentShroud bot (@agentshroud_bot).

---

## 🔴 CRITICAL: System Blockers

### 2. Bot Startup Crash-Loops (Config Errors)
- **Symptoms:** Bots (Pi/Trillian) stuck in "Up 1 second" status.
- **Root Cause:** `apply-patches.js` was injecting invalid configuration values:
    - `"memorySearch": false` (expected object)
    - `"heartbeat": {"enabled": false}` (unrecognized key)
- **Status:** Identified and mitigated by fixing `apply-patches.js` in the repository.

### 3. 1Password Session Expiry (`op-proxy`)
- **Symptoms:** Bots fail to fetch Brave Search API keys; Gateway returns `503 Service Unavailable` for credential requests.
- **Impact:** Bots crash-loop or run with degraded functionality.
- **Context:** Requires manual re-auth on specific hosts (Pi, Trillian).

---

## 🟠 HIGH: Security & Logic Issues

### 5. ContextGuard False Positives (Collaborator Block)
- **Symptoms:** `[BLOCKED BY AGENTSHROUD: Multi-turn disclosure risk exceeded threshold (score=210.00)]`.
- **Impact:** Collaborators (e.g., Steve) are unable to interact with the bot because their benign queries are flagged as disclosure risks.
- **Context:** Identified on Mar 9. Threshold is currently too aggressive for trusted collaborators.

### 7. SMTP Port Blocks (Email Failures)
- **Symptoms:** `⚠️ Daily Competitive Analysis Email — FAILED`.
- **Root Cause:** Sandbox network blocks ports 465 and 587.
- **Impact:** Automated reporting is non-functional in the sandbox environment.
- **Proposed Fixes:** Gmail API (HTTPS/443), host-side relay, or gateway-routed email tool.

---

## 🟡 MEDIUM: Infrastructure & Deployment


## 🔵 LOW: User Experience & Documentation

### 12. Pandoc/LaTeX Dependency Issues
- **Symptoms:** `pdflatex not found. Please select a different --pdf-engine`.
- **Context:** Conflicts between `basictex` and `mactex` on macOS preventing automated PDF generation of whitepapers.
- **Workaround:** Generate HTML and print to PDF via browser.

### 13. Hallucination in Competitor Reports
- **Symptoms:** Bot reported on non-existent competitor "Zetherion AI".
- **Status:** Fixed by implementing mandatory link verification for all entities in reports.
