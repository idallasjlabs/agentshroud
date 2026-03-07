# Git History Purge Plan

> **Purpose:** Purge all commit history before making the repo public. Secrets and tokens from chat history are embedded across dozens of commits.
>
> **Date:** 2026-03-07 | **Status:** PLANNED

---

## Pre-Purge Checklist

- [ ] Backup full repo with history to `~/Development/agentshroud-history-backup`
- [ ] Verify backup has all commits (`git log --oneline | wc -l`)
- [ ] Run secret scan and build rotation checklist (see below)
- [ ] Rotate ALL leaked secrets BEFORE going public
- [ ] Notify Claude (Codex) session about force push
- [ ] Notify Pi instance about force push

---

## Procedure

```bash
cd ~/Development/agentshroud

# 1. Backup the full repo WITH history for offline review
cp -r . ~/Development/agentshroud-history-backup

# 2. Verify the backup
cd ~/Development/agentshroud-history-backup
git log --oneline | wc -l  # confirm all commits present
cd ~/Development/agentshroud

# 3. Create orphan branch (all current files, zero history)
git checkout --orphan clean-main
git add -A
git commit -m "Initial commit — AgentShroud v0.8.0 Watchtower"

# 4. Replace main
git branch -D main
git branch -m clean-main main

# 5. Force push (DESTROYS all remote history)
git push origin main --force

# 6. Delete old feature branches remotely
git push origin --delete feat/v0.8.0-enforcement-hardening
git push origin --delete feature/imessage-integration
```

---

## Post-Purge — Other Instances

### Pi
```bash
cd ~/Development/agentshroud
git fetch origin
git checkout main
git reset --hard origin/main
```

### Trillian (when back online)
```bash
cd ~/Development/agentshroud
git fetch origin
git checkout main
git reset --hard origin/main
```

### Claude (Codex on Marvin)
Same as Pi — fetch and hard reset.

---

## GitHub Cache Warning

GitHub caches old commits by SHA for ~90 days even after force push. Options:
1. **Wait 90 days** — cached commits expire automatically
2. **Contact GitHub Support** — request immediate cache purge
3. **Delete and recreate repo** — nuclear option, guarantees no cached history

If any high-value secrets (API keys, bot tokens) were committed, **rotate them regardless** — don't rely on history purge alone.

---

## Secret Rotation Checklist

See `secret-scan-results.md` for the full scan output.

| Secret Type | Where to Rotate | Status |
|-------------|----------------|--------|
| Telegram bot tokens (4 bots) | @BotFather → `/revoke` then `/newtoken` | ⬜ |
| Gateway auth token | Regenerate, update 1Password + env vars | ⬜ |
| 1Password service account token | 1Password admin console | ⬜ |
| SSH keys (if committed) | `ssh-keygen` new keys, update `authorized_keys` | ⬜ |
| iCloud app-specific password | appleid.apple.com → App-Specific Passwords | ⬜ |
| Anthropic OAuth token | Anthropic console | ⬜ |
| Brave Search API key | Brave developer portal | ⬜ |
| Any other API keys in chat logs | Per-provider console | ⬜ |

---

## Post-Rotation Verification

- [ ] All bots respond on Telegram with new tokens
- [ ] Gateway auth works with new token
- [ ] 1Password CLI authenticates
- [ ] SSH connections work with new keys
- [ ] Email sending works with new app password
- [ ] Claude OAuth works
- [ ] Web search works with new Brave key
