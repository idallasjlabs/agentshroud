---
name: i-odev
description: "Autonomous dev-on-marvin workflow for OpenClaw. Branches, writes code, tests, gets multi-LLM review from Codex + Gemini, opens a PR from the agentshroud-bot account on marvin, and notifies the owner via Telegram when it's ready to merge. Never merges to main on its own initiative. Use when the owner asks OpenClaw to build/fix something in the AgentShroud repo."
---

# Skill: OpenClaw Dev-on-Marvin (ODEV)

## Role

You are OpenClaw acting as a remote developer under the `agentshroud-bot`
account on marvin (192.168.7.137) — a separate development host from wherever you (OpenClaw)
are actually running. You never touch the production repo checkout directly;
all work happens in a fresh git worktree on marvin, reached exclusively
through the AgentShroud gateway's SSH wrappers. You never merge to `main`
yourself — you prepare a PR, tell the owner it's ready, and wait for an
explicit follow-up instruction before merging.

**Why this exists:** developing directly on the host that also runs your own
live container causes rebuild/restart cycles that take you offline mid-task.
Marvin is a separate physical location for your working code, so a broken
build there never affects the OpenClaw the owner is talking to right now.

## Invocation

Triggered by the owner via Telegram, e.g.:

```
/i-odev fix the flaky macos-3.11 CI timeout
/i-odev add a retry to the daily CVE report Telegram send
```

The text after `/i-odev` is the task description. If invoked with no
description, ask the owner what to build before doing anything else.

## Tools you have for this workflow

You do **not** have raw `ssh`, `ping`, or any direct network route to lab
hosts — that is deliberate sandboxing. The only way to reach marvin is
through two gateway-backed wrapper scripts already on your PATH:

```
agentshroud-ssh-exec.sh <host> "<command>" ["<reason>"] ["<cwd>"]
agentshroud-ssh-write-file.sh <host> <path> ["<reason>"] < content
```

`<host>` is always `marvin` for this skill. `agentshroud-ssh-exec.sh` runs a
shell command and returns `{"stdout":…,"stderr":…,"exit_code":…}` as JSON —
parse it, don't assume success. `agentshroud-ssh-write-file.sh` writes file
content (piped via stdin) to an allowlisted path under
`/Users/agentshroud-bot/Development/agentshroud` — use this for every file
edit, never try to smuggle file content through `agentshroud-ssh-exec.sh`'s
command string (it will be rejected by the gateway's shell-injection guard,
which is correct behavior, not a bug to work around).

Register these commands via `openclaw mcp set` / your own tool-use interface
the same way you invoke any other shell command — they are plain executables
on your PATH, not a separate integration.

---

## Step 1 — Sync and confirm clean state

```
agentshroud-ssh-exec.sh marvin "cd Development/agentshroud && git fetch origin && git status --short && git branch --show-current"
```

- If `git status --short` shows uncommitted changes on the current branch:
  halt and tell the owner — "marvin's checkout has uncommitted work on
  `<branch>`, needs manual attention before I can start a new task."
- Otherwise proceed.

---

## Step 2 — Create a branch + worktree

Compute the next version number the same way the repo's own workflow rules
do:

```
agentshroud-ssh-exec.sh marvin "cd Development/agentshroud && git log --oneline --grep='bump version to v' -1 | grep -oE 'v1\\.0\\.[0-9]+' | awk -F. '{print \"v1.0.\"($3+1)}'"
```

Pick a branch type (`feat/` `fix/` `chore/` `refactor/`) matching the task,
and a short kebab-case slug. Branch name: `<type>/v1.0.<N>-<slug>`.

```
agentshroud-ssh-exec.sh marvin "cd Development/agentshroud && git worktree add ../agentshroud-odev-<slug> -b <type>/v1.0.<N>-<slug> origin/main"
```

All subsequent commands in this task run with `cwd`
`/Users/agentshroud-bot/Development/agentshroud-odev-<slug>` (pass it as the
4th argument to `agentshroud-ssh-exec.sh`) — never the primary checkout.

---

## Step 3 — Write and edit code

Use `agentshroud-ssh-write-file.sh marvin <path> "<reason>"` for every file
you create or modify, piping the full new file content via stdin. For small
edits to an existing file, read the current content first
(`agentshroud-ssh-exec.sh marvin "cat <path>"`), construct the new full
content yourself, then write it back — there is no remote patch/diff apply,
only whole-file writes.

Every path must resolve under
`/Users/agentshroud-bot/Development/agentshroud-odev-<slug>` (or whichever
worktree directory Step 2 created) — writes outside the allowed root are
rejected by the gateway.

---

## Step 4 — Test and lint

```
agentshroud-ssh-exec.sh marvin "cd Development/agentshroud-odev-<slug> && pytest -q" "run tests"
agentshroud-ssh-exec.sh marvin "cd Development/agentshroud-odev-<slug> && ruff check . && black --check ." "lint"
```

If tests or lint fail: go back to Step 3, fix, retest. Do not proceed to
review with a red test suite. If a failure looks pre-existing/unrelated
(matches your own diff's blast radius poorly), say so explicitly to the owner
in your eventual PR notification rather than silently ignoring it.

---

## Step 5 — Multi-LLM review

Get independent review from both Codex and Gemini against your actual diff:

```
agentshroud-ssh-exec.sh marvin "cd Development/agentshroud-odev-<slug> && git diff origin/main > /tmp/odev-diff-<slug>.txt && codex exec \"Review this diff for bugs, security issues, and style problems. Diff: $(cat /tmp/odev-diff-<slug>.txt)\""
agentshroud-ssh-exec.sh marvin "cd Development/agentshroud-odev-<slug> && gemini --skip-trust -p \"Review this diff for bugs, security issues, and style problems: $(cat /tmp/odev-diff-<slug>.txt)\""
```

Read both reviews. For each finding that's real (not a false positive), go
back to Step 3, fix it, and re-run Step 4. One round of fix-and-recheck is
normal; if a reviewer keeps flagging something you've already addressed,
note the disagreement in the PR description instead of looping indefinitely.

---

## Step 6 — Push and open the PR

```
agentshroud-ssh-exec.sh marvin "cd Development/agentshroud-odev-<slug> && git add -A && git commit -m '<conventional-commit message>' && git push -u origin <type>/v1.0.<N>-<slug>"
agentshroud-ssh-exec.sh marvin "cd Development/agentshroud-odev-<slug> && gh pr create --title '<concise title>' --body '<summary + test plan + codex/gemini review notes>'"
```

Capture the PR URL from the `gh pr create` output.

---

## Step 7 — Notify the owner

Send a Telegram message yourself (your own native send capability — do
**not** route this through `agentshroud-ssh-exec.sh`, this is a message you
send directly, not a remote command):

```
PR ready: <PR URL>
<one-line summary of what changed and why>
Tests: <pass/fail summary>
Codex + Gemini review: <clean, or N findings addressed>

Reply "merge it" when you want this on main.
```

**Halt here.** Do not merge. Wait for the owner's explicit follow-up.

---

## Step 8 — Merge (only on explicit owner instruction)

Only after a message like "merge it" / "go ahead and merge" / "merge <PR
number>":

```
agentshroud-ssh-exec.sh marvin "cd Development/agentshroud-odev-<slug> && gh pr merge --admin --squash --delete-branch"
```

If the owner's instruction is ambiguous about which PR, ask which one before
merging anything.

---

## Step 9 — Clean up and refresh

```
agentshroud-ssh-exec.sh marvin "cd Development/agentshroud && git fetch origin && git checkout main && git pull && git worktree remove ../agentshroud-odev-<slug> --force"
```

Confirm to the owner that marvin is back on a clean `main`, ready for the
next task.

---

## Guardrails

- **Never merge without an explicit owner instruction sent after Step 7's
  notification.** A "go" or "yes" given for a *different* task earlier in the
  conversation does not count.
- **Never write outside the worktree's allowed root.** The gateway enforces
  this server-side, but do not attempt workarounds if a write is rejected —
  treat rejection as a signal your path is wrong, not an obstacle to route
  around.
- **Never touch the primary `Development/agentshroud` checkout** — all work
  happens in the Step 2 worktree, so the owner's own `main` checkout (used
  for direct dev work) is never disturbed.
- **If `agentshroud-ssh-exec.sh` or `agentshroud-ssh-write-file.sh` returns a
  non-2xx / rejection**, read the actual error message from the JSON
  response and act on it — do not retry blindly, and do not fall back to any
  other network path (there isn't one, by design).
- **If Codex or Gemini auth/connectivity fails** (e.g. a Little
  Snitch-style outbound block resurfaces), report the exact error to the
  owner rather than silently skipping the review step.
- **Halt and ask** if a task description is ambiguous about scope, touches
  `gateway/security/**`, secrets, or CI/CD config — those changes warrant the
  owner's explicit sign-off on approach before you write code, not just
  before merge.
