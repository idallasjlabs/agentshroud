---
name: i-odev
description: "Autonomous dev workflow for OpenClaw, running under the agentshroud-bot account (same physical machine as production, isolated by user account — not a separate host). Two modes: a single task (branch, code, test, multi-LLM review, PR, notify, halt for merge approval) or a comprehensive multi-directory review-and-fix sweep across the whole repo. Uses Codex, Gemini, local models (LM Studio), and Claude Code together. Never merges to main on its own initiative."
---

# Skill: OpenClaw Dev Workflow (ODEV)

## Role

You are OpenClaw acting as a remote developer under the `agentshroud-bot`
account — the **same physical machine** production runs on, isolated only by
user account (not a separate host). You never touch the production repo
checkout (`ijefferson.admin`'s) directly; all work happens in a fresh git
worktree under `agentshroud-bot`'s own checkout, reached exclusively through
the AgentShroud gateway's SSH wrappers. You never merge to `main` yourself —
you prepare a PR, tell the owner it's ready, and wait for an explicit
follow-up instruction before merging.

**Why this exists:** developing directly in the checkout that also runs your
own live container causes rebuild/restart cycles that take you offline
mid-task. The `agentshroud-bot` account's checkout is a separate working copy
on the same box, so a broken build there never affects the OpenClaw the
owner is talking to right now.

## Invocation

Triggered by the owner via Telegram:

```
/i-odev fix the flaky macos-3.11 CI timeout          (single task)
/i-odev review gateway/web/,cli/,dashboard/           (comprehensive review, explicit scope)
/i-odev review                                        (comprehensive review, whole repo)
```

If invoked with no text at all, ask the owner which mode and what scope
before doing anything else. `review` (with or without a directory list)
triggers **Mode B** below; anything else is a task description for **Mode A**.

## Tools you have for this workflow

You do **not** have raw `ssh`, `ping`, or any direct network route to lab
hosts — that is deliberate sandboxing. The only way to reach the
`agentshroud-bot` checkout is through two gateway-backed wrapper scripts
already on your PATH:

```
agentshroud-ssh-exec.sh marvin "<single command>" ["<reason>"] ["<absolute cwd>"]
agentshroud-ssh-write-file.sh marvin <absolute path> ["<reason>"] < content
```

Critical constraints, confirmed by real use — not theoretical:

- **One command per call, no shell chaining.** `&&`, `|`, `;`, and bare `&`
  (backgrounding) in the command string are all rejected by the gateway's
  injection guard. Use the wrapper's own `cwd` argument instead of `cd X &&`.
  There is no way to background a long-running remote command through this
  channel — every call is synchronous.
- **`cwd` must be an absolute path.** A relative path is rejected outright.
- **`agentshroud-ssh-write-file.sh` writes content (piped via stdin)** to an
  allowlisted path — the primary checkout or a sibling worktree named
  `agentshroud-hdev-*`/`agentshroud-odev-*` under
  `/Users/agentshroud-bot/Development/`. There is no remote patch/diff apply,
  only whole-file writes — read the current content first
  (`agentshroud-ssh-exec.sh marvin "cat <path>"`), construct the new full
  content, then write it back.
- **Use `~/.venv/bin/python3 -m pytest ...` for all tests**, not the bare
  system `python3` — the venv has `gateway/requirements.txt` and the spaCy
  model installed; system Python does not.

## Jira ticket — every development batch gets one

**This is a standing rule, not optional:** every task (Mode A) or sweep (Mode
B) you run under this skill gets a real Jira ticket on the agentshroudai
SCRUM board (`https://agentshroudai.atlassian.net`), created near the start
and kept up to date as the work progresses — a GitHub PR alone is not
sufficient tracking.

**Critical distinction — do NOT run this via `agentshroud-ssh-exec.sh`.**
Every other command in this skill reaches the `agentshroud-bot` checkout on
marvin through the gateway's SSH wrappers. The Jira helper is different: it
runs directly in **your own container**, using your own network path to the
gateway (`GATEWAY_AUTH_TOKEN` is already in your environment) — the same
mechanism Hermes's `jira-weekly-review` cron job uses. Run it as a plain
local command, never prefixed with `agentshroud-ssh-exec.sh marvin`:

```
python3 /home/node/.openclaw/workspace/jira_dev_ticket.py create --project SCRUM --summary "<short title>" --description "<what and why>" --issue-type Task [--parent SCRUM-<epic>] [--labels openclaw,dev-batch]
python3 /home/node/.openclaw/workspace/jira_dev_ticket.py comment --issue SCRUM-<n> --body "<status update>"
python3 /home/node/.openclaw/workspace/jira_dev_ticket.py transition --issue SCRUM-<n> --status "<status name, e.g. In Progress / Done>"
```

`create` prints `{"key": "SCRUM-<n>"}` on success — capture that key, you need
it for every later `comment`/`transition` call. Every subcommand exits 0 on
success and 1 with a real error on stderr on failure; if it fails, report the
exact error to the owner rather than silently skipping the ticket update —
the same "no silent no-op" standard as everything else in this skill.

If the owner's request references a specific SCRUM epic (e.g. "continue the
v1.3.0 work"), pass `--parent` with that epic's key. Otherwise create a
standalone Task with no parent and mention in your Telegram notification that
the owner may want to link it to an epic themselves.

---

## Reviewers and fixer available to you

All four are pre-authenticated and confirmed working non-interactively from
this account — no env-var juggling required, each is durable across fresh
SSH sessions:

| Tool | Invocation | Notes |
|------|-----------|-------|
| Codex | `codex exec "<prompt>"` | Needs cwd inside a real git repo (its own trust gate). |
| Gemini | `gemini --skip-trust -p "<prompt>"` | `GEMINI_API_KEY` is exported automatically via `.zshenv` — do not try to set it yourself. |
| Local (LM Studio, Qwen3-14B) | `curl -sS -m 60 http://127.0.0.1:1234/v1/chat/completions -H "Content-Type: application/json" -d '{"model":"qwen/qwen3-14b","messages":[{"role":"user","content":"<prompt>"}]}'` | Reachable directly via loopback — same physical machine. Parse `.choices[0].message.content` from the JSON response. Free, private, no rate limits — prefer it for high-volume/simple checks when Codex/Gemini capacity matters. |
| Claude (fixer) | `claude -p "<prompt>"` | Has its own full file read/write/tool access in the given cwd — describe the issue, it applies the fix itself. Don't try to hand-apply diffs yourself. |

| Local (omlx, DeepSeek-R1-Qwen3-8B) | `curl -sS -m 60 -H "Authorization: Bearer $OMLX_API_KEY" http://127.0.0.1:8000/v1/chat/completions -H "Content-Type: application/json" -d '{"model":"DeepSeek-R1-0528-Qwen3-8B-6bit","messages":[{"role":"user","content":"<prompt>"}]}'` | `OMLX_API_KEY` is exported automatically via `.zshenv`, same as Gemini. Prefer this model over omlx's `gemma-4-12B-it-4bit` — the larger model has been observed to time out (60s+) under host memory pressure; the 8B model responds in ~6s. |

---

## Mode A — Single task

### Step 1 — Sync and confirm clean state

```
agentshroud-ssh-exec.sh marvin "git fetch origin" "" "/Users/agentshroud-bot/Development/agentshroud"
agentshroud-ssh-exec.sh marvin "git status --short" "" "/Users/agentshroud-bot/Development/agentshroud"
```

If `git status --short` shows uncommitted changes: halt and tell the owner —
"the checkout has uncommitted work on `<branch>`, needs manual attention
before I can start a new task." Otherwise proceed.

### Step 2 — Create a branch + worktree

```
agentshroud-ssh-exec.sh marvin "git log --oneline --grep=\"bump version to v\" -1" "" "/Users/agentshroud-bot/Development/agentshroud"
```

Read the output yourself and compute the next `v1.0.<N>` — do not pipe this
through grep/awk, the gateway rejects piped commands. Pick a branch type
(`feat/` `fix/` `chore/` `refactor/`) matching the task and a short
kebab-case slug: `<type>/v1.0.<N>-<slug>`.

```
agentshroud-ssh-exec.sh marvin "git worktree add ../agentshroud-odev-<slug> -b <type>/v1.0.<N>-<slug> origin/main" "" "/Users/agentshroud-bot/Development/agentshroud"
```

All subsequent commands use `cwd`
`/Users/agentshroud-bot/Development/agentshroud-odev-<slug>` — never the
primary checkout.

### Step 2b — Create the Jira ticket

Run this yourself, directly (not via `agentshroud-ssh-exec.sh` — see "Jira
ticket" above):

```
python3 /home/node/.openclaw/workspace/jira_dev_ticket.py create --project SCRUM --summary "<task summary>" --description "Branch: <type>/v1.0.<N>-<slug>. <what and why>" --issue-type Task --labels openclaw,dev-batch
```

Capture the returned key (e.g. `SCRUM-124`) — you'll comment on and
transition this same ticket in Steps 7 and 8. Immediately after creating it:

```
python3 /home/node/.openclaw/workspace/jira_dev_ticket.py transition --issue SCRUM-<n> --status "In Progress"
```

If the board has no transition matching "In Progress" by that exact name,
skip the transition (it's not fatal) but still proceed — the created ticket
itself is what matters most.

### Step 3 — Write and edit code

Use `agentshroud-ssh-write-file.sh` for every change, per the constraints
above.

### Step 4 — Test and lint

```
agentshroud-ssh-exec.sh marvin "~/.venv/bin/python3 -m pytest -q" "run tests" "/Users/agentshroud-bot/Development/agentshroud-odev-<slug>"
agentshroud-ssh-exec.sh marvin "ruff check ." "lint" "/Users/agentshroud-bot/Development/agentshroud-odev-<slug>"
agentshroud-ssh-exec.sh marvin "black --check ." "format check" "/Users/agentshroud-bot/Development/agentshroud-odev-<slug>"
```

If any fail: go back to Step 3, fix, retest. Do not proceed with a red suite.

### Step 5 — Multi-LLM review

Get independent review from Codex and Gemini against your actual diff (get
the diff text yourself first via a single `git diff origin/main` call, then
embed it in the review prompt — do not try to pipe it with `>`/`cat` chained
into the same command):

```
agentshroud-ssh-exec.sh marvin "git diff origin/main" "" "/Users/agentshroud-bot/Development/agentshroud-odev-<slug>"
agentshroud-ssh-exec.sh marvin "codex exec \"Review this diff for bugs, security issues, and correctness problems, with file:line citations: <diff text>\"" "" "/Users/agentshroud-bot/Development/agentshroud-odev-<slug>"
agentshroud-ssh-exec.sh marvin "gemini --skip-trust -p \"Review this diff for bugs, security issues, and correctness problems, with file:line citations: <diff text>\"" "" "/Users/agentshroud-bot/Development/agentshroud-odev-<slug>"
```

Only act on findings that are clearly real (either tool flags something
concrete and specific, not a vague style preference). Fix via `claude -p`
(see Mode B Step 2c for the exact pattern), re-run Step 4, repeat once if
needed. If a reviewer keeps flagging something you've already addressed,
note the disagreement in the PR instead of looping indefinitely.

### Step 6 — Build and validate containers

Build the affected images from THIS worktree's code, under a project name
that never collides with the live `agentshroud-bot` stack you're running
under — **build only, no `up`, no port binding, zero risk of disrupting the
OpenClaw you're talking to right now**:

```
agentshroud-ssh-exec.sh marvin "docker-compose -f docker/docker-compose.yml -f docker/docker-compose.agentshroud-bot.marvin.yml -p agentshroud-bot-verify build gateway openclaw" "" "/Users/agentshroud-bot/Development/agentshroud-odev-<slug>"
```

If the task touched `docker/bots/hermes/` or hermes-related gateway code,
also build hermes:

```
agentshroud-ssh-exec.sh marvin "docker-compose -f docker/docker-compose.yml -f docker/docker-compose.agentshroud-bot.marvin.yml -p agentshroud-bot-verify build hermes" "" "/Users/agentshroud-bot/Development/agentshroud-odev-<slug>"
```

Then run the static smoke suite — the same "Startup Smoke Tests (static)"
gate CI runs, no live containers, no port risk, catches config/wiring
errors before you ever push:

```
agentshroud-ssh-exec.sh marvin "bash scripts/smoke.sh" "" "/Users/agentshroud-bot/Development/agentshroud-odev-<slug>"
```

If a build or the smoke suite fails: read the actual error, go back to Step
3, fix, retest from Step 4. Do not open a PR on a failing build or smoke
suite.

Clean up the verify-only images afterward so they don't accumulate on disk:

```
agentshroud-ssh-exec.sh marvin "docker-compose -f docker/docker-compose.yml -f docker/docker-compose.agentshroud-bot.marvin.yml -p agentshroud-bot-verify down --rmi local" "" "/Users/agentshroud-bot/Development/agentshroud-odev-<slug>"
```

**Why not a live `up -d`:** a full live-and-monitored deploy is what the
owner's own redeploy already does after merge — duplicating it here would
mean either a silent port conflict (the live stack already holds those
ports) or a second, unmonitored live stack. Build + static smoke is the
safe, useful pre-merge signal.

### Step 7 — Update documentation and website

Judgment call, not a blanket action — only touch docs this specific change
actually affects:

- Changed a script's flags/usage, a module's public behavior, an API
  contract, or added/removed a skill? Update the corresponding file under
  `docs/` (check `docs/runbooks/`, `docs/reference/`, `docs/api/` for an
  existing page first — prefer editing over creating new).
- Only touch the public site (`docs/index.html`, `docs/CNAME`) if the
  change is genuinely public-facing (roadmap, feature list, install
  instructions). Most dev-batch tasks will not need this.
- If nothing applies, say so explicitly in the PR description ("no doc
  changes needed — internal fix, no documented behavior changed") instead
  of silently skipping the question.

### Step 8 — Update the knowledge graph

```
agentshroud-ssh-exec.sh marvin "graphify --version" "" "/Users/agentshroud-bot/Development/agentshroud-odev-<slug>"
```

If that fails (not installed), install it once — non-interactive, uses the
Gemini backend automatically since `GEMINI_API_KEY` is already exported in
your environment (no Claude subagent orchestration needed, unlike when the
owner runs `/graphify` interactively):

```
agentshroud-ssh-exec.sh marvin "pip install --user graphifyy -q" "" "/Users/agentshroud-bot/Development/agentshroud-odev-<slug>"
```

Then update the graph incrementally:

```
agentshroud-ssh-exec.sh marvin "graphify . --update --obsidian" "" "/Users/agentshroud-bot/Development/agentshroud-odev-<slug>"
```

This regenerates `graphify-out/` — include it in the commit in Step 9 like
any other changed file. If it errors for a reason other than "not
installed" (e.g. Gemini API connectivity), report the exact error and
proceed without it — it's a nice-to-have, not a merge gate.

### Step 9 — Push and open the PR

```
agentshroud-ssh-exec.sh marvin "git add -A" "" "/Users/agentshroud-bot/Development/agentshroud-odev-<slug>"
agentshroud-ssh-exec.sh marvin "git commit -m '<conventional-commit message>'" "" "/Users/agentshroud-bot/Development/agentshroud-odev-<slug>"
agentshroud-ssh-exec.sh marvin "git push -u origin <type>/v1.0.<N>-<slug>" "" "/Users/agentshroud-bot/Development/agentshroud-odev-<slug>"
agentshroud-ssh-exec.sh marvin "gh pr create --title '<concise title>' --body '<summary + test plan + review notes>'" "" "/Users/agentshroud-bot/Development/agentshroud-odev-<slug>"
```

Capture the PR URL from the output.

### Step 9b — Update the Jira ticket with the PR link

```
python3 /home/node/.openclaw/workspace/jira_dev_ticket.py comment --issue SCRUM-<n> --body "PR opened: <PR URL>. Tests: <pass/fail summary>. Review: <clean, or N findings addressed>."
```

### Step 10 — Notify the owner

Send a Telegram message yourself (your own native send capability — never
route this through `agentshroud-ssh-exec.sh`):

```
PR ready: <PR URL>
Jira: <SCRUM-n URL>
<one-line summary>
Tests: <pass/fail summary>
Review: <clean, or N findings addressed>

Reply "merge it" when you want this on main.
```

**Halt here.** Do not merge. Wait for the owner's explicit follow-up.

### Step 11 — Merge (only on explicit owner instruction)

```
agentshroud-ssh-exec.sh marvin "gh pr merge --admin --squash --delete-branch" "" "/Users/agentshroud-bot/Development/agentshroud-odev-<slug>"
```

If ambiguous which PR, ask before merging anything.

Once the merge succeeds, close out the Jira ticket:

```
python3 /home/node/.openclaw/workspace/jira_dev_ticket.py comment --issue SCRUM-<n> --body "Merged to main: <PR URL>."
python3 /home/node/.openclaw/workspace/jira_dev_ticket.py transition --issue SCRUM-<n> --status "Done"
```

If "Done" doesn't match an available transition name, the comment above is
still real tracking — don't treat a transition mismatch as a task failure.

### Step 12 — Clean up

```
agentshroud-ssh-exec.sh marvin "git checkout main" "" "/Users/agentshroud-bot/Development/agentshroud"
agentshroud-ssh-exec.sh marvin "git pull" "" "/Users/agentshroud-bot/Development/agentshroud"
agentshroud-ssh-exec.sh marvin "git worktree remove ../agentshroud-odev-<slug> --force" "" "/Users/agentshroud-bot/Development/agentshroud"
```

---

## Mode B — Comprehensive review sweep

Use when invoked as `/i-odev review [directory1,directory2,...]`. If no
directories given, use this default order (skip any already covered by an
open or recently-merged sweep PR unless the owner asks for a re-review):

```
gateway/security/ gateway/ssh_proxy/ gateway/ingest_api/ gateway/proxy/
gateway/soc/ gateway/runtime/ gateway/approval_queue/ gateway/web/
docker/scripts/ docker/bots/ scripts/ dashboard/ cli/ chatbot/
browser-extension/
```

### Step 1 — One branch + worktree for the whole sweep

Same as Mode A Steps 1-2, but the slug should reflect the sweep, e.g.
`chore/v1.0.<N>-comprehensive-review-<date>`. ALL directories in this sweep
share this single worktree/branch — do not create a new one per directory.

Then create ONE Jira ticket for the whole sweep (same as Mode A Step 2b, run
directly — not via `agentshroud-ssh-exec.sh`):

```
python3 /home/node/.openclaw/workspace/jira_dev_ticket.py create --project SCRUM --summary "Comprehensive review sweep <date>" --description "Directories: <list>. Branch: <slug>." --issue-type Task --labels openclaw,dev-batch,review-sweep
python3 /home/node/.openclaw/workspace/jira_dev_ticket.py transition --issue SCRUM-<n> --status "In Progress"
```

Capture the key — every directory's update in Step 2g comments on this same
ticket, not a new one per directory.

### Step 2 — Work through directories one at a time

For **each** directory, in order:

**a. Review** — get independent findings from Codex, Gemini, and (for a
quick supplementary pass) the local model:

```
agentshroud-ssh-exec.sh marvin "codex exec \"Review <directory> for bugs, security issues, and correctness problems. List concrete findings with file:line citations. Be specific — only report things you are confident are real, not style preferences.\"" "" "/Users/agentshroud-bot/Development/agentshroud-<slug>"
agentshroud-ssh-exec.sh marvin "gemini --skip-trust -p \"Review <directory> for bugs, security issues, and correctness problems. List concrete findings with file:line citations. Be specific — only report things you are confident are real, not style preferences.\"" "" "/Users/agentshroud-bot/Development/agentshroud-<slug>"
```

**b. Cross-reference.** Only act on findings BOTH tools raised, or a single
finding that is unambiguously a real bug (not a style nit). Everything else
goes in the final PR's "needs human review" table, not acted on.

**c. Fix** — for each confirmed issue:

```
agentshroud-ssh-exec.sh marvin "claude -p \"Fix this specific issue in <file>: <exact issue from the review, with file:line>. Make the minimal correct change — do not refactor unrelated code, do not add speculative error handling, do not add comments explaining what the code does.\"" "" "/Users/agentshroud-bot/Development/agentshroud-<slug>"
```

**d. Test** — run the closest matching test file(s):

```
agentshroud-ssh-exec.sh marvin "~/.venv/bin/python3 -m pytest gateway/tests/test_<matching>.py -q" "" "/Users/agentshroud-bot/Development/agentshroud-<slug>"
```

If tests fail, ask `claude -p` to fix its own regression, describing the
failure — up to 2 retries. If still broken, revert that file
(`git checkout -- <file>`) and note it as skipped.

**e. Lint + format:**

```
agentshroud-ssh-exec.sh marvin "black <changed files>" "" "/Users/agentshroud-bot/Development/agentshroud-<slug>"
agentshroud-ssh-exec.sh marvin "ruff check <changed files>" "" "/Users/agentshroud-bot/Development/agentshroud-<slug>"
```

Do this for every file you touch, every time — a prior sweep shipped a PR
that failed CI lint because this step was skipped.

**f. Commit** once this directory's tests pass:

```
agentshroud-ssh-exec.sh marvin "git add -A" "" "/Users/agentshroud-bot/Development/agentshroud-<slug>"
agentshroud-ssh-exec.sh marvin "git commit -m 'fix(<directory>): <summary>'" "" "/Users/agentshroud-bot/Development/agentshroud-<slug>"
```

**g. Telegram update** (your own native send, not ssh-exec) after every
directory, not just at the end:

```
[<directory>] reviewed. Codex+Gemini findings: N. Fixed: M. Skipped: K. Tests: <pass/fail>.
```

Also comment the same line on the sweep's Jira ticket (run directly, not via
`agentshroud-ssh-exec.sh`):

```
python3 /home/node/.openclaw/workspace/jira_dev_ticket.py comment --issue SCRUM-<n> --body "[<directory>] reviewed. Codex+Gemini findings: N. Fixed: M. Skipped: K. Tests: <pass/fail>."
```

### Step 3 — After the last directory (or a natural stopping point)

Once, for the whole sweep — not per-directory:

**a. Build and validate containers** — same as Mode A Step 6 (isolated
`agentshroud-bot-verify` project, build-only, no live `up`, then `bash
scripts/smoke.sh`, then tear down the verify images). If it fails, fix and
re-run before continuing.

**b. Update documentation and website** — same judgment call as Mode A Step
7, applied across everything the sweep touched.

**c. Update the knowledge graph** — same as Mode A Step 8
(`graphify . --update --obsidian`, installing it first if needed).

Then push, and open ONE PR summarizing every directory's findings and fixes
across the whole sweep (a table: directory | findings | fixed | skipped |
tests). Comment the PR link on the Jira ticket
(`jira_dev_ticket.py comment --issue SCRUM-<n> --body "PR opened: <PR URL>..."`).
Send a final Telegram message with the PR link and the Jira ticket link.
**Halt** — no merge without the owner's explicit follow-up, exactly like Mode
A Step 11. Once the owner explicitly merges, close out the ticket the same
way as Mode A Step 11 (comment + transition to "Done").

If you judge you've hit a natural stopping point before finishing the full
directory list (diminishing findings, or you're running low on your own
context), say so explicitly in the PR and Telegram message rather than
silently stopping — name which directories remain for a future sweep.

---

## Guardrails

- **Never merge without an explicit owner instruction sent after your PR
  notification.** A "go" or "yes" given for a *different* task earlier in
  the conversation does not count.
- **Never write outside the current worktree's allowed root.** Treat a
  rejection as a signal your path is wrong, not an obstacle to route around.
- **Never touch the primary `Development/agentshroud` checkout** for actual
  edits — only for Step 1/12's sync/cleanup, which only ever fetch/checkout/
  pull, never write files there.
- **If a tool call returns a real error** (not just "no issues found"), read
  the actual error and act on it — do not retry blindly, and do not
  workaround a rejection from the gateway's own guards (path allowlist,
  injection patterns) — those are correct behavior, not bugs.
- **If Codex/Gemini/local-model connectivity fails** (e.g. a Little
  Snitch-style outbound block resurfaces on a new binary), report the exact
  error to the owner rather than silently skipping that reviewer.
- **Halt and ask** if a task or directory touches `gateway/security/**`,
  secrets, or CI/CD config in a way that looks architectural rather than a
  clear bug fix — those warrant the owner's explicit sign-off on approach.
- **Never skip the Jira ticket.** It is run directly by you (`python3
  /home/node/.openclaw/workspace/jira_dev_ticket.py ...`), never through
  `agentshroud-ssh-exec.sh` — that wrapper only reaches marvin, not your own
  container's gateway network path. If the create/comment/transition call
  fails, report the real error; don't silently proceed without a ticket.
