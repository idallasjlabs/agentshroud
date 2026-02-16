# CLAUDE.md — SecureClaw Repository Constitution

> **"One Claw Tied Behind Your Back"** — You decide what the agent sees, not the agent.

---

## Prime Directive

You are working on **SecureClaw**, an open-source security proxy layer for OpenClaw.
The codebase lives on a **Raspberry Pi 4 (8GB, Debian 11, ARM64)** accessed via Tailscale SSH.

**Rules:**
1. **TDD always.** Red → Green → Refactor. No exceptions.
2. **No new files unless explicitly requested.** Don't create docs, configs, or helpers speculatively.
3. **No opportunistic refactors.** Fix what you're asked to fix. Nothing more.
4. **Security first.** This is a security product. Every change gets security review.
5. **Tests must be fast and isolated.** No real network, no real DB, no sleeps.

---

## Project Overview

- **Gateway** (`gateway/`): FastAPI proxy — PII sanitizer, audit ledger, approval queue, multi-agent router
- **Chatbot** (`chatbot/`): Telegram bot interface
- **Docker** (`docker/`): Hardened containers (seccomp, cap_drop ALL, read-only FS, secrets)
- **Skills** (`.claude/skills/`): TDD, QA, CR, PR, Git Guard, CI/CD, etc.
- **Agents** (`.claude/agents/`): Dev team roles

## Environment

| Item | Value |
|------|-------|
| Host | Raspberry Pi 4 Model B (8GB) |
| OS | Debian 11 (Bullseye) aarch64 |
| Python | 3.11 via miniforge3 (`~/miniforge3/envs/oneclaw`) |
| Node | v22 |
| Docker | 29.x |
| Network | Tailscale only |
| SSH | `secureclaw-bot@raspberrypi.tail240ea8.ts.net` |
| Repo | `~/Development/oneclaw` |

### Running Tests
```bash
~/miniforge3/envs/oneclaw/bin/python -m pytest gateway/tests/ -v
```

### Running with Coverage
```bash
~/miniforge3/envs/oneclaw/bin/python -m pytest gateway/tests/ --cov=gateway --cov-report=term-missing
```

### Code Quality
```bash
~/miniforge3/envs/oneclaw/bin/python -m ruff check gateway/
~/miniforge3/envs/oneclaw/bin/python -m black --check gateway/
```

---

## Definition of Done

A task is done when:
- [ ] Tests written FIRST (TDD red phase)
- [ ] All tests pass (green phase)
- [ ] Code cleaned up (refactor phase)
- [ ] Coverage ≥ 80% on changed files
- [ ] No security regressions
- [ ] Committed on a feature branch (never direct to main)
- [ ] PR opened with: summary, how tested, rollback plan

## Git Workflow

- Branch from latest `main`: `feat/description`, `fix/description`, `test/description`
- Commit messages: `type: short description` (feat, fix, test, docs, refactor, chore)
- Squash merge PRs
- Never force-push to `main`

## Security Constraints

- **No credentials in code.** Use `op read` or Docker secrets.
- **No `op item get --format json`** — always `op read <reference>`.
- **No direct filesystem access** from OpenClaw container.
- **All data flows through gateway.**
- **Approval queue** for sensitive operations.
- **Audit everything.**

## Pi-Specific Notes

- ARM64 — some packages need aarch64 builds
- CPU is 2-3x slower than x86 — be patient with builds
- 8GB RAM — set container memory limits
- No sudo for `secureclaw-bot` — use conda, not system packages
- Original `.venv` (Python 3.9) is for Mac — don't touch it
- Use `~/miniforge3/envs/oneclaw/bin/python` for everything

## Current Status

- **Coverage:** 92% (116 tests)
- **Branch:** `fix/code-review-2026-02-16`
- **Phase:** 3A/3B complete, Phase 4 (SSH Capability) in progress
- **Grade:** B+

## Agent Hierarchy

- **Claude Code** is the PRIMARY developer (via `.claude/agents/developer`)
- All other agents are SECONDARY — they do not write production code
- See `.claude/agents/` for the full team
