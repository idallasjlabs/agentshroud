# 🔐 Secret Scan Results — Pre-Purge Rotation Checklist

> **Scanned:** 2026-03-07 14:45 UTC
> **Branch:** `feat/v0.8.0-enforcement-hardening`
> **Method:** grep + pattern matching across all tracked files

---

## 🚨 CRITICAL — Must Rotate Before Going Public

### 1. Telegram Bot Tokens (ALL 4 EXPOSED)

| Bot | Token | Found In |
|-----|-------|----------|
| `@therealidallasj_bot` (old) | `8469477154:AAFOF...IpTg` | `archive/SYSTEM_STATUS.md:127` |
| `@agentshroud_marvin_bot` | `8736289266:AAGVzcmqiSaTSyPz5B8lJCcxkmZPg9jTe28` | `telegram_history.jsonl:857`, `:967`, `:970`, `:971`, `:996` |
| `@agentshroud_trillian_bot` | `8751040644:AAHf1zXfKI0XXdhNMH8eC_BZPexjQSVK1pA` | `telegram_history.jsonl:864`, `:1636` |
| `@agentshroud_raspberrypi_bot` | `8690957340:AAHgOYrylnUY3nllrCUK-MIHxkELmlQjt6I` | `telegram_history.jsonl:867` |

**Rotation:** @BotFather → `/revoke` then `/newtoken` for each bot. Update:
- Docker secrets: `docker/secrets/telegram_bot_token_*.txt`
- `apply-patches.js` (injected via `TELEGRAM_BOT_TOKEN` env var — no change needed if using env)
- Host-specific compose overlays

### 2. Gateway Auth Tokens (2 EXPOSED)

| Token | Found In |
|-------|----------|
| `b539ae0c7a720f71e9b26cfab1b53c58ae362a0ad40d857eaed9a44a15932a05` | `archive/FINAL_CONFIGURATION.md:137`, `archive/ACCESS_INFO.md` (×3), `archive/QUICK_ACCESS.md` (×6), `archive/CONNECT_NOW.md` (×2), `archive/SYSTEM_STATUS.md` (×2), `archive/SETUP_SUMMARY.md` (×2), `archive/session-notes/continue-20260215-1457.md` (×3), `telegram_history.jsonl` (×10+), `.claude/skills/sec-offense/SKILL.md:373` |
| `14bf48103da11537b7207a2fe5487084d39a799a6129f3bbcb644a417c7f091b` | `archive/HOW_TO_CONNECT.md` (×3) |
| `acd0842962070d58c2bb825876aab743c4c45ddbc2eae7e475c4058e0b3f7832` | `docs/archive/CONNECTION-GUIDE.md` (×2), `docs/archive/README.md`, `docs/archive/SESSION-SUMMARY.md` (×2) |
| `dd92285d1a3c22f46fc325a8a6756b6fb2977b7af127dd08fb7432757776a287` | `archive/session-notes/continue-20260215-0717.md` (×2) |

**Rotation:** Generate new token, update:
- `docker/secrets/gateway_password.txt`
- 1Password item `tdx3r77qoplljrv45luh7zkngi`
- All host env vars / compose files

### 3. iCloud App-Specific Password (EXPOSED)

| Credential | Value | Found In |
|-----------|-------|----------|
| iCloud app password | `ibkd-byru-cade-fpaq` | `archive/ALL-SERVICES-WORKING.md:123`, `archive/ICLOUD-SUCCESS-SUMMARY.md:13,119,164` |

**Rotation:** appleid.apple.com → Security → App-Specific Passwords → Revoke + regenerate. Update 1Password item `25ghxryyvup5wpufgfldgc2vjm`.

### 4. 1Password Item IDs (EXPOSED — lower risk but reveals vault structure)

| Item | ID | Found In |
|------|-----|----------|
| iCloud credentials | `25ghxryyvup5wpufgfldgc2vjm` | `docker/bots/openclaw/start.sh:116`, `docker/scripts/start-agentshroud.sh:116` |
| Gateway credentials | `tdx3r77qoplljrv45luh7zkngi` | `docker/bots/openclaw/config/cron/jobs.json:112,259` |

**Risk:** Item IDs alone can't access secrets without the service account token, but they reveal vault structure. Consider using `op://` URIs with item names instead of IDs.

---

## ⚠️ MEDIUM — Should Clean Up

### 5. Telegram Chat History File

| File | Risk |
|------|------|
| `telegram_history.jsonl` (1.9MB) | Contains ALL chat history including tokens, passwords, config dumps, internal IPs, and architecture details |
| `telegram_history.jsonl.tgz` (434KB) | Compressed version of above |
| `tg_export_session.session` (28KB) | Telegram export session file |

**Action:** Remove from repo entirely. Add to `.gitignore`.

### 6. Cron Job Configs with 1Password Commands

| File | Risk |
|------|------|
| `docker/bots/openclaw/config/cron/jobs.json` | Contains `op item get` commands with vault names and item IDs |
| `docker/config/openclaw/cron/jobs.json` | Same (duplicate) |

**Action:** Move 1Password references to env vars or a separate non-committed config.

### 7. Archive Directory

| Directory | Risk |
|-----------|------|
| `archive/` (entire directory) | Session notes, setup summaries, config dumps — riddled with tokens, passwords, URLs with auth |
| `docs/archive/` | Same pattern — connection guides with tokens |

**Action:** Exclude from public repo. Add to `.gitignore` or delete.

---

## ℹ️ LOW — Informational

### 8. Docker Image SHAs (not secret, but reveal build history)
- Various SHA256 hashes in `telegram_history.jsonl` — Docker image digests
- Not rotatable, not dangerous

### 9. Internal Network Details (exposed but changing)
- Tailscale IPs: `100.107.248.66`, `100.88.24.16`
- LAN IPs: `192.168.7.137`, `192.168.7.97`, `192.168.7.25`
- Docker subnets: `172.10-12.0.0/16`, `172.20-23.0.0/16`
- Found throughout archive and chat history

### 10. 1Password Vault Name (exposed)
- `"Agent Shroud Bot Credentials"` — appears in start scripts and cron jobs
- Not a security risk alone but reveals organization structure

---

## Pre-Public Checklist

| # | Action | Priority | Status |
|---|--------|----------|--------|
| 1 | Rotate ALL 4 Telegram bot tokens via @BotFather | 🔴 CRITICAL | ⬜ |
| 2 | Rotate gateway auth token | 🔴 CRITICAL | ⬜ |
| 3 | Revoke + regenerate iCloud app-specific password | 🔴 CRITICAL | ⬜ |
| 4 | Remove `telegram_history.jsonl` + `.tgz` + `.session` from repo | 🔴 CRITICAL | ⬜ |
| 5 | Remove or gitignore `archive/` directory | 🟡 HIGH | ⬜ |
| 6 | Remove or gitignore `docs/archive/` directory | 🟡 HIGH | ⬜ |
| 7 | Clean 1Password item IDs from cron jobs (use env vars) | 🟡 HIGH | ⬜ |
| 8 | Remove `.claude/skills/sec-offense/SKILL.md` (has gateway token) | 🟡 HIGH | ⬜ |
| 9 | Add comprehensive `.gitignore` entries | 🟡 HIGH | ⬜ |
| 10 | Purge git history (orphan branch) | 🔴 CRITICAL | ⬜ |
| 11 | Verify no secrets in final commit | 🔴 CRITICAL | ⬜ |
| 12 | Re-scan with gitleaks after purge | 🟡 HIGH | ⬜ |

---

## Files to Add to .gitignore

```gitignore
# Chat history (contains secrets)
telegram_history.jsonl
telegram_history.jsonl.tgz
tg_export_session.session

# Archives (contain secrets from early development)
archive/
docs/archive/

# Secrets
docker/secrets/
*.secret
*.key
*.pem

# Gitleaks reports
gitleaks-report.json

# Session data
*.session
```

---

## Post-Purge Verification

After orphan branch + rotation:

```bash
# 1. Scan final commit for secrets
gitleaks detect --source . --no-git

# 2. Verify no old tokens work
curl -s "https://api.telegram.org/bot<OLD_TOKEN>/getMe"  # should fail

# 3. Verify new tokens work
curl -s "https://api.telegram.org/bot<NEW_TOKEN>/getMe"  # should succeed

# 4. Verify gateway auth
curl -s -H "Authorization: Bearer <NEW_TOKEN>" http://localhost:8080/status
```
