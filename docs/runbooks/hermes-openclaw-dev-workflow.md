# Starting a Development Task via Hermes / OpenClaw

## Status: ready to use, with 4 known gaps (see below)

Both bots run under the `agentshroud-bot` account on marvin (same physical
machine as production, isolated by user account, not a separate host — see
`docs/runbooks/colima-docker-guide.md`). Both are healthy as of this writing:

```
personal gateway:  http://localhost:8080/status       → {"status":"healthy","version":"1.3.0"}
bot gateway:        http://localhost:9080/status       → {"status":"healthy","version":"1.3.0"}  (via ssh agentshroud-bot@192.168.7.137)
```

---

## How to start a task

Send a Telegram message to whichever bot you want doing the work:

```
/i-hdev <task description>              — Hermes, single task
/i-odev <task description>              — OpenClaw, single task
/i-hdev review <dir1,dir2,...>          — Hermes, comprehensive review sweep (specific dirs)
/i-hdev review                          — Hermes, comprehensive review sweep (whole repo)
/i-odev review [dirs]                   — same, OpenClaw
```

If you send `/i-hdev` or `/i-odev` with no text, the bot will ask you which
mode and scope before doing anything — it will not guess.

**Which bot to use:** either is equivalent for this workflow — same skill,
same guardrails, same tools. Pick based on which one you're already talking
to, or split unrelated tasks across both to run them in parallel.

---

## What happens automatically (confirmed real, in
`docker/config/{hermes,openclaw}/skills/i-hdev|i-odev/SKILL.md`)

1. **Sync + safety check** — fetches `origin/main` in the `agentshroud-bot`
   checkout, halts if that checkout has uncommitted changes (never runs on
   top of dirty state).
2. **Branch + worktree** — creates `<type>/v1.0.<N>-<slug>` and a dedicated
   git worktree under `/Users/agentshroud-bot/Development/`. It never edits
   the primary checkout directly, and never touches your own
   `ijefferson.admin` checkout.
3. **Jira ticket** — creates a real ticket on the `agentshroudai` SCRUM board
   near the start of every task or sweep, transitions it to "In Progress",
   and keeps commenting on it as work progresses (PR link, review outcome,
   final merge). Not optional — a PR alone is never treated as sufficient
   tracking.
4. **Code + test + lint** — writes changes via a gateway-mediated
   write-file wrapper (no direct filesystem access), runs `pytest`, `ruff`,
   `black --check`. Loops back to fix on any failure — never proceeds with a
   red suite.
5. **Multi-LLM review loop** — gets independent review from **Codex**
   (`codex exec`) and **Gemini** (`gemini --skip-trust`) against the actual
   diff. Only acts on findings both flag, or a single finding that's
   unambiguously a real bug. **Claude is the fixer**, not a third reviewer —
   `claude -p` applies the fix directly, then the test/lint step re-runs.
   This is the "loop until resolved" you asked about: review → fix (Claude)
   → retest, repeating once if a reviewer still flags something after the
   first fix. If a reviewer keeps flagging something already addressed, that
   disagreement is noted in the PR rather than looped indefinitely.
6. **PR opened**, Jira commented with the PR link, **Telegram notification**
   sent with the PR URL, Jira ticket link, test/review summary.
7. **Halts.** Does not merge. Waits for your explicit reply (e.g. "merge
   it") in the *same* conversation — an approval given for a different task
   earlier does not count.
8. **On your explicit merge instruction**: `gh pr merge --admin --squash
   --delete-branch`, then closes out the Jira ticket (comment + transition
   to "Done"), cleans up the worktree.

For a comprehensive review sweep (`review` mode), steps 4-6 repeat per
directory (default order: `gateway/security/`, `gateway/ssh_proxy/`,
`gateway/ingest_api/`, `gateway/proxy/`, `gateway/soc/`, `gateway/runtime/`,
`gateway/approval_queue/`, `gateway/web/`, `docker/scripts/`,
`docker/bots/`, `scripts/`, `dashboard/`, `cli/`, `chatbot/`,
`browser-extension/`), with a Telegram + Jira update after *every*
directory, all under one branch/worktree/PR/ticket for the whole sweep.

---

## What is **not** currently automated (the 4 gaps)

You asked for these and they are reasonable, but they are not in the skill
today — the bot will not do them unless you separately ask, either in the
same conversation after the PR is up, or by extending the skill itself:

| You asked for | Current state |
|---|---|
| Build all containers | Not run. The skill tests via `pytest`/`ruff`/`black` in the worktree, never does a docker rebuild. |
| Monitor + resolve all errors in logs | Not run. No log-tailing/error-triage step exists in the skill. |
| Update all documentation and the website | Not run. No doc/website step exists in the skill. |
| `graphify . --update --obsidian` | Not run. Nothing in the skill invokes graphify. |

**Recommendation:** don't bolt these onto every single task — a one-line
typo fix doesn't need a full container rebuild or a graphify update. Instead:
ask for them explicitly when a task actually warrants it ("also rebuild and
verify containers before you open the PR"), or say the word and I'll extend
`i-hdev`/`i-odev` (both `docker/config/hermes/...` and
`docker/config/openclaw/...` copies, they must stay identical) to add these
as an optional post-review step for sweeps specifically, gated behind the
same "halt for approval" boundary as the merge step — since a container
rebuild and a graphify regen are exactly the kind of thing that should be
reviewed before landing, not run silently on every task.

---

## Monitoring progress

**Telegram** — this is the primary channel; you'll get a message after every
directory in a sweep, and a final one when the PR is ready.

**Hermes dashboard** — `http://localhost:9119` (personal) — shows live
session activity, cron jobs, memory.

**OpenClaw canvas/UI** — `http://localhost:18789` (personal) — same idea for
OpenClaw.

For the bot account specifically (dev instance, not the ones above): SSH in
and check directly —
```bash
ssh agentshroud-bot@192.168.7.137 'curl -s http://localhost:9080/status'
ssh agentshroud-bot@192.168.7.137 'docker ps --format "table {{.Names}}\t{{.Status}}"'
```

**Ask Claude Code (me)** — at any point, ask me to check:
- `gh pr list --state open` / `gh pr view <n>` — PR + CI status
- Jira SCRUM board directly (I have MCP access) — ticket status
- `ssh agentshroud-bot@192.168.7.137 'cd .../agentshroud-hdev-<slug> && git log --oneline -5'` — commit progress
- Container logs on either environment if something looks stuck

---

## Things that will make a task halt and ask you, not fail silently

- Uncommitted changes already in the `agentshroud-bot` checkout.
- A task or directory that touches `gateway/security/**`, secrets, or
  CI/CD config in a way that looks architectural rather than a clear bug
  fix — the skill explicitly halts for your sign-off on approach.
- Codex/Gemini/local-model connectivity failure — reported to you, not
  silently skipped.
- Any Jira API failure — reported, not silently proceeded past.
- Ambiguity about which PR to merge, if you have more than one in flight.

---

## Source of truth

The skill files are version-controlled and identical in shape for both
bots (only the bot name and a couple of file paths differ):
- `docker/config/hermes/skills/i-hdev/SKILL.md`
- `docker/config/hermes/skills/i-odev/SKILL.md`
- `docker/config/openclaw/skills/i-hdev/SKILL.md`
- `docker/config/openclaw/skills/i-odev/SKILL.md`

Changes to these are pushed live via `scripts/update-bot-agents.sh` (Hermes:
zero-restart, writable volume; OpenClaw: read-only rootfs, staged for next
image rebuild). If you ask me to add the 4 missing steps above, this is
where the change lands, and — per this repo's own rules — that change goes
through a normal branch → PR → CI → your merge-approval cycle before it's
live, same as any other code change.
