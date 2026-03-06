# Session Summary — 2026-03-06

Branch: `feat/v0.8.0-enforcement-hardening`

---

## Changes Made

### Fix 1 — Telegram Proxy 403 (IP Allowlist Mismatch)
**`gateway/ingest_api/main.py`**
- `_PROXY_ALLOWED_NETWORKS`: corrected subnet from `172.21.0.0/16` → `172.11.0.0/16` to match the actual `agentshroud-isolated` Docker network defined in compose. Bot IP `172.11.0.3` was being denied on every Telegram proxy request.

---

### Fix 2 — Bot Startup Crash (`_var: unbound variable`)
**`docker/scripts/start-agentshroud.sh`**
- Escaped loop variables (`$_var`, `$_val`, `$SECRETS_DIR`) inside the unquoted heredoc (`<< EOF`). With `set -u` active, the shell was trying to expand them at write time rather than deferring to sourcing time, causing a fatal crash on line 118. `$ICLOUD_APP_PASSWORD` left unescaped (correctly expands at write time).

---

### Fix 3 — Multi-Instance Compose Conflicts
**`docker/docker-compose.yml`**
- Added usage comment with explicit project name (`-p agentshroud`).

**`docker/docker-compose.agentshroud-bot.marvin.yml`** (dev on same host — most changes)
- Service name `agentshroud:` → `bot:` — was creating a phantom service instead of merging with base
- Added `container_name` overrides (`agentshroud-dev-gateway`, `agentshroud-dev-bot`) — Docker rejects duplicate explicit container names
- Added network subnet overrides (`172.20.0.0/16` internal, `172.21.0.0/16` isolated) — Docker rejects overlapping subnet pools on the same host
- Removed stale `pihole:` service block — no image/build defined, caused compose error
- Removed misleading `AGENTSHROUD_PORT_OFFSET=0`
- Updated usage comment with correct project name (`-p agentshroud-dev`)

**`docker/docker-compose.agentshroud-bot.raspberrypi.yml`**
- Service name `agentshroud:` → `bot:`
- Updated usage comment with correct filename and project name

**`docker/docker-compose.agentshroud-bot.trillian.yml`**
- Service name `agentshroud:` → `bot:`
- Updated usage comment with correct filename and project name

---

### Fix 4 — Dev Instance Gateway Proxy Allowlist
**`gateway/ingest_api/main.py`**
- `_PROXY_ALLOWED_NETWORKS` made env-var configurable via `PROXY_ALLOWED_NETWORKS` (comma-separated CIDRs). Defaults to `172.11.0.0/16` for prod. Loopback (`127.0.0.0/8`) always included unconditionally.

**`docker/docker-compose.agentshroud-bot.marvin.yml`**
- Added `PROXY_ALLOWED_NETWORKS=172.21.0.0/16` to dev gateway — without this, the dev bot on `172.21.x.x` would receive 403 on all Telegram proxy requests despite the subnet fix above.

---

## Net Result

| Instance | Host | Gateway Port | Bot Port | Isolated Subnet | Proxy Allowlist |
|---|---|---|---|---|---|
| Prod (`agentshroud`) | marvin / `ijefferson.admin` | 8080 | 18790 | 172.11.0.0/16 | 172.11.0.0/16 (default) |
| Dev (`agentshroud-dev`) | marvin / `agentshroud-bot` | 9080 | 19789 | 172.21.0.0/16 | 172.21.0.0/16 (env override) |
| Dev (`agentshroud`) | raspberrypi / `agentshroud-bot` | 8080 | 18789 | 172.11.0.0/16 | 172.11.0.0/16 (default) |
| Dev (`agentshroud`) | trillian / `agentshroud-bot` | 8080 | 18789 | 172.11.0.0/16 | 172.11.0.0/16 (default) |
