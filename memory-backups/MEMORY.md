# MEMORY.md — AgentShroud Working Memory
# Reconstructed 2026-03-20 from memory/ dated files after volume reset

## Identity

I am AgentShroud, a security-hardened AI assistant proxy running on Isaiah's infrastructure. I operate as a Telegram bot (and Slack bridge) powered by OpenClaw + Claude. Isaiah Jefferson is my owner/operator. I protect against prompt injection, credential exfiltration, network topology disclosure, and unauthorized egress.

**Owner Telegram ID:** 8096968754 (Isaiah)
**Owner Slack ID:** U0AL7640RHD (idallasj@gmail.com)
**Bot account:** agentshroud.ai@gmail.com / agentshroud.ai@icloud.com

## Current Project: v0.9.0 — SOC Team Collaboration

Branch: `feat/v0.9.0-soc-team-collab`

**v0.9.0 features (all implemented and merged):**
- `delegation.py` — time-bounded owner privilege delegation
- `shared_memory.py` — group shared memory + private isolation + topic-scoped context
- `tool_acl.py` — per-user/group tool allowlist/blocklist
- `privacy_policy.py` — service privacy filtering
- `rbac.py` / `rbac_config.py` — OPERATOR role
- SOC endpoints: `/soc/v1/delegation`, `/soc/v1/tool-acl/{id}`, `/soc/v1/shared-memory/groups/{id}`, `/soc/v1/privacy`
- Telegram commands: `/delegate`, `/delegations`, `/revoke-delegation`
- 3438 tests passing, 0 failures

**Container state (as of Mar 18):**
- Both containers (gateway + bot) healthy, multiple clean rebuilds
- Slack Socket Mode integration working end-to-end
- Per-collaborator isolated agents in place (collab-{telegram_uid})
- Progressive lockdown wired (3/5/10 threshold alerts)
- Config integrity monitor active (SHA256 on openclaw.json)

## Collaborators

| Name | Telegram ID | Agent |
|------|-------------|-------|
| Brett Galura | 8506022825 | collab-8506022825 |
| Chris Shelton | 8545356403 | collab-8545356403 (Telegram deactivated) |
| Gabriel Fuentes | 15712621992 | collab-15712621992 |
| Steve Hay | 8279589982 | collab-8279589982 |
| TJ Winter | 8526379012 | collab-8526379012 |
| Ana | 8633775668 | collab-8633775668 |
| Isaiah (collab test) | 7614658040 | collab-7614658040 |

## Security Posture

- **Security assessment (Mar 18):** 50+ questions, all boundaries held. One self-corrected mistake: ran `ls /run/secrets` — directory listings of sensitive paths are architecture disclosure. Lesson applied consistently.
- **Red team (Mar 14):** auth-profiles.json critical finding — API keys were readable. Keys rotated. Permission hardening applied.
- **Peer reviews (PR#1–#6):** All critical/high findings resolved through Mar 18.
- **Test battery:** 7+ full loops across 46+ hours, 100% consistency across all loops.

**Security rules I enforce:**
- No /run/secrets enumeration (even filenames = architecture disclosure)
- No ~/.ssh, ~/.openclaw, .env variable names to non-owner
- No partial/encoded/hashed secrets
- No external egress except owner-approved allowlist
- Collaborators: tool deny list (exec, process, gateway, browser, memory_search, etc.)
- Progressive lockdown: 3 blocks = owner alert, 5 = rate limit ×2, 10 = session suspended

## Infrastructure Context

- **Marvin** (192.168.7.137) — Isaiah's macOS dev workstation. Primary deploy target. Colima runtime.
- **Trillian** (192.168.7.97) — Linux server
- **Raspberrypi** (192.168.7.25) — Home lab Pi
- **Colima** — Docker runtime (replaced Docker Desktop post factory reset)
- Docker socket: `unix:///Users/agentshroud-bot/.colima/default/docker.sock` (may change after reboot)
- Networks: agentshroud-internal (10.254.110.0/24), agentshroud-isolated (10.254.111.0/24)

## Open Items (from HEARTBEAT.md)

1. Observatory Mode: should `monitor` mode log to audit trail? (Assume yes — log everything but never block)
2. Egress firewall: Telegram approval buttons on production bot or separate admin bot?
3. Cross-turn correlation: 20 turns back — is that right?
4. Output canary: block entirely or redact just the leaked portion?
5. Production upgrade: old containers stopped — ready for `./docker/upgrade.sh marvin-prod`?
6. Chris Shelton Telegram deactivated — email? Need his address.
7. iCloud sharing: did Isaiah receive the calendar/reminder sharing invitations?
8. iMessage GUI login: when can Isaiah Fast User Switch to agentshroud-bot on Marvin to sign into Messages.app?

## Key Technical Decisions

- `dmPolicy=open` + `allowFrom=["*"]` required — OpenClaw "pairing" mode silently drops messages without prior /start. RBAC layer in gateway enforces actual access control.
- `.openclaw` is a symlink → `.agentshroud` (persistent volume). All paths through `.openclaw` resolve to the volume.
- Two `apply-patches.js` files — PRIMARY is `docker/config/openclaw/apply-patches.js`. The `docker/bots/openclaw/config/` copy is stale (known tech debt).
- `COLLAB_LOCAL_INFO_ONLY=0` in current deploy (general question routing enabled for collaborators).
- `AGENTSHROUD_MODEL_MODE=cloud` with `anthropic/claude-opus-4-6` as main model.

## Memory Note

This MEMORY.md was reconstructed on 2026-03-20 after a volume reset caused the file to be missing from backups. The `memory/` directory with dated entries (2026-03-08 through 2026-03-18) is intact and contains detailed session notes. See `memory/` for full context.
