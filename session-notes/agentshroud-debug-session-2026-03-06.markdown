# AgentShroud Debug Session — 2026-03-06

---

## tmux 2.8 on CentOS 7

**Q:** How to install tmux 2.8 on CentOS 7?

**A:**

### Option 1: Build from Source (Recommended)
```bash
sudo yum install -y gcc make libevent-devel ncurses-devel
wget https://github.com/tmux/tmux/releases/download/2.8/tmux-2.8.tar.gz
tar -xzf tmux-2.8.tar.gz
cd tmux-2.8
./configure --prefix=/usr/local
make
sudo make install
tmux -V
```

### Option 2: Via EPEL
```bash
sudo yum install -y epel-release
sudo yum install -y tmux
```

**libevent from source (if needed):**
```bash
wget https://github.com/libevent/libevent/releases/download/release-2.1.12-stable/libevent-2.1.12-stable.tar.gz
tar -xzf libevent-2.1.12-stable.tar.gz
cd libevent-2.1.12-stable
./configure --prefix=/usr/local
make && sudo make install
```

---

## Installing zsh on CentOS 7

```bash
# Easiest — via yum
sudo yum install -y zsh
zsh --version

# Set as default shell
chsh -s $(which zsh)

# Oh My Zsh (optional)
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

---

## tmux 2.8 Build Success

Build and install completed successfully. Verified with:
```bash
tmux -V
# tmux 2.8
which tmux
# /usr/local/bin/tmux
```

---

## named-checkconf

```bash
# Check default config
named-checkconf

# Check + all zone files
named-checkconf -z /etc/named.conf

# Check zone file
named-checkzone example.com /var/named/example.com.zone
```

### Common Workflow on CentOS 7
```bash
sudo named-checkconf /etc/named.conf
sudo named-checkzone example.com /var/named/example.com.zone
sudo systemctl restart named
sudo systemctl status named
```

---

## named.service Failed — Zone File Error

**Error:**
```
dns_master_load: fluenceenergy.com.lan:5896: unexpected end of line
dns_master_load: fluenceenergy.com.lan:5895: unexpected end of input
zone fluenceenergy.com/IN: loading from master file fluenceenergy.com.lan failed
```

**Fix:**
```bash
# View problem lines
awk 'NR>=5890 && NR<=5900 {print NR": "$0}' /var/named/fluenceenergy.com.lan

# Edit and fix
sudo vi +5895 /var/named/fluenceenergy.com.lan

# Validate
sudo named-checkzone fluenceenergy.com /var/named/fluenceenergy.com.lan

# Restart
sudo systemctl restart named
```

---

## DNS Terminology

| Term | Meaning |
|---|---|
| **Reverse zone file** | Zone file containing PTR records |
| **Reverse lookup zone** | e.g. `250.190.10.in-addr.arpa` |
| **PTR record** | Maps IP → hostname |
| **Forward zone file** | Contains A/AAAA/CNAME/MX records |

**dig -x** = reverse DNS lookup (IP → hostname)
```bash
dig -x 8.8.8.8          # Returns PTR record
dig -x 10.190.250.1 +short
```

---

## Claude Code — Shift+Enter Newline

**Easiest fix:** Run `/terminal-setup` inside Claude Code (auto-configures VS Code, Alacritty, Zed, Warp).

**For tmux:** Add to `~/.tmux.conf`:
```bash
set -g extended-keys always
set -as terminal-features 'xterm*:extkeys'
```

**Fallback:** Type `\` then Enter for newlines anywhere.

---

## Ghostty + tmux Bugs

### 1. `missing or unsuitable terminal: xterm-ghostty` over SSH
```bash
infocmp xterm-ghostty | ssh user@remote -- tic -x -
# Or set in ~/.config/ghostty/config:
term = xterm-256color
```

### 2. Shift+Enter not working inside tmux
```bash
# ~/.tmux.conf
set -s extended-keys on
set -s extended-keys-format csi-u
set -as terminal-features 'xterm-ghostty:extkeys'

# ~/.config/ghostty/config
keybind = shift+enter=text:\x1b\r
```

### 3. Recommended ~/.tmux.conf for Ghostty
```bash
set -g default-terminal "xterm-256color"
set -as terminal-overrides ",xterm-ghostty:Tc"
set -s extended-keys on
set -s extended-keys-format csi-u
set -as terminal-features 'xterm-ghostty:extkeys'
```

---

## git pull — No Tracking Information

**Error:** `There is no tracking information for the current branch.`

**Fix:**
```bash
git branch --set-upstream-to=origin/feat/v0.8.0-enforcement-hardening feat/v0.8.0-enforcement-hardening && git pull
```

**Prevent in future:**
```bash
git push -u origin feat/v0.8.0-enforcement-hardening
```

---

## git pull — Divergent Branches

**Error:** `fatal: Need to specify how to reconcile divergent branches.`

```bash
# Rebase (recommended for feature branches)
git pull origin feat/v0.8.0-enforcement-hardening --rebase

# Set global default
git config --global pull.rebase true
```

---

## Docker Compose — `-f` Flag Error

**Cause 1:** Literal `\n` in command — run as two separate commands.

**Cause 2:** Using old `docker-compose` v1 instead of `docker compose` v2:
```bash
docker compose version   # Should show v2.x.x
sudo yum install docker-compose-plugin  # CentOS fix
```

---

## Docker Build — openclaw@0.11.4 Not Found

**Error:** `npm error notarget No matching version found for openclaw@0.11.4`

**Diagnosis:**
```bash
npm view openclaw versions
# Package switched to date-based versioning — latest: 2026.3.2
```

**Fix:**
```bash
# Find the correct Dockerfile
find . -name 'Dockerfile.agentshroud'
# ./docker/Dockerfile.agentshroud

# Update version (macOS sed requires '')
sed -i '' 's/openclaw@0.11.4/openclaw@2026.3.2/' ./docker/Dockerfile.agentshroud
```

---

## Docker Build — gpg not found

**Error:** `/bin/sh: 1: gpg: not found`

**Fix:** Add `gnupg` to apt-get install block in Dockerfile:
```dockerfile
RUN apt-get update && apt-get install -y --no-install-recommends \
    gnupg \
    unzip \
    && rm -rf /var/lib/apt/lists/*
```

---

## Docker Build — 1Password GPG Signature Failed

**Error:** `gpg: no valid OpenPGP data found` — signature file was 112 bytes (error page).

**Root cause:** Variable name bug — `case` statement set `TRIVY_ARCH` but curl URLs used `${ARCH}` (undefined).

**Fix:** Replace broken curl/zip/GPG block with official 1Password apt repo:
```dockerfile
RUN curl -sS https://downloads.1password.com/linux/keys/1password.asc | \
    gpg --dearmor --output /usr/share/keyrings/1password-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/1password-archive-keyring.gpg] https://downloads.1password.com/linux/debian/$(dpkg --print-architecture) stable main" | \
    tee /etc/apt/sources.list.d/1password.list && \
    apt-get update && apt-get install -y --no-install-recommends 1password-cli \
    && rm -rf /var/lib/apt/lists/*
```

Also added `gnupg` to base apt-get install block.

---

## Dockerfile.agentshroud — Summary of All Changes

| # | Change | Reason |
|---|---|---|
| 1 | `openclaw@0.11.4` → `openclaw@2026.3.2` | Package uses date-based versioning; 0.11.4 never existed |
| 2 | Added `gnupg` to base apt-get block | Required for 1Password apt repo GPG key import |
| 3 | Replaced 1Password curl/zip/GPG install with apt repo method | `${ARCH}` variable was undefined; apt repo is more reliable |
| 4 | Removed orphan `rm -f /tmp/op.zip` line | Leftover bare shell command from old install block |

---

## Container Startup — Script Errors

### Error 1: `SECRETS_DIR: unbound variable`

**Root cause:** `SECRETS_DIR` was only defined inside a heredoc, not in the outer script body. When sourced with `set -u` active, it failed.

**Fix:** Added `SECRETS_DIR="${SECRETS_DIR:-/tmp/secrets}"` to outer script before line 112 (`_ICLOUD_ENV_FILE` definition).

Also fixed typo inside heredoc: `chmod 700 "{$SECRETS_DIR}"` → `chmod 700 "${SECRETS_DIR}"`

### Error 2: `/tmp/.icloud-env: line 1: ICLOUD_APP_PASSWORD: unbound variable`

**Root cause:** `_ICLOUD_ENV_FILE` was being sourced at line 157 while `set -u` was active in the parent shell. The heredoc used `<< EOF` (unquoted), causing variables to expand at write time rather than at source time.

**Fix:** Wrapped the source call:
```bash
set +u; . "$_ICLOUD_ENV_FILE" || true; set -u
```

### Error 3: `line 118: _var: unbound variable` / `_val: unbound variable`

**Root cause:** Same `set -u` issue — `for` loop variables in the heredoc content being evaluated in outer shell context.

**Fix:** Same `set +u` / `set -u` wrap around the source call.

---

## Telegram — `deleteWebhook failed: undefined: undefined`

### Investigation Steps

```bash
# 1. Confirmed api.telegram.org reachable through proxy (TLS handshake OK)
docker compose -p agentshroud exec bot curl -sv https://api.telegram.org/bot<token>/getMe

# 2. Found TELEGRAM_API_BASE_URL=http://gateway:8080/telegram-api
docker compose -p agentshroud exec bot env | grep -i telegram

# 3. Tested gateway route
curl http://gateway:8080/telegram-api/bot<token>/getMe
# → {"detail":"Telegram proxy not configured"}

# 4. Found gateway reads token from /run/secrets/telegram_bot_token
grep -n 'telegram_bot_token' gateway/ingest_api/main.py
# line 2220: with open("/run/secrets/telegram_bot_token", "r") as f:

# 5. Confirmed telegram_bot_token NOT mounted in gateway
docker compose -p agentshroud exec gateway ls -la /run/secrets/
# Only: 1password_service_account, gateway_password
```

### Root Cause

`telegram_bot_token` secret was defined globally in `docker-compose.yml` but not added to the gateway service's `secrets:` list.

### Fix

Added to gateway service in `docker/docker-compose.yml`:
```yaml
  gateway:
    secrets:
      - gateway_password
      - 1password_service_account
      - telegram_bot_token    # ← added
```

Then redeployed:
```bash
docker compose -f docker/docker-compose.yml -p agentshroud up -d
docker compose -f docker/docker-compose.yml -p agentshroud exec gateway ls -la /run/secrets/
```

---

## docker-compose.yml — Orphaned Containers

**Warning:** `Found orphan containers ([agentshroud-bot-20260306-0810 ...])`

**Fix:**
```bash
docker compose -f docker/docker-compose.yml -p agentshroud up -d --remove-orphans
```

---

*Session date: 2026-03-06 | Branch: feat/v0.8.0-enforcement-hardening | Host: marvin*
