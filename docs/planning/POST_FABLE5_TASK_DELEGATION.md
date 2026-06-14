# Post-fable-5 Task Delegation

**Date:** 2026-06-11
**Context:** The 2026-06-11 full review identified 5 engineering priorities that DO need
claude-fable-5 (tracked in PRs #159–#163 + the `_filter_outbound` refactor and OpenAPI
contract work). The tasks below were explicitly triaged as **not** requiring the most
powerful model — they are mechanical, process-driven, manual, or infrastructure-blocked,
and can be handled by secondary agents (Gemini/Codex per
`docs/governance/AGENT_ROLES.md`) or by Isaiah directly after fable-5 access ends
2026-06-22.

## Task list

| # | Task | Why it doesn't need the top model | Recommended owner | Status / blockers |
|---|------|-----------------------------------|-------------------|-------------------|
| 1 | Coverage grind 85% → 94% (CI gate currently 84, measured 85.39%) | Mechanical test-writing against existing behavior; no architectural judgment | Codex / Gemini (test augmentation is their lane per AGENT_ROLES.md) | Open; large but parallelizable module-by-module |
| 2 | Weekly kaizen cron re-wire (`CronCreate "47 16 * * 5"`) | One scheduling command per session | Any session agent | Session-only wiring — re-arm each session (workflow debt #4) |
| 3 | Monthly chaos drill cron re-wire (`CronCreate "3 9 1 * *"`) | One scheduling command per session | Any session agent | Session-only wiring — re-arm each session (workflow debt #5) |
| 4 | Formal sprint cadence + Jira discipline | Process adoption, not engineering | Isaiah + any agent | `/scrum`, `/agile`, `/pm` skills installed but unused (workflow debt #3) |
| 5 | Canary / progressive rollout | Infrastructure provisioning, not code design | Isaiah (infra decision) | **Blocked:** needs ≥2 prod instances; only marvin today (workflow debt #2) |
| 6 | Rotate OpenClaw Telegram bot token via BotFather | Manual credential operation — no agent should handle the live token | **Isaiah (manual)** | **Outstanding:** token exposed in an AI session on 2026-06-11; rotate, then update 1Password "Agent Shroud Bot Credentials" + `docker/setup-secrets.sh extract` + redeploy |
| 7 | Branch-protection toggle audit | Manual GitHub Settings → Branches checklist | Isaiah (manual) | Checklist in `docs/governance/BRANCH_PROTECTION.md` |
| 8 | Dev-instance chores on marvin (`agentshroud-bot` account) | Routine ops commands | Isaiah / any agent | `op signin` (CLI has no accounts) → `./docker/setup-secrets.sh extract` → `asb rebuild`; clear webchat localStorage at `http://127.0.0.1:18790` to fix device_token_mismatch |
| 9 | Pi-hole DNS restore | One env-var change + redeploy | Any agent | Waiting on Pi-hole (192.168.7.45) health; then set `AGENTSHROUD_DNS_PRIMARY=192.168.7.45` in `docker/.env` and redeploy |
| 10 | Obsidian vault docs upkeep (`.obsidian-vaults/` module map, git-log notes, ADRs) | Document analysis and summarization | Gemini (its designated lane) | Ongoing maintenance; refresh after the current PR train merges |

## Notes

- Items 6 and 7 are **manual, user-owned** — no agent should execute them.
- Item 5 is the only infrastructure-blocked item; everything else is actionable now.
- Security-relevant judgment calls (anything touching `gateway/security/`, the outbound
  pipeline, or trust/ACL logic) stay with the primary agent regardless of model, per the
  multi-agent hierarchy in `CLAUDE.md` §0.1.
