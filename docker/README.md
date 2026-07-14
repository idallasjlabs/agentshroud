# AgentShroud Docker Configuration

**Status**: ✅ **READY TO RUN** (pending API key setup)
**Phase**: 3 (Hardened Container + Persona Integration)
**Last Updated**: February 14, 2026

---

## Quick Start

**Goal**: Working chat interface with Isaiah's personality in <5 minutes.

**See**: [QUICKSTART.md](./QUICKSTART.md) for detailed instructions.

**TL;DR**:
```bash
# 1. Add your Anthropic API key
echo "YOUR_ANTHROPIC_API_KEY" > secrets/anthropic_api_key.txt
chmod 600 secrets/anthropic_api_key.txt

# 2. Start the stack
docker-compose up -d

# 3. Test
curl http://localhost:8080/status
```

---

## Container Runtime Support (SCRUM-92)

AgentShroud runs on any of the following container runtimes. The helper scripts
(`scripts/asb`, canary, rollback) auto-detect which one is installed via the shim in
`scripts/lib/container-runtime.sh` — you do not pick a runtime by hand.

| Runtime | Compose form detected | Status | Notes |
|---------|----------------------|--------|-------|
| **Docker Desktop** | `docker-compose` (standalone) | ✅ Supported | macOS/Windows; ships the standalone binary. |
| **Colima** (macOS) | `docker-compose` (standalone) | ✅ Supported — **deploy hosts** | marvin/trillian/rpi run Colima + standalone `docker-compose`. `asb` also sets `DOCKER_HOST` to the Colima socket. |
| **Docker Engine** (Linux) | `docker compose` (plugin) | ✅ Supported | Used when the standalone `docker-compose` binary is absent but the `docker` CLI + compose plugin are present. |
| **Podman** | `podman-compose` or `podman compose` | ✅ Supported | Rootless daemonless alternative; `podman-compose` binary preferred, else the `podman compose` plugin. |

### Detection contract

The shim resolves the compose command with a deterministic, first-match-wins order:

1. `AGENTSHROUD_COMPOSE` env var, if set — honored verbatim (escape hatch for exotic
   hosts / CI). Nothing overrides it.
2. `docker-compose` standalone binary — **the working deploy-host path**, kept first
   among auto-detected options so production behavior is unchanged.
3. `docker` CLI + working `docker compose` plugin.
4. `podman-compose` standalone binary.
5. `podman` CLI + working `podman compose` plugin.
6. None found → non-zero exit with a remediation message.

Sourced usage in a script:

```bash
. "$(dirname "$0")/lib/container-runtime.sh"
COMPOSE="$(detect_container_runtime)" || exit 1
$COMPOSE -f docker/docker-compose.yml -p agentshroud up -d
```

Override the runtime explicitly (e.g. to force podman on a host that also has docker):

```bash
export AGENTSHROUD_COMPOSE="podman compose"
scripts/asb up
```

The detection logic is covered by `scripts/smoke.d/test-container-runtime.sh`
(7 assertions using fake `docker`/`podman` stubs — no real daemon required), wired
into `scripts/smoke.sh`.

### Reproducible dev shell (Nix flake)

`flake.nix` provides the full toolchain (Python 3.11 + test/lint deps,
`docker-compose`, `ruff`, `black`, `shellcheck`, `node`, `pytest`). With Nix
(flakes enabled):

```bash
nix develop            # enter the dev shell with the whole toolchain
nix flake check        # build the dev shell + run lint + runtime-shim checks
nix run .#lint         # ruff + black --check + shellcheck
nix run .#smoke        # static startup smoke suite
```

---

## Files

### Core Configuration
- **Dockerfile.openclaw** - OpenClaw container (Python 3.11, non-root user)
- **docker-compose.yml** - Full stack orchestration (Gateway + OpenClaw)
- **QUICKSTART.md** - Step-by-step setup guide
- **.gitignore** - Prevents committing secrets

### Secrets
- **secrets/README.md** - API key setup instructions
- **secrets/anthropic_api_key.txt** - Your API key (create this file)

### Documentation
- **README.md** - This file

---

## Architecture

### Container Stack

```
┌─────────────────────────────────────────┐
│  agentshroud-gateway                     │
│  - Port: 127.0.0.1:8080 (REST API)      │
│  - Port: 127.0.0.1:8181 (CONNECT proxy) │
│  - PII sanitization + audit ledger      │
│  - Multi-agent routing                  │
│  - Approval queue (WebSocket)           │
└──────────┬───────────────────┬──────────┘
           │  172.20.0.0/16    │  172.21.0.0/16
           ▼                   ▼
┌──────────────────┐  ┌────────────────────────────────────┐
│  agentshroud-openclaw │  │  agentshroud-hermes  [--profile full│
│  (OpenClaw)      │  │  - Port: 8642 (OpenAI-compat API)  │
│  - Port: 18789   │  │  - Port: 9119 (dashboard)          │
│  - Node.js 22    │  │  - nousresearch/hermes-agent        │
│  - @agentshroud  │  │  - Python 3.11, non-root (UID 10000│
│    _bot          │  │  - @agentshroud_hermes_bot          │
└──────────────────┘  └────────────────────────────────────┘
                                  │
                       ┌──────────┘
                       ▼
           ┌──────────────────────────────┐
           │  agentshroud-hci             │
           │  [--profile full]            │
           │  - Port: 9121 (Basic-Auth)   │
           │  - Hermes Control Interface  │
           └──────────────────────────────┘

           ┌──────────────────────────────┐
           │  agentshroud-voice-gateway   │
           │  [--profile voice|full]      │
           │  - Port: 8765 (WebSocket)    │
           │  - Whisper STT + Piper TTS   │
           │  → ESP32-S3-BOX-3 terminal   │
           └──────────────────────────────┘
```

**Profile `full`** starts the complete stack (gateway + OpenClaw + Hermes + HCI + voice-gateway).
**Profile `voice`** starts gateway + voice-gateway only (useful for voice-terminal testing without the full bot stack).
Omitting profiles starts gateway + OpenClaw only (original default).

### Security Features (Implemented)

**Container Hardening**:
- ✅ Non-root execution (UID 1000:1000)
- ✅ Capability dropping (`cap_drop: ALL`)
- ✅ No new privileges (`no-new-privileges: true`)
- ✅ tmpfs on /tmp and /var/tmp only (noexec, nosuid)
- ✅ Resource limits (memory: 2GB, CPU: 2 cores, PIDs: 256)
- ✅ Health checks (30s interval, 3 retries)

**Network Isolation**:
- ✅ Internal-only Docker network
- ✅ Gateway bound to 127.0.0.1:8080 ONLY (no LAN access)
- ✅ OpenClaw not exposed to host (internal communication only)
- ✅ No 0.0.0.0 bindings

**Credential Security**:
- ✅ API key via Docker secrets (not environment variables)
- ✅ Mounted at `/run/secrets/anthropic_api_key` (400 permissions)
- ✅ Never logged or exposed in container output
- ✅ .gitignore prevents committing secrets

**Persona Integration**:
- ✅ IDENTITY, SOUL, USER files mounted read-only at `/workspace/`
- ✅ Loaded by OpenClaw on startup
- ✅ Session-scoped (no shared state between conversations)

**Data Persistence**:
- ✅ Gateway ledger: `gateway-data` volume
- ✅ OpenClaw conversations: `openclaw-data` volume
- ✅ Survives container restarts
- ✅ Can be wiped with `docker-compose down -v`

---

## Network DMZ — IEC 62443 FR5 (Restricted Data Flow) · SCRUM-93

AgentShroud segments its containers into tiers so that a compromised bot cannot
reach the internet or the host directly. This is the network-topology half of
SCRUM-93 (the gateway-logic half is MFA for high-risk approvals — see
`MFAGuard`).

**Tier model (defined in `docker/docker-compose.yml` → `networks:`):**

| Tier | Docker network | `internal` | Members | Purpose |
|------|----------------|-----------|---------|---------|
| Edge | `agentshroud-internal` (10.254.110.0/24) | `false` | **gateway only** | Internet-facing side; egress + host port publishing |
| DMZ (bots) | `agentshroud-isolated` (10.254.111.0/24) | `true` | gateway, openclaw, hermes | No internet; every egress hop forced through `gateway:8181` and inspected by the 76-module pipeline |
| DMZ (edge broker, opt-in) | `agentshroud-dmz` (10.254.113.0/24) | `true` | *(none by default)* | Reserved attachment point for a future reverse proxy / edge broker fronting the gateway |

**Why this is a DMZ:** the bot containers (`openclaw`, `hermes`) join
`agentshroud-isolated` **only**. That network is `internal: true`, so Docker
installs no default route to the internet — the bots physically cannot open an
outbound connection except to the gateway. The gateway is the sole conduit
between the internet-facing edge (`agentshroud-internal`) and the isolated DMZ,
so all bot traffic transits the security pipeline (PromptGuard, EgressFilter,
approval queue, etc.).

**Invariant — do NOT break:** the **gateway must stay on BOTH
`agentshroud-internal` AND `agentshroud-isolated`.** It is the only bridge
across the DMZ boundary; removing either membership breaks bot connectivity and
collapses FR5 isolation. The new `agentshroud-dmz` network is declared but
**intentionally left unattached** in the base compose file — attaching an edge
broker to it is an opt-in override, precisely so it can never regress the
gateway's mandatory dual membership.

**Verify the boundary:**

```bash
# Gateway is on both edge + DMZ networks (must show internal AND isolated):
docker inspect -f '{{range $k,$_ := .NetworkSettings.Networks}}{{$k}} {{end}}' agentshroud-gateway

# Bots are on the isolated DMZ ONLY (should NOT list agentshroud-internal):
docker inspect -f '{{range $k,$_ := .NetworkSettings.Networks}}{{$k}} {{end}}' agentshroud-openclaw

# The isolated network has no internet route (internal: true):
docker network inspect agentshroud_agentshroud-isolated -f '{{.Internal}}'   # → true
```

---

## MFA for High-Risk Approvals — IEC 62443 FR1 · SCRUM-93

Second factor (TOTP, RFC 6238) required to **approve** a high-risk queued action
(`email_sending`, `imessage_sending`, `file_deletion`, `external_api_calls`,
`skill_installation`, and destructive admin ops). Enforced at the approval-queue
`decide()` chokepoint by `gateway/security/mfa_guard.py::MFAGuard` — **fail-closed**
(missing/invalid/replayed code → approval denied). **Disabled by default**;
existing deployments are unchanged until an operator opts in.

| Env var | Meaning |
|---------|---------|
| `AGENTSHROUD_MFA_ENABLED` | `true`/`1`/`yes`/`on` to require a second factor |
| `AGENTSHROUD_MFA_SECRET` | Base32 TOTP shared secret (inline) — prefer the file form |
| `AGENTSHROUD_MFA_SECRET_FILE` | Path to a Docker-secret file holding the base32 secret (takes precedence) |
| `AGENTSHROUD_MFA_WINDOW` | Clock-skew tolerance in ±time-steps (default `1`) |

Provision the secret via Docker secrets — **never commit it**. Rejections never
require MFA, so the owner can always decline an action. The REST decide endpoint
returns HTTP `403` when the factor is missing/invalid; the approvals WebSocket
replies `{"type":"mfa_required"}`.

---

## Security Features (Deferred to Phase 5+)

These are planned but not yet implemented (Phase 3 has no skills, no external content):

- 🚧 Read-only root filesystem (requires OpenClaw compatibility testing)
- 🚧 Custom seccomp profile (skill execution hardening)
- 🚧 PromptGuard input filtering
- 🚧 SkillGuard sandboxing
- 🚧 MEMORY.md PII scrubber
- 🚧 Tailscale VPN for remote access
- 🚧 Outbound network allowlisting
- 🚧 ClawSec security suite

**Rationale**: Phase 3 delivers basic chat only. No skills = minimal attack surface. Advanced controls added when skills enabled in Phase 5.

---

## Usage

### Start the Stack

```bash
# Gateway + OpenClaw only (default)
docker-compose -f docker/docker-compose.yml -p agentshroud up -d

# Full stack — gateway + OpenClaw + Hermes + HCI
docker-compose -f docker/docker-compose.yml -p agentshroud --profile full up -d
```

### Check Status

```bash
docker-compose -f docker/docker-compose.yml -p agentshroud ps

# Default stack (gateway + OpenClaw):
# NAME                    STATUS              PORTS
# agentshroud-gateway     Up (healthy)        127.0.0.1:8080->8080/tcp
# agentshroud-openclaw    Up (healthy)        127.0.0.1:18789->18789/tcp

# Full stack additionally shows:
# agentshroud-hermes      Up (healthy)        127.0.0.1:8642->8642/tcp
#                                             127.0.0.1:9119->9119/tcp
# agentshroud-hci         Up (healthy)        127.0.0.1:9121->9121/tcp
```

### Port Reference

| Container | Port | Purpose |
|-----------|------|---------|
| agentshroud-gateway | 8080 | REST API + MCP proxy |
| agentshroud-gateway | 8181 | HTTP CONNECT proxy (bot egress) |
| agentshroud-openclaw | 18789 | OpenClaw chat API |
| agentshroud-openclaw | 18790 | OpenClaw web UI |
| agentshroud-hermes | 8642 | Hermes OpenAI-compatible API + /health |
| agentshroud-hermes | 9119 | Hermes agent dashboard |
| agentshroud-hci | 9121 | Hermes Control Interface (Basic-Auth) |

### View Logs

```bash
# All containers
docker-compose -f docker/docker-compose.yml -p agentshroud logs -f

# Specific container
docker-compose -f docker/docker-compose.yml -p agentshroud logs -f gateway
docker-compose -f docker/docker-compose.yml -p agentshroud logs -f hermes
```

### Hermes / HCI

Hermes and HCI are activated by the `full` compose profile.

**Prerequisites:**
1. Create `@agentshroud_hermes_bot` via @BotFather on Telegram.
2. Store the token in the "Agent Shroud Bot Credentials" 1Password vault as item `hermes-telegram`.
3. Run `docker/setup-secrets.sh store` to pull it into Docker secrets.

**Health check:**
```bash
curl http://localhost:8642/health
```

**HCI (Hermes Control Interface)** is available at `http://localhost:9121` and requires HTTP Basic Auth. Credentials are sourced from Docker secrets at startup.

### Test Chat

```bash
# Get auth token from gateway logs
docker-compose logs gateway | grep "Generated new token"

# Send message
curl -X POST http://localhost:8080/forward \
  -H "Authorization: Bearer <YOUR_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "What is your expertise in battery energy storage?",
    "source": "api",
    "content_type": "text"
  }'
```

### Stop the Stack

```bash
# Graceful shutdown
docker-compose down

# Nuclear option (deletes all data)
docker-compose down -v
```

---

## Troubleshooting

See [QUICKSTART.md](./QUICKSTART.md) for detailed troubleshooting steps.

**Common Issues**:

1. **Missing API key** → Add to `secrets/anthropic_api_key.txt`
2. **Port 8080 in use** → Stop other services or change port in docker-compose.yml
3. **Container unhealthy** → Check logs: `docker-compose logs <service>`
4. **401 Unauthorized** → Get token from gateway logs
5. **Network errors** → Verify Docker network: `docker network ls`

---

## Development

### Rebuild Containers

```bash
# After code changes
docker-compose up -d --build

# Force rebuild (no cache)
docker-compose build --no-cache
docker-compose up -d
```

### Exec into Container

```bash
# Gateway
docker exec -it agentshroud-gateway bash

# OpenClaw
docker exec -it openclaw-chat bash

# Check user (should be non-root)
docker exec openclaw-chat whoami
# Output: openclaw
```

### Verify Security

```bash
# Check running processes
docker exec openclaw-chat ps aux

# Check file permissions
docker exec openclaw-chat ls -la /workspace/
docker exec openclaw-chat ls -la /run/secrets/

# Check network config
docker network inspect docker_agentshroud-internal

# Verify no external ports on openclaw
docker ps | grep openclaw
# Should show NO host port mappings
```

---

## Startup Warnings Reference

Normal startup produces several warnings that are expected and harmless. This section explains each one so new users know what to ignore.

| Warning | Source | Meaning | Action required? |
|---------|--------|---------|-----------------|
| `⚠️  Gateway is binding to a non-loopback address` | OpenClaw | The bot gateway binds to `0.0.0.0:18789` so the AgentShroud gateway container (a different IP on the Docker network) can reach it. OpenClaw emits this warning whenever it isn't on loopback. The port is mapped as `127.0.0.1:18789` on the host and the Docker network is `internal: true` (no internet). Authentication is enforced by `AGENTSHROUD_GATEWAY_PASSWORD`. | ✅ No action — expected |
| `⚠ Brave Search API key unavailable` | start-agentshroud.sh | No Brave Search API key was found. Web search tool will be disabled but all other features work. | ℹ️ Optional — store key via `setup-secrets.sh store` if web search is needed |
| `WARN: secret extraction incomplete — starting with available secrets only` | scripts/asb | `setup-secrets.sh extract` could not find one or more secrets in the credential backend. Containers start in degraded mode; unconfigured features are disabled at runtime. | ℹ️ Optional — run `docker/setup-secrets.sh store` to configure missing secrets |
| `NOTE: host-specific token '...' not found — using production token` | scripts/asb | A host-specific Telegram bot token (e.g. `telegram_bot_token_marvin`) was not stored. Falls back to the production token. | ℹ️ Dev only — store a host token if you want a separate dev bot |
| `WARNING: grammY SDK not found at .../openclaw/node_modules/grammy/...` | patch-telegram-sdk.sh | grammY is bundled inside `openclaw/dist/extensions/telegram/` (not at the legacy top-level path). The OpenClaw dist patch still runs and succeeds — see the following `OpenClaw dist: patched N file(s)` line. | ✅ No action — expected since OpenClaw 2026.x |
| `op-proxy: disallowed reference blocked` | gateway | The bot requested a 1Password secret whose path isn't in `allowed_op_paths` in `agentshroud.yaml`. This is the gateway enforcing least-privilege on credential access. | ✅ No action unless a legitimate tool needs the path — add it to `allowed_op_paths` in `agentshroud.yaml` |
| `hermes: waiting for gateway...` | agentshroud-hermes | Hermes performs a readiness check against `http://gateway:8080/status` on startup. The message appears if the gateway container is still initializing. Resolves within a few seconds once the gateway is healthy. | ✅ No action — expected on cold start |
| `hci: hermes not reachable at :8642` | agentshroud-hci | The HCI startup probe checks Hermes health before opening its own listener. Retries automatically. | ✅ No action — resolves once Hermes passes its health check |

---

## Next Steps (Phase 4+)

Once chat is working:

1. **iOS Shortcuts** → Forward messages via Gateway API
2. **Shared File Volume** → Mount host directory for file access
3. **Browser Extension** → Forward URLs and selections
4. **Approval Dashboard** → Real-time UI for approval queue
5. **Advanced Security** → ClawSec suite, PromptGuard, SkillGuard
6. **Tailscale VPN** → Remote access via VPN only
7. **Auto-Deploy Scripts** → One-command setup

---

## Reference

**Phase 2 (Gateway)**: [../PHASE2_COMPLETE.md](../PHASE2_COMPLETE.md)
**Phase 3 (Container)**: [../PHASE3_REQUIREMENTS.md](../PHASE3_REQUIREMENTS.md)
**Project Status**: [../README.md](../README.md)
**Working State**: [../WORKING_STATE.md](../WORKING_STATE.md)

---

**Status**: ✅ Ready for user testing
**Pending**: User must add Anthropic API key to `secrets/anthropic_api_key.txt`
**Next**: Follow [QUICKSTART.md](./QUICKSTART.md) to start the stack


## Cron Failure Alerting (SCRUM-61)

The gateway watches both bots' persisted cron job stores and Telegrams the
owner when a job starts failing — no bot-side configuration needed.

Chain: `CronStateMonitor` (polls, default 60 s) → `AlertDispatcher` →
`POST /api/alerts` → event bus → `AlertTelegramRelay` → owner Telegram.

| Env var (gateway) | Default | Purpose |
|---|---|---|
| `AGENTSHROUD_CRON_STORES` | `openclaw:/data/bot-config/cron/jobs.json,hermes:/data/hermes-config/cron/jobs.json` | Comma-separated `bot:path` cron stores to watch |
| `AGENTSHROUD_CRON_MONITOR_INTERVAL` | `60` | Poll interval, seconds |

Alert policy: first failure of a job → HIGH (one Telegram); 3+ consecutive
errors → one CRITICAL escalation; recovery closes the episode (re-alerts on
the next failure). Relay-side: PII-sanitized, 24 h dedup, 10/h cap with an
explicit "N suppressed" notice, warnings can never starve critical alerts.

Requires the `hermes-config` volume mounted read-only into the gateway
(present in this compose file). A missing mount degrades gracefully — the
store is skipped with a debug log.

## Progressive-Trust Enforcement Mode (SCRUM-78)

Tool calls are gated by the progressive-trust ladder: an agent/user must reach
the trust level a tool requires (`gateway/security/progressive_trust_config.py`).
This is **enforced by default** — a level-too-low call is blocked.

To size the blast radius of a new or expanded ladder vocabulary before it
starts denying (or as an instant rollback valve), run in monitor mode:

```bash
AGENTSHROUD_PROGRESSIVE_ENFORCEMENT=monitor   # log "would-deny", don't block
AGENTSHROUD_PROGRESSIVE_ENFORCEMENT=enforce   # default: block (omit to keep)
```

In monitor mode the gateway logs `ToolACL MONITOR (would-deny) by trust ladder`
for each call that enforce mode *would* block, and per-user would-deny counts
accumulate on the enforcer — flip to `enforce` once the logs look clean.

## Multi-Bot Shared Report Store (SCRUM-79)

Reports (competitive intel, security summaries) are stored once in a
gateway-owned store on the `gateway-data` volume and read by any bot through
the gateway — no more per-bot duplicated pipelines or cross-container file
reads. Content is PII-sanitized on write.

| API (auth required) | Purpose |
|---|---|
| `POST /api/reports` | Store `{bot, title, content, tags}` (returns `{id}`) |
| `GET /api/reports[?bot=]` | List report metadata (no bodies), newest first |
| `GET /api/reports/{id}` | Fetch one report (metadata + content) |

| Env var | Default | Purpose |
|---|---|---|
| `AGENTSHROUD_REPORTS_DIR` | `/app/data/reports` | Store location on the gateway-data volume |

Report ids are server-generated and path-safe; the store rejects any
non-token id, caps content size (1 MB, matching the request-body limit),
bounds report count (oldest pruned), sanitizes ALL free-text fields
(content, title, tags), and tolerates corrupt files in listings.

**Confidentiality note:** the gateway-data volume is read-only-mounted into
both bots, so this is a **shared bulletin board — every bot can read every
report** (directly, even bypassing the API). It is not per-bot access-
controlled storage; that is why all free-text is sanitized on write. If
per-bot confidentiality is ever needed, give the store its own volume not
mounted into the bots.

## SOC Per-Module Enforcement Heat-Map (SCRUM-80)

Live, per-security-module allow/block/sanitize counts — the auditor-facing
"is enforcement actually happening?" view. Counts are **real** (recorded at
enforcement points), never fabricated; a module not yet instrumented reports
`instrumented: false` with genuine zeros.

| SOC API (auth required) | Purpose |
|---|---|
| `GET /soc/security/modules` | Modules with mode + live `stats` + `instrumented` flag |
| `GET /soc/security/modules/heatmap` | Aggregated per-module counts + totals |

Counts are process-lifetime (reset on gateway restart); durable enforcement
history lives in the audit ledger. Currently instrumented: `egress_filter`,
`tool_acl` — more modules feed the collector as they adopt
`record_decision()` from `gateway/security/module_stats.py`.
