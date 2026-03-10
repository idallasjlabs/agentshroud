# AgentShroud™ Telegram-Reported Issues
**Generated:** 2026-03-09
**Source:** `telegram_history.jsonl`

This document captures issues, bugs, and blockers identified during live interactions between Isaiah Jefferson (@therealidallasj) and the AgentShroud bot (@agentshroud_bot).

---

## 🔴 CRITICAL: System Blockers

### 1. Anthropic API Credits & Rate Limits
- **Symptoms:** `LLM request rejected: Your credit balance is too low`, `AnthropicError: 429 Too Many Requests`.
- **Impact:** All agent functionality stops.
- **Context:** Occurred multiple times (Feb 20, Feb 21, Mar 9). Heavy Opus usage triggers rate limits even when funded.

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

### 4. SSH Key Regeneration on Restart
- **Symptoms:** `SSH keys seem to have broken`, `Permission denied (publickey)`.
- **Root Cause:** Container restarts/rebuilds regenerate the `id_ed25519` key, changing the public key fingerprint.
- **Impact:** Gateway loses management access to Marvin, Pi, and Trillian until keys are manually re-added to `authorized_keys`.

---

## 🟠 HIGH: Security & Logic Issues

### 5. ContextGuard False Positives (Collaborator Block)
- **Symptoms:** `[BLOCKED BY AGENTSHROUD: Multi-turn disclosure risk exceeded threshold (score=210.00)]`.
- **Impact:** Collaborators (e.g., Steve) are unable to interact with the bot because their benign queries are flagged as disclosure risks.
- **Context:** Identified on Mar 9. Threshold is currently too aggressive for trusted collaborators.

### 6. iMessage Integration Permissions
- **Symptoms:** `osascript: Not authorized to send Apple events to Messages`.
- **Status:** Documented in `IMESSAGE_PERMISSION_FIX.md`, but remains a recurring manual setup hurdle.

### 7. SMTP Port Blocks (Email Failures)
- **Symptoms:** `⚠️ Daily Competitive Analysis Email — FAILED`.
- **Root Cause:** Sandbox network blocks ports 465 and 587.
- **Impact:** Automated reporting is non-functional in the sandbox environment.
- **Proposed Fixes:** Gmail API (HTTPS/443), host-side relay, or gateway-routed email tool.

---

## 🟡 MEDIUM: Infrastructure & Deployment

### 8. Colima / Docker Stability (Marvin)
- **Symptoms:** `Docker/Colima is not responding!`, `VZ VM driver is crashing`, `Colima disk is locked`.
- **Impact:** Services on Marvin go offline.
- **Status:** Requires manual intervention to delete stale disk locks or restart the VZ driver.

### 9. Glibc TLS Incompatibility (Trillian)
- **Symptoms:** Gateway crashing with exit code 127 or TLS errors.
- **Root Cause:** Pinned `python:3.13-slim` SHA digest has glibc incompatibilities with Trillian's x86_64 runtime.
- **Resolution:** Unpinning SHA or switching to `bookworm-slim`.

### 10. Seccomp Profile Conflicts (x86_64)
- **Symptoms:** `gateway glibc TLS error persists`.
- **Root Cause:** Custom seccomp profiles block `arch_prctl` syscall, which is required for TLS allocation on x86_64 but not on ARM.
- **Resolution:** Overriding `security_opt` in `docker-compose.yml` for specific hosts.

---

## 🔵 LOW: User Experience & Documentation

### 11. Bot Token Migration Confusion
- **Symptoms:** `Telegram send failed: chat not found`.
- **Context:** Users must manually `/start` the new bot (@agentshroud_bot) because bots cannot initiate DMs. This caused confusion when migrating from the old bot token.

### 12. Pandoc/LaTeX Dependency Issues
- **Symptoms:** `pdflatex not found. Please select a different --pdf-engine`.
- **Context:** Conflicts between `basictex` and `mactex` on macOS preventing automated PDF generation of whitepapers.
- **Workaround:** Generate HTML and print to PDF via browser.

### 13. Hallucination in Competitor Reports
- **Symptoms:** Bot reported on non-existent competitor "Zetherion AI".
- **Status:** Fixed by implementing mandatory link verification for all entities in reports.
