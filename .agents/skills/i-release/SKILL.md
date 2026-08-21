---
name: i-release
description: "Full release workflow triggered by 'release it': verify CI and update the open PR, merge to main, refresh the graphify knowledge graph, bump/sync the version and tag+publish a GitHub release, update documentation and confirm every service reports the new version, close the driving Jira issue and its sprint, then rebuild/restart both the local prod stack and the remote dev environment (agentshroud-bot host) from main."
---

# Skill: Release (i-release)

## Role

You are executing AgentShroud's end-to-end release process. This is a
production-impacting, multi-system workflow (GitHub, Jira, two live deploy
targets) — work through it in order, verify each step actually succeeded
before moving to the next, and report status honestly if anything fails
rather than proceeding past a broken step.

## Invocation

Triggered by the owner saying "release it" (or equivalent — "ship it",
"release this") with an open PR already in flight that this session has been
working on. If it's ambiguous which PR/branch, ask before proceeding — never
guess which PR to release.

## Steps

### 1. Verify CI and update the PR

```bash
gh pr checks <PR#>
```

All required checks must be green, or failing only on the documented
pre-existing flake (`test (macos-latest, 3.11)`, see
`reference_ci_known_flakes.md` in memory — and note `pytest-timeout` was
added 2026-08-14 specifically so a real hang there fails fast instead of
silently burning 20 minutes; a failure now is more likely a genuine bug than
before). If something is genuinely broken, fix it — don't route around a
real failure. If the PR description is stale relative to what actually
shipped (e.g. a fix commit landed after the description was written), update
it with `gh pr edit <PR#> --body "..."` so the merged history reads
accurately.

### 2. Merge

Solo-author PRs on this repo require an admin override (branch protection
`REVIEW_REQUIRED` — see `reference_branch_protection.md`):

```bash
gh pr merge <PR#> --admin --squash --delete-branch
```

Then sync local main:

```bash
git checkout main && git pull
git branch -d <feature-branch>   # if it still exists locally
```

### 3. Update graphify

```bash
/graphify
```

Run this from the repo root on the freshly-merged main so the knowledge
graph reflects the new code. This is a full pipeline run, not `--update`,
unless the graph is already current apart from this merge (`--update` is
fine then — see the graphify skill for when each applies).

**Always include the Obsidian vault** (owner-confirmed 2026-08-14):
`graphify-out/obsidian/` is a first-class deliverable of every graphify run
in this repo, not optional. Pass `--obsidian`, or if the flow taken doesn't
already export it, follow up explicitly with `graphify export obsidian`
before considering this step done — check for freshly-added/changed nodes'
corresponding `.md` files as a spot check.

When committing `graphify-out/` after a full or vault-inclusive update,
stage in batches of ~500 files — `git add --pathspec-from-file=<nul-separated-file>
--pathspec-file-nul` — never `git add graphify-out/` or `git add -A` in one
shot. The repo's `git-secrets` pre-commit hook builds a single `git grep`
argv from every staged file; 500+ files (especially with the vault's
emoji/unicode filenames) overflows it with a bash-level "Argument list too
long", not a real secret finding. If a commit fails this way, `git reset`
first — a failed commit leaves everything staged, so the next attempt
re-scans the same oversized set and fails identically.

### 4. Tag and release

Version is sourced from `gateway/__init__.py`'s `__version__` — bump it
first (semver: patch for fixes, minor for new capability/feature work, per
this repo's own history of v1.3.0 → v1.4.0 for meaningful feature jumps),
then sync every mirror:

```bash
# Edit gateway/__init__.py: __version__ = "X.Y.Z"
scripts/sync-version.sh          # propagates to gateway/pyproject.toml + docker/versions.env
git add gateway/__init__.py gateway/pyproject.toml docker/versions.env
git commit -m "chore(release): bump version to vX.Y.Z"
git push
git tag vX.Y.Z
git push origin vX.Y.Z
```

Pushing the tag triggers `.github/workflows/release.yml`, which independently
verifies `scripts/sync-version.sh --check` and that the tag matches
`gateway/__init__.py`'s `__version__` — if either check fails, the release
job fails loudly rather than shipping a mismatched version. Watch it:

```bash
gh run list --workflow=release.yml -L 1
gh run watch <run-id>
```

Once the release workflow completes, confirm the GitHub Release itself was
created with real notes (not just the tag):

```bash
gh release view vX.Y.Z
```

If the workflow only tags and doesn't author release notes, write and
publish them: `gh release create vX.Y.Z --title "vX.Y.Z" --notes "..."`
summarizing what shipped (pull the PR list since the last tag via
`git log <prev-tag>..vX.Y.Z --oneline` for the real content, not a guess).

### 5. Documentation and version visibility

`scripts/sync-version.sh` only covers `gateway/pyproject.toml` and
`docker/versions.env` — it does NOT touch hand-written docs. Check and update
by hand:

- `AGENTS.md`'s `| **Current Version** | vX.Y.Z |` row (project identity
  table, section 1) — this has drifted before (found stale at v1.3.0 while
  v1.4.0 had already shipped, 2026-08-14) and is easy to forget since nothing
  automated enforces it.
- `docs/` — check for a changelog, release-notes page, or version-referencing
  content under `docs/architecture/`, `docs/project/`, or the public site
  (`docs/index.html`) if this release is genuinely public-facing.
- Confirm every running service actually reports the new version at runtime,
  not just in source: gateway `/status` endpoint, Hermes dashboard, voice
  gateway's system-prompt version string (there was a live regression
  2026-08-08 where it answered "1.0.0" from nowhere — verify this isn't
  silently stale again) — check these AFTER the rebuild step below, since
  that's when the new version actually becomes live.

### 6. Close Jira

Comment with the PR/release link, then transition:

```
mcp__atlassian__addCommentToJiraIssue(cloudId=..., issueIdOrKey="SCRUM-N",
  commentBody="Merged: <PR URL>. Released: vX.Y.Z (<release URL>).")
mcp__atlassian__transitionJiraIssue(cloudId=..., issueIdOrKey="SCRUM-N",
  transition={"id": "41"})   # Done — confirm the id via getTransitionsForJiraIssue first if unsure
```

Then close the sprint containing that issue. The dedicated sprint-management
tools (`jira_update_sprint`, `jira_move_issues_to_backlog`) have had
recurring auth failures on this project's connectors (`atlassian-idallasj`:
OAuth session error; `atlassian-agentshroud`: generic failure) even when the
generic `mcp__atlassian__*` issue-write tools work fine — if sprint-close
fails the same way again, don't silently give up: move any other incomplete
issues in the sprint out first (`editJiraIssue` with `customfield_10020:
null` clears the sprint field via the working generic connector), then retry
the sprint-state transition, and if it still fails, report the exact error
and ask the owner to re-auth rather than leaving it silently unresolved.

### 7. Rebuild/restart prod and dev from main

**Prod (local host):**

```bash
scripts/asb rebuild full
```

Verify: `docker ps --format '{{.Names}}\t{{.Status}}'` shows all containers
`healthy`, and `curl http://localhost:8080/status` reports the new version.
Watch for the two real bugs found and fixed 2026-08-13 in this exact path —
`update-agentshroud.sh` previously skipped rebuilding Hermes's local image
after a pin bump (silent no-op) and skipped sourcing `docker/.env` (silent
model-config reversion to cloud/Anthropic); both are now fixed, but verify
the deployed Hermes model config is still correct
(`docker exec agentshroud-hermes-v2 hermes --version`, and check
`/opt/data/config.yaml`'s `model:` section) rather than assuming.

**Dev (remote — agentshroud-bot's own host, separate from this session's
direct SSH sandboxing used by the i-hdev/i-odev skills):**

```bash
ssh agentshroud-bot@<dev-host-ip> "cd ~/Development/agentshroud && git checkout main && git pull && scripts/asb rebuild full"
```

Confirm the target IP against memory (`feedback_allowed_ips.md` — the 4 lab
hosts) before connecting; don't guess or reuse a stale IP from an old
session. Verify the same way as prod: containers healthy, version endpoint
correct.

## Guardrails

- Never skip a step silently because it's inconvenient (e.g. don't merge
  around a real CI failure, don't skip the Jira close because the connector
  errored once — retry with the fallback path above, then report honestly if
  it's still blocked).
- This skill performs real, hard-to-reverse actions (merge to main, a public
  git tag/release, closing tracking issues, restarting production). If
  invoked in a context where any of these would be a surprise (no prior
  discussion of "release it" for this specific PR), confirm scope with the
  owner before proceeding rather than assuming.
- Report a final summary: PR merged (link), version tagged/released (link),
  Jira issue + sprint state, prod status, dev status — don't just say
  "done," show the evidence for each piece (RULE C / RULE D format from
  AGENTS.md applies here too).
