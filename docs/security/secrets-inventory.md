# Secrets Inventory — Pre-Release Security Audit

> **Generated:** 2026-03-19
> **Branch:** `feat/v0.9.0-soc-team-collab`
> **Scope:** All tracked files + git history findings
> **Gitleaks scan:** 62 findings — 4 confirmed real secrets in history, ~58 false positives

Format: `<file> # <purpose> [required|not required]`

---

## 1. Active Secret Files (`docker/secrets/`)

All files below are created at deploy time by `docker/secrets/setup-secrets.sh`.
**None are tracked by git** — only the `.example` templates are committed.
The actual secret files are gitignored via `docker/secrets/*.txt` and `docker/secrets/1password_*`.

```
docker/secrets/anthropic_oauth_token.txt       # Claude OAuth token (sk-ant-oat01-...) for API calls [required]
docker/secrets/anthropic_api_key.txt           # Anthropic API key alternate form [required]
docker/secrets/openai_api_key.txt              # OpenAI API key for GPT model support [required]
docker/secrets/google_api_key.txt              # Google API key for Gemini model support [required]
docker/secrets/gateway_password.txt            # Auto-generated 32-byte hex token for gateway HTTP auth [required]
docker/secrets/telegram_bot_token_production.txt # Live Telegram bot token for the active bot [required]
docker/secrets/1password_bot_email.txt         # 1Password account email for op CLI auth [required]
docker/secrets/1password_bot_master_password.txt # 1Password master password for op CLI auth [required]
docker/secrets/1password_bot_secret_key.txt    # 1Password secret key (A3-...) for op CLI auth [required]
docker/secrets/1password_service_account       # 1Password service account token for non-interactive auth [required]
```

---

## 2. CRITICAL — Real Secrets in Git History

These files contain actual credentials committed to the repository at some point in the commit history.
**Rotation required before any public release.** History must be expunged with `git filter-repo`.

```
gateway/tests/test_data/device.json            # Ed25519 SSH private key committed in test fixture — real key, not generated [not required]
docs/archive/VAULT-SHARING-INSTRUCTIONS.md     # 1Password secret key (A3-...) in plaintext sharing instructions [not required]
telegram_history.jsonl                         # Gateway password hash (bcrypt) + Telegram bot tokens across 10+ lines [not required]
archive/FINAL_CONFIGURATION.md                # Gateway auth token b539ae... in connection config block [not required]
archive/ACCESS_INFO.md                         # Gateway auth token b539ae... repeated x3 in access reference doc [not required]
archive/QUICK_ACCESS.md                        # Gateway auth token b539ae... repeated x6 in quickstart doc [not required]
archive/CONNECT_NOW.md                         # Gateway auth token b539ae... repeated x2 in connection guide [not required]
archive/SYSTEM_STATUS.md                       # Telegram bot token (8469477154:...) + gateway token x2 in status doc [not required]
archive/SETUP_SUMMARY.md                       # Gateway auth token b539ae... x2 in setup summary [not required]
archive/HOW_TO_CONNECT.md                      # Gateway auth token 14bf48... x3 in alternate connection guide [not required]
archive/session-notes/continue-20260215-1457.md # Gateway auth token b539ae... x3 in session continuation notes [not required]
archive/session-notes/continue-20260215-0717.md # Gateway auth token dd9228... x2 in session continuation notes [not required]
archive/ALL-SERVICES-WORKING.md               # iCloud app-specific password (ibkd-byru-cade-fpaq) in working config [not required]
archive/ICLOUD-SUCCESS-SUMMARY.md             # iCloud app-specific password x3 in iCloud setup summary [not required]
docs/archive/CONNECTION-GUIDE.md              # Gateway auth token acd084... x2 in tracked connection guide [not required]
docs/archive/README.md                         # Gateway auth token acd084... in tracked archive README [not required]
docs/archive/SESSION-SUMMARY.md               # Gateway auth token acd084... x2 in tracked session summary [not required]
.claude/skills/sec-offense/SKILL.md           # Gateway auth token b539ae... embedded in offensive security skill example [not required]
telegram_history.jsonl                         # Telegram bot tokens for 3 bots (@agentshroud_marvin_bot, @agentshroud_trillian_bot, @agentshroud_raspberrypi_bot) [not required]
```

### Credential Rotation Checklist

| Credential | Rotation Method | Status |
|------------|----------------|--------|
| Ed25519 private key (device.json) | `ssh-keygen -t ed25519` new key; remove old from `authorized_keys` | pending |
| 1Password secret key (VAULT-SHARING-INSTRUCTIONS.md) | 1Password admin console → regenerate secret key | pending |
| Gateway password hash (telegram_history.jsonl) | Regenerate via `setup-secrets.sh`; update 1Password item `tdx3r77qoplljrv45luh7zkngi` | pending |
| Gateway auth tokens (b539ae..., 14bf48..., acd084..., dd9228...) | Same as above — all are the same credential at different points in time | pending |
| Telegram bot tokens (4 bots) | @BotFather → `/revoke` then `/newtoken` for each bot | pending |
| iCloud app-specific password | appleid.apple.com → Security → App-Specific Passwords → Revoke | pending |

---

## 3. Secret-Adjacent Tracked Files

These files are intentionally tracked. They contain no real secrets — only templates, placeholders, or
documentation of how secrets are structured.

```
docker/secrets/anthropic_oauth_token.txt.example   # Template: shows expected token format (sk-ant-oat01-...) [required]
docker/secrets/anthropic_api_key.txt.example        # Template: shows expected API key format (sk-...) [required]
docker/secrets/openai_api_key.txt.example           # Template: shows expected OpenAI key format [required]
docker/secrets/google_api_key.txt.example           # Template: shows expected Google key format [required]
docker/secrets/gateway_password.txt.example         # Template: shows auto-generation command [required]
docker/secrets/telegram_bot_token_production.txt.example # Template: shows expected bot token format [required]
docker/secrets/1password_bot_email.txt.example      # Template: shows email placeholder [required]
docker/secrets/1password_bot_master_password.txt.example # Template: placeholder only [required]
docker/secrets/1password_bot_secret_key.txt.example # Template: shows A3- prefix format [required]
docker/secrets/1password_service_account.example    # Template: service account token placeholder [required]
docker/secrets/README.md                            # Operator setup instructions for the secrets directory [required]
docker/secrets/setup-secrets.sh                     # Interactive secrets provisioning script, no credentials embedded [required]
docker/.env.example                                 # Model profile env var template; contains no secrets [required]
.llm_settings/mcp-servers/github/.env.example      # GitHub MCP env var template; no real tokens [required]
```

---

## 4. False Positives — Test Fixtures (gitleaks suppression candidates)

These 34 test files contain fake API key patterns (`sk-test-*`, `sk-proj-abc*`, `fake-*-key`) used as
test fixtures. They trigger gitleaks rules but contain no real credentials.
**Action:** Add allowlist entries to `.gitleaks.toml` (already applied).

```
gateway/tests/conftest.py                      # Root test config; fake sk-ant-* and sk-proj-* tokens for fixture injection [required]
gateway/tests/test_auth.py                     # Auth middleware tests; fake bearer tokens and API keys [required]
gateway/tests/test_agentshroud_manager.py      # Manager integration tests; fake API key placeholders [required]
gateway/tests/test_all_modules_enforce.py      # Cross-module enforcement tests; fake key patterns throughout [required]
gateway/tests/test_block_credentials.py        # Credential blocking tests; fake sk-test-* keys as attack payloads [required]
gateway/tests/test_canary_tripwire.py          # Tripwire tests; fake canary tokens [required]
gateway/tests/test_config_validation.py        # Config validation; fake key format assertions [required]
gateway/tests/test_credential_injector.py      # Credential injector; fake sk-ant-* patterns to test injection logic [required]
gateway/tests/test_credential_isolation.py     # Isolation tests; fake keys per-agent to test leak detection [required]
gateway/tests/test_dashboard.py                # Dashboard tests; fake auth tokens [required]
gateway/tests/test_dashboard_endpoints.py      # Dashboard endpoint tests; fake bearer tokens [required]
gateway/tests/test_e2e.py                      # End-to-end tests; fake full-stack credentials [required]
gateway/tests/test_e2e_watchtower.py           # Watchtower e2e; fake tokens for all services [required]
gateway/tests/test_egress_telegram_notify.py   # Egress notify tests; fake bot token for mock Telegram calls [required]
gateway/tests/test_env_guard.py                # Env guard tests; fake API keys in env var assertions [required]
gateway/tests/test_file_sandbox.py             # File sandbox tests; fake key patterns in file content checks [required]
gateway/tests/test_key_vault.py                # Key vault tests; fake sk-ant-* keys for vault storage tests [required]
gateway/tests/test_log_sanitizer.py            # Log sanitizer tests; fake secrets to verify redaction [required]
gateway/tests/test_mcp_proxy.py                # MCP proxy tests; fake API keys in tool call fixtures [required]
gateway/tests/test_mcp_result_endpoint.py      # MCP result endpoint; fake key patterns in result payloads [required]
gateway/tests/test_op_proxy.py                 # 1Password proxy tests; fake op:// URIs and vault references [required]
gateway/tests/test_prompt_guard.py             # Prompt guard tests; fake keys as injection attack vectors [required]
gateway/tests/test_runtime_engines.py          # Runtime engine tests; fake model API keys [required]
gateway/tests/test_security_audit.py           # Security audit tests; fake credentials as audit fixtures [required]
gateway/tests/test_security_audit_advanced.py  # Advanced audit tests; fake keys for multi-pattern coverage [required]
gateway/tests/test_security_fixes.py           # Security fix regression tests; fake tokens as payloads [required]
gateway/tests/test_security_integration.py     # Security integration tests; fake keys across modules [required]
gateway/tests/test_shared_memory.py            # Shared memory tests; fake sk-proj-* keys in memory fixtures [required]
gateway/tests/test_slack_proxy.py              # Slack proxy tests; fake Slack bot tokens [required]
gateway/tests/test_soc_auth.py                 # SOC auth tests; fake bearer tokens for role assertions [required]
gateway/tests/test_ssh_endpoints.py            # SSH endpoint tests; fake SSH key material in request fixtures [required]
gateway/tests/test_telegram_proxy_inbound.py   # Telegram inbound tests; fake bot token for mock getUpdates [required]
gateway/tests/test_telegram_proxy_outbound.py  # Telegram outbound tests; fake bot token for mock sendMessage [required]
gateway/tests/test_token_validation.py         # Token validation tests; fake sk-ant-* and sk-proj-* patterns [required]
```

---

## 5. Recommendations

### 5.1 History Expungement

The 4 CRITICAL secret categories in Section 2 span across dozens of commits in the 735-commit history.
Use `git filter-repo` (preferred over BFG) to rewrite history:

```bash
# Install git-filter-repo
pip install git-filter-repo

# Remove all files that should never have been committed
git filter-repo --path telegram_history.jsonl --invert-paths
git filter-repo --path telegram_history.jsonl.tgz --invert-paths
git filter-repo --path tg_export_session.session --invert-paths
git filter-repo --path-glob 'archive/*' --invert-paths

# Alternative: orphan branch (simpler, loses all history)
# See docs/security/history-purge-plan.md for full procedure
```

> **GitHub cache warning:** GitHub retains unreferenced commits by SHA for ~90 days.
> Contact GitHub Support to request immediate purge, or delete and recreate the repository.

### 5.2 `.gitleaks.toml` Allowlist for Test False Positives

Applied. See `gitleaks.toml` in the repo root — path-based and regex-based allowlists now suppress
all 34 test fixture files and 6 regex patterns. Run `gitleaks detect --source . --no-git` to verify
0 findings on the working tree.

### 5.3 Pre-Release Secrets Management Strategy

| Action | Priority | Status |
|--------|----------|--------|
| Rotate all 4 Telegram bot tokens (@BotFather) | CRITICAL | pending |
| Rotate gateway password (setup-secrets.sh) | CRITICAL | pending |
| Rotate iCloud app-specific password | CRITICAL | pending |
| Regenerate Ed25519 key pair from device.json | CRITICAL | pending |
| Rotate 1Password secret key | CRITICAL | pending |
| Expunge git history (filter-repo — see §5.1) | CRITICAL | pending |
| Add gitleaks allowlist for test fixtures | HIGH | done |
| Add `archive/` to `.gitignore` | HIGH | pending |
| Contact GitHub Support for cache purge after history rewrite | HIGH | pending |
| Re-scan with `gitleaks detect --source . --no-git` post-purge | REQUIRED | pending |

### 5.4 Files Safe to Delete from Working Tree

These files contain secrets and have no future role in the codebase:

```
telegram_history.jsonl          — 1.9 MB chat history export; all useful data already analyzed
telegram_history.jsonl.tgz      — compressed backup of above
tg_export_session.session       — Telegram MTProto session file; not needed by the bot
archive/                        — early development session notes; entirely superseded
```

---

## Appendix — Gitleaks Suppression Summary

| Finding Category | Count | Action |
|-----------------|-------|--------|
| Real secrets in history (Section 2) | 4 credential types / ~20 file instances | Rotate + expunge history |
| Test fixture false positives (Section 4) | ~34 files / ~58 findings | Suppressed via .gitleaks.toml |
| Example template files (Section 3) | 14 files | Suppressed via .gitleaks.toml path allowlist |
| **Total gitleaks findings** | **~62** | |
