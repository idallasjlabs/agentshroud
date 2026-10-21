## Mode B — Comprehensive review sweep

Use when invoked as `/i-hdev review [directory1,directory2,...]`. If no
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
python3 /opt/data/workspace/jira_dev_ticket.py create --project SCRUM --summary "Comprehensive review sweep <date>" --description "Directories: <list>. Branch: <slug>." --issue-type Task --labels hermes,dev-batch,review-sweep
python3 /opt/data/workspace/jira_dev_ticket.py transition --issue SCRUM-<n> --status "In Progress"
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
python3 /opt/data/workspace/jira_dev_ticket.py comment --issue SCRUM-<n> --body "[<directory>] reviewed. Codex+Gemini findings: N. Fixed: M. Skipped: K. Tests: <pass/fail>."
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
